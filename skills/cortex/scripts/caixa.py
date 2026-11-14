"""Inicia ou confere o Cérebro de uma empresa, sem sobrescrever conteúdo."""
import argparse
import json
import re
from pathlib import Path

from gerar_plugin import SLUG, _json_bytes, achar_cerebro, links_locais, manifestos

SKILL = Path(__file__).resolve().parents[1]
BLOCO = re.compile(r"<!-- (?:business-os|cortex):inicio.*?<!-- (?:business-os|cortex):fim -->\n?", re.S)
LIMITE_RESUMO = 400
MANIFESTOS = ("plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json")
CATALOGOS = (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json")
GITIGNORE = """/cerebro/fontes/
/entregas/
/tmp/
*.mp4
*.mov
*.wav
*.mp3
*.zip
*.csv
*.xlsx
**/node_modules/
**/dist/
**/.next/
**/.astro/
**/.wrangler/
**/.venv/
**/__pycache__/
*.pyc
.DS_Store
.env
.env.*
!.env.example""".splitlines()
SKILL_CONTEXTO = """---
name: contexto
description: {descricao}
---

# Cérebro de {titulo}

Leia primeiro [RESUMO.md](../../RESUMO.md). Depois abra só o que a tarefa pedir:

- [negocio.md](../../negocio.md): oferta, preços, dados práticos e operação
- [publico.md](../../publico.md): quem compra, dores, objeções e frases reais
- [mensagem.md](../../mensagem.md): posicionamento, provas, voz e limites
- [marca.md](../../marca.md): identidade visual
- [momento.md](../../momento.md): objetivo e prioridades
- [historico.md](../../historico.md): decisões e aprendizados

Na raiz deste plugin, duas pastas acima desta skill, podem existir `processos/`, `modelos/`, `conhecimento/` e `referencias/`. Liste a pasta e abra o arquivo do assunto.

## Regras

- Campo vazio é lacuna: pergunte, não invente.
- `(hipótese)` e `(a confirmar)` não viram afirmação pública.
- Promessa só com prova registrada em `mensagem.md`; respeite os limites de lá.
- Esta é a versão instalada do Cérebro. Para mudar algo, edite o repositório da empresa, não a cópia instalada.
"""


def _ler(path):
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def iniciar(pasta, nome=None, titulo=None):
    root = Path(pasta).resolve()
    brain = root / "cerebro"
    if (root / ".business-os").exists() and not brain.exists():
        raise ValueError("Pasta legada .business-os encontrada. Renomeie para cerebro e rode de novo.")
    if (brain / "plugin.json").is_file():
        nome = json.loads(_ler(brain / "plugin.json"))["name"]
    nome = nome or root.name
    if len(nome) > 64 or not SLUG.fullmatch(nome):
        raise ValueError("Informe --nome com letras minúsculas, números e hífens, até 64 caracteres.")
    titulo = titulo or nome
    if any(ord(c) < 32 for c in titulo):
        raise ValueError("--titulo não pode ter caracteres de controle.")
    feitos = []

    def gravar(path, data, sobrescrever=False):
        if path.exists() and (not sobrescrever or path.read_bytes() == data):
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        feitos.append(path.relative_to(root).as_posix())

    modelo = SKILL / "modelo"
    for source in sorted(modelo.rglob("*")):
        if source.is_file():
            gravar(brain / source.relative_to(modelo), source.read_bytes())

    descricao = "Cérebro de " + titulo + ": oferta, público, mensagem, marca, momento, processos e conhecimento."
    portable, codex, claude = manifestos(nome, titulo, "0.1.0", descricao)
    claude.update({"displayName": titulo, "author": {"name": titulo}})
    for rel, data in zip(MANIFESTOS, (portable, codex, claude)):
        gravar(brain / rel, _json_bytes(data))
    skill = SKILL_CONTEXTO.format(
        titulo=titulo,
        descricao=json.dumps(descricao + " Use em consultas, decisões e trabalhos sobre " + titulo + ".", ensure_ascii=False),
    )
    gravar(brain / "skills/contexto/SKILL.md", skill.encode("utf-8"))

    # Catálogos: preserva outras entradas e só corrige o destino desta.
    entradas = (
        ({"name": nome, "interface": {"displayName": titulo}},
         {"name": nome, "source": {"source": "local", "path": "./cerebro"},
          "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Productivity"}),
        ({"name": nome, "description": descricao, "owner": {"name": titulo}},
         {"name": nome, "source": "./cerebro", "description": descricao}),
    )
    for rel, (base, entrada) in zip(CATALOGOS, entradas):
        path = root / rel
        data = json.loads(_ler(path)) if path.is_file() else {**base, "plugins": []}
        atual = next((p for p in data.setdefault("plugins", []) if p.get("name") == nome), None)
        if atual is None:
            data["plugins"].append(entrada)
        else:
            atual["source"] = entrada["source"]
        if not path.is_file() or json.loads(_ler(path)) != data:
            gravar(path, _json_bytes(data), sobrescrever=True)

    nota = _ler(SKILL / "nota-agents.md")
    agents = _ler(root / "AGENTS.md")
    if BLOCO.search(agents):
        agents = BLOCO.sub(lambda _: nota, agents, count=1)
    else:
        agents = (agents.rstrip("\n") + "\n\n" if agents.strip() else "") + nota
    gravar(root / "AGENTS.md", agents.encode("utf-8"), sobrescrever=True)

    claude_md = _ler(root / "CLAUDE.md")
    if "@AGENTS.md" not in claude_md:  # com CLAUDE.md presente, o Claude Code não lê o AGENTS.md
        claude_md = (claude_md.rstrip("\n") + "\n" if claude_md.strip() else "") + "@AGENTS.md\n"
        gravar(root / "CLAUDE.md", claude_md.encode("utf-8"), sobrescrever=True)

    ignore = _ler(root / ".gitignore")
    faltam = [line for line in GITIGNORE if line not in {x.strip() for x in ignore.splitlines()}]
    if faltam:
        ignore = (ignore.rstrip("\n") + "\n\n" if ignore.strip() else "") + "# Cortex\n" + "\n".join(faltam) + "\n"
        gravar(root / ".gitignore", ignore.encode("utf-8"), sobrescrever=True)
    return feitos


def conferir(pasta):
    root = Path(pasta).resolve()
    try:
        brain = achar_cerebro(root)
    except ValueError as error:
        return [str(error)]
    problemas = []
    if brain.name != "cerebro":
        problemas.append("Pasta legada .business-os: renomeie para cerebro.")

    ids = set()
    for rel in MANIFESTOS:
        try:
            manifest = json.loads(_ler(brain / rel))
            ids.add((manifest["name"], manifest["version"]))
        except (ValueError, KeyError, TypeError):
            problemas.append("Manifesto ausente ou inválido: " + rel)
    if len(ids) > 1:
        problemas.append("Nome ou versão diferentes entre os manifestos.")
    nome = next(iter(ids))[0] if len(ids) == 1 else None
    for rel in CATALOGOS:
        try:
            source = next(p["source"] for p in json.loads(_ler(root / rel))["plugins"] if p["name"] == nome)
            if (source["path"] if isinstance(source, dict) else source) != "./" + brain.name:
                raise ValueError
        except (ValueError, KeyError, TypeError, StopIteration):
            problemas.append("Catálogo ausente ou sem apontar para ./" + brain.name + ": " + rel)
    if not (brain / "skills/contexto/SKILL.md").is_file():
        problemas.append("Skill ausente: skills/contexto/SKILL.md")

    resumo = re.sub(r"<!--.*?-->", "", _ler(brain / "RESUMO.md"), flags=re.S)
    palavras = len(resumo.split())
    if not palavras:
        problemas.append("RESUMO.md ausente ou vazio.")
    elif palavras > LIMITE_RESUMO:
        problemas.append("RESUMO.md com %d palavras; o limite é %d. Leve o detalhe para os outros arquivos." % (palavras, LIMITE_RESUMO))

    for doc in sorted(brain.rglob("*.md")):
        if "fontes" in doc.relative_to(brain).parts:
            continue
        for link in links_locais(_ler(doc)):
            target = (doc.parent / link).resolve()
            if not target.exists() or not target.is_relative_to(brain.resolve()):
                problemas.append("Link quebrado ou para fora do Cérebro: %s -> %s" % (doc.relative_to(brain).as_posix(), link))

    nota = _ler(SKILL / "nota-agents.md")
    if nota not in _ler(root / "AGENTS.md"):
        problemas.append("Bloco do Cortex ausente ou desatualizado no AGENTS.md; rode iniciar.")
    if (root / "CLAUDE.md").is_file() and "@AGENTS.md" not in _ler(root / "CLAUDE.md"):
        problemas.append("CLAUDE.md sem a linha @AGENTS.md.")
    return problemas


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="comando", required=True)
    start = commands.add_parser("iniciar", help="cria ou atualiza a estrutura padrão")
    start.add_argument("pasta")
    start.add_argument("--nome", help="identificador do plugin, em kebab-case")
    start.add_argument("--titulo", help="nome da empresa como deve aparecer")
    commands.add_parser("conferir", help="aponta o que foge do padrão").add_argument("pasta")
    args = parser.parse_args()
    try:
        if args.comando == "iniciar":
            feitos = iniciar(args.pasta, args.nome, args.titulo)
            print("\n".join(feitos) if feitos else "Nada a criar: a estrutura já está no padrão.")
            return
        problemas = conferir(args.pasta)
    except (ValueError, OSError, UnicodeError, KeyError) as error:
        parser.exit(1, "Não foi possível concluir: " + str(error) + "\n")
    if problemas:
        parser.exit(1, "\n".join(problemas) + "\n")
    print("Cérebro no padrão.")


if __name__ == "__main__":
    main()
