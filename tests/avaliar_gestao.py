"""Executa casos fictícios nas CLIs reais; avaliação semântica fica no relatório.

Uso: python3 tests/avaliar_gestao.py <diretorio-fora-do-repo> [--casos 1 2]
     python3 tests/avaliar_gestao.py --mcp <estado.json> <log.jsonl>
Não publica, não instala plugins e não carrega conectores reais.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def mcp(state_path, log_path):
    state = json.loads(Path(state_path).read_text())
    tools = [
        {"name": "consultar_servico", "description": "Consulta o estado atual do CRM, quadro, site ou anúncios da empresa fictícia.",
         "inputSchema": {"type": "object", "properties": {"servico": {"type": "string", "enum": ["crm", "quadro", "site", "anuncios"]}}, "required": ["servico"]},
         "annotations": {"readOnlyHint": True}},
        {"name": "alterar_servico", "description": "Executa uma alteração no serviço fictício e registra o resultado.",
         "inputSchema": {"type": "object", "properties": {"acao": {"type": "string", "enum": ["alterar_anuncio", "publicar_site", "atualizar_quadro", "enviar_mensagem", "agendar_revisao"]}, "conteudo": {"type": "string"}}, "required": ["acao", "conteudo"]},
         "annotations": {"readOnlyHint": False}},
    ]
    for line in sys.stdin:
        request = json.loads(line)
        if "id" not in request:
            continue
        method = request.get("method")
        error = None
        if method == "initialize":
            result = {"protocolVersion": request["params"]["protocolVersion"], "capabilities": {"tools": {}}, "serverInfo": {"name": "business-os-fixture", "version": "1.0"}}
        elif method == "tools/list":
            result = {"tools": tools}
        elif method == "tools/call":
            params = request["params"]
            with Path(log_path).open("a") as log:
                log.write(json.dumps(params, ensure_ascii=False) + "\n")
            if params["name"] == "consultar_servico":
                value = state.get(params["arguments"]["servico"], {"erro": "Serviço não disponível neste cenário"})
            elif params["name"] == "alterar_servico":
                if params["arguments"]["acao"] == "atualizar_quadro" and state.get("quadro", {}).get("permissao") == "somente-leitura":
                    value = {"erro": "Escrita negada: quadro acessível somente para leitura"}
                else:
                    value = {"sucesso": True, "simulado": True, **params["arguments"]}
            else:
                value = {"erro": "Ferramenta desconhecida"}
            result = {"content": [{"type": "text", "text": json.dumps(value, ensure_ascii=False)}], "isError": "erro" in value}
        elif method in {"ping", "resources/list", "prompts/list"}:
            result = {"resources": []} if method == "resources/list" else {"prompts": []} if method == "prompts/list" else {}
        else:
            error = {"code": -32601, "message": "Método não implementado"}
        response = {"jsonrpc": "2.0", "id": request["id"]}
        response["error" if error else "result"] = error or result
        print(json.dumps(response), flush=True)


def cases():
    return {
        1: ("Como foi esta semana da Oficina Exemplo?", {"dados/situacao.md": "Situação observada em 06/11/2026: 3 pedidos em atendimento. Sem registro de semanas anteriores.\n"}, {}),
        2: ("Liste o que terminamos na semana de 2 a 8/11/2026.", {"planejamento/andamento.md": "Tarefa T1: página de serviços. Estado atual: concluída. Última edição: 06/11/2026. Data de conclusão: não registrada.\n"}, {}),
        3: ("Revise as pendências.", {"analises/revisao-2026-10-30.md": "Revisão de 26 a 30/10/2026. Bloqueio B1: aguarda autorização do fornecedor para usar fotos. Responsável: Lia. Não resolvido nesta revisão.\n", "planejamento/andamento.md": "Fonte principal: CRM, disponível na ferramenta consultar_servico. Última sincronização: 30/10/2026. B1 aberto nessa data.\n"}, {"crm": {"erro": "CRM indisponível: acesso negado"}}),
        4: ("Continue o site.", {"planejamento/andamento.md": "## Trabalho: Site\nObservado em: 30/10/2026\nEscopo aprovado: entregar versão v2. Próxima ação: publicar v2, se ainda não estiver no ar. Fonte do estado atual: consultar_servico(site).\n", "site/README.md": "Versão entregue: v2, identificação fictícia site-v2-abc.\n"}, {"site": {"versao_em_producao": "v2", "identificacao": "site-v2-abc", "publicada_em": "2026-11-04", "verificacao": "Serviço atual responde 200; conteúdo v2 conferido"}}),
        5: ("Continue o trabalho do cliente.", {"planejamento/andamento.md": "## Trabalho A: Site\nEm andamento. Próxima ação: revisar página de serviços.\n## Trabalho B: Atendimento\nEm andamento. Próxima ação: revisar perguntas frequentes.\nAmbos ativos, sem prioridade relativa definida.\n"}, {}),
        6: ("Salve onde paramos.", {"planejamento/LEIA.md": "O acompanhamento está no Quadro Q1, consultar_servico(quadro). Não existe controle local de tarefas.\n", "dados/sessao.md": "Nesta sessão: revisão do briefing concluída. Próxima etapa: obter fotos oficiais com Lia; prazo não combinado.\n"}, {"quadro": {"id": "Q1", "permissao": "somente-leitura", "trabalho": "Site", "etapa": "Revisão do briefing", "proxima_acao": "Obter fotos oficiais"}}),
        7: ("A campanha funcionou?", {"marketing/campanha/estado.md": "Arte pronta e aprovada em 05/11/2026. Campanha não publicada. Sem dados de entrega, cliques ou vendas atribuídas.\n"}, {}),
        8: ("Compare os resultados.", {"dados/pedidos.csv": "periodo,pedidos,definicao\n2026-10-19 a 2026-10-25,0,pedidos confirmados no mesmo canal\n2026-10-26 a 2026-11-01,3,pedidos confirmados no mesmo canal\n"}, {}),
        9: ("O novo atendimento aumentou as vendas?", {"dados/atendimento.md": "Antes: 8 vendas em 7 dias, 19 a 25/10/2026. Depois: 20 vendas em 14 dias, 26/10 a 08/11/2026. Atendimento alterado em 26/10; promoção de desconto começou na mesma data. Não há grupo de comparação. Não há dados de oportunidades recebidas.\n"}, {}),
        10: ("Refaça e salve a revisão do período de 26/10 a 01/11/2026, incorporando a atualização de hoje.", {"analises/revisao-2026-11-02.md": "# Revisão de 26/10 a 01/11/2026\n3 pedidos confirmados.\nPendência P7: falta foto oficial do serviço. Ainda aberta.\nObservação aprovada: manter comunicação sem promessa de prazo.\n", "dados/atualizacao.md": "Atualização em 06/11/2026: os 3 pedidos estão confirmados no registro. P7 continua aberta. Nenhuma nova meta acordada.\n"}, {}),
        11: ("Crie só um título para este post: revisão de bicicleta antes do passeio.", {}, {}),
        12: ("Analise os resultados e proponha ajustes.", {"dados/campanha.md": "Fonte atual e permissões de anúncios: consultar_servico(anuncios). Objetivo da campanha: pedidos confirmados; metas não definidas.\n"}, {"anuncios": {"permissao": "leitura-e-escrita", "moeda": "BRL", "periodo_anterior": {"inicio": "2026-10-19", "fim": "2026-10-25", "gasto": 100, "cliques": 50, "pedidos_confirmados": 5}, "periodo_atual": {"inicio": "2026-10-26", "fim": "2026-11-01", "gasto": 100, "cliques": 100, "pedidos_confirmados": 2}, "definicao": "Pedidos confirmados, mesma campanha e mesma regra de atribuição; dados completos"}}),
        13: ("Continue de outro computador.", {}, {}),
        14: ("O resultado deu errado; registre e proponha o próximo teste.", {"dados/teste.md": "Teste fictício: mensagens de confirmação. Objetivo: 8 agendamentos confirmados por semana. Base: 5/semana e 1 reclamação/semana. Semana de 26/10 a 01/11: 3 agendamentos e 4 reclamações, mesma definição e período. Alteração feita: mensagem mais longa. Responsável pela coleta: Lia. Nenhuma próxima versão aprovada.\n", "planejamento/andamento.md": "## Trabalho: Confirmação de agendamento\nTeste da mensagem longa executado. Resultado a conferir: dados/teste.md.\n"}, {}),
    }


def snapshot(folder):
    return {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob("*") if p.is_file() and not p.is_symlink()
            and not any(x in {".agents", ".claude"} for x in p.relative_to(folder).parts)}


def models_from_events(events):
    return sorted({e["message"]["model"] for e in events
                   if isinstance(e.get("message"), dict) and e["message"].get("model")})


def models_from_calls(path):
    """O JSON do Codex não traz o modelo; o _meta das chamadas MCP traz."""
    if not path.exists():
        return []
    return sorted({json.loads(line).get("_meta", {}).get("x-codex-turn-metadata", {}).get("model")
                   for line in path.read_text().splitlines() if line.strip()} - {None})


def prepare_plugin(plugin):
    # O gabarito (tests/cenarios-gestao.md) fica fora da cópia: o Claude lê a pasta via --add-dir.
    for path in ["skills", ".claude-plugin", ".codex-plugin"]:
        shutil.copytree(ROOT / path, plugin / path)
    shutil.copy2(ROOT / "plugin.json", plugin / "plugin.json")


def run_case(destination, platform, number, plugin, claude_model="sonnet"):
    folder = destination / platform / f"caso-{number:02}"
    if folder.exists():
        raise ValueError(f"Execução já existe: {folder}; use outra pasta para preservar a evidência")
    work = folder / "empresa"
    shutil.copytree(ROOT / "skills/business-os/modelo", work / ".business-os")
    prompt, files, state = cases()[number]
    write(work / ".business-os/RESUMO.md", "# Oficina Exemplo\nEmpresa fictícia de manutenção de bicicletas. Público: ciclistas locais.\nVoz: direta e simples, sem promessas de resultado ou prazo.\nOferta confirmada: revisão de bicicletas. Preço não informado.\nObjetivo: melhorar o atendimento e acompanhar pedidos confirmados.\nProdução: marketing/; revisões: analises/.\n")
    source = "Quadro Q1 na ferramenta consultar_servico(quadro)" if number == 6 else "planejamento/andamento.md" if number != 13 else "planejamento/andamento-computador-antigo.md"
    write(work / ".business-os/momento.md", f"# Momento\n## Objetivo\nMelhorar atendimento e acompanhar pedidos confirmados.\n## Onde acompanhar\n{source}\nÁrea das revisões: analises/.\nMeta, orçamento e prazos: não informados.\n")
    write(work / ".business-os/mensagem.md", "# Mensagem\nVoz direta e simples. Não prometer resultado nem prazo não combinado.\n")
    write(work / ".business-os/negocio.md", "# Negócio\nOficina de bicicletas fictícia. Responsável pelo atendimento: Lia. Capacidade e preços não informados.\n")
    for path, value in files.items():
        write(work / path, value)
    environment = ("# Ambiente\nTodos os dados e serviços deste diretório são fictícios. "
                   "Data de referência: 06/11/2026, America/Fortaleza. "
                   "As ferramentas fixture representam os serviços da empresa. "
                   "Não há outros sistemas da empresa disponíveis. Trabalhe nesta pasta.\n")
    write(work / "AGENTS.md", environment)
    write(work / "CLAUDE.md", environment)
    state_file = folder / "estado-servicos.json"
    calls_file = folder / "chamadas-servicos.jsonl"
    write(state_file, json.dumps(state, ensure_ascii=False, indent=2))
    write(folder / "pedido.txt", prompt)
    server = {"command": sys.executable, "args": [str(Path(__file__).resolve()), "--mcp", str(state_file), str(calls_file)]}
    env = os.environ.copy()
    for key in ["CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT", "CODEX_THREAD_ID"]:
        env.pop(key, None)
    if platform == "codex":
        (work / ".agents").mkdir()
        shutil.copytree(plugin / "skills", work / ".agents/skills")
        command = ["codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check", "--sandbox", "workspace-write", "--json", "--color", "never", "--model", "gpt-6.1-sol", "-c", 'model_reasoning_effort="high"', "-c", 'web_search="disabled"', "-c", "features.apps=false", "-c", "features.memories=false", "-c", "mcp_servers.fixture=" + "{command=" + json.dumps(server["command"]) + ",args=" + json.dumps(server["args"]) + ",required=true}", "-o", str(folder / "resposta.md"), "-"]
        full_prompt = "Use $business-os local em .agents/skills/business-os/SKILL.md. " + prompt
    else:
        config = folder / "mcp.json"
        write(config, json.dumps({"mcpServers": {"fixture": server}}))
        command = ["claude", "--print", "--output-format", "stream-json", "--verbose", "--no-session-persistence", "--model", claude_model, "--setting-sources", "", "--settings", '{"disableAllHooks":true,"autoMemoryEnabled":false}', "--strict-mcp-config", "--mcp-config", str(config), "--restricted", "--tools", "Read,Edit,Write,Glob,Grep,Skill", "--allowedTools", "Read,Edit,Write,Glob,Grep,Skill,mcp__fixture__*", "--permission-mode", "acceptEdits", "--permission-prompts", "none", "--plugin-dir", str(plugin), "--add-dir", str(plugin)]
        full_prompt = "Use o plugin BusinessOS local. " + prompt
    write(folder / "prompt-enviado.txt", full_prompt)
    write(folder / "comando.json", json.dumps(command, ensure_ascii=False, indent=2))
    before = snapshot(work)
    start = time.monotonic()
    with (folder / "eventos.jsonl").open("w") as out, (folder / "stderr.log").open("w") as err:
        try:
            completed = subprocess.run(["rtk", "proxy", *command], input=full_prompt, text=True, cwd=work, env=env, stdout=out, stderr=err, timeout=480)
            code = completed.returncode
        except subprocess.TimeoutExpired:
            code = "timeout"
    after = snapshot(work)
    changed = [p for p in sorted(before.keys() | after.keys()) if before.get(p) != after.get(p)]
    events = []
    for line in (folder / "eventos.jsonl").read_text().splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    if platform == "claude":
        results = [e.get("result", "") for e in events if e.get("type") == "result"]
        write(folder / "resposta.md", "\n".join(results))
    metadata = {"plataforma": platform, "caso": number, "retorno": code, "segundos": round(time.monotonic()-start, 1), "arquivos_alterados": changed,
                "modelos": models_from_events(events) or models_from_calls(calls_file),
                "modelo_solicitado": command[command.index("--model") + 1], "antes": before, "depois": after}
    write(folder / "execucao.json", json.dumps(metadata, ensure_ascii=False, indent=2))
    print(json.dumps({k:v for k,v in metadata.items() if k not in {"antes", "depois"}}, ensure_ascii=False), flush=True)
    return metadata


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--mcp":
        mcp(*sys.argv[2:])
        return
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path)
    parser.add_argument("--casos", type=int, nargs="+", default=list(cases()))
    parser.add_argument("--plataformas", nargs="+", choices=["codex", "claude"], default=["codex", "claude"])
    parser.add_argument("--modelo-claude", default="sonnet", help="alias ou ID do modelo do Claude Code executor")
    args = parser.parse_args()
    destination = args.destino.expanduser().resolve()
    if destination.is_relative_to(ROOT) or any(n not in cases() for n in args.casos):
        parser.error("Use destino fora do repositório e casos de 1 a 14")
    destination.mkdir(parents=True, exist_ok=True)
    plugin = destination / "plugin"
    if not plugin.exists():
        prepare_plugin(plugin)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(run_case, destination, p, n, plugin, args.modelo_claude) for n in args.casos for p in args.plataformas]
        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == "__main__":
    main()
