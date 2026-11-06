# Organização do negócio

## Um repositório por empresa

Para um negócio novo, use uma raiz em kebab-case, por exemplo `churrascaria-do-jonas/`. Dentro dela use nomes curtos, também em kebab-case, sem repetir o nome da empresa. O padrão é um único repositório privado; outro repositório só quando houver necessidade própria de acesso, manutenção ou entrega. Não mude a visibilidade de um repositório existente ao aplicar o padrão.

```text
churrascaria-do-jonas/
  .gitignore
  AGENTS.md
  CLAUDE.md
  README.md
  .agents/plugins/marketplace.json     catálogo Codex, quando houver plugin
  .claude-plugin/marketplace.json      catálogo Claude Code, quando houver plugin
  .business-os/
    RESUMO.md
    negocio.md
    publico.md
    mensagem.md
    marca.md
    momento.md
    historico.md
    assets/                           arquivos oficiais da marca
    referencias/                      repertório revisado e leve
    processos/                        processos aprovados
    agentes/                          instruções e bases aprovadas
    fontes/                           bruto local, ignorado pelo Git
    plugin.json                       quando o contexto for instalável
    .codex-plugin/plugin.json          compatibilidade Codex
    .claude-plugin/plugin.json         compatibilidade Claude Code
    skills/contexto/SKILL.md           consulta aos mesmos arquivos acima
  site/                               código versionado
  planejamento/                       andamento e planos locais, se usados
  analises/                           revisões e conferências locais, se usadas
  marketing/                          produção local
  atendimento/
    processos/                        rascunhos locais
    agentes/                          versões de trabalho e testes locais
  entregas/                           pacotes e exportações locais
  tmp/                                temporários locais
```

Os sete documentos do contexto continuam existindo; as subpastas os complementam. Crie as pastas de conteúdo somente quando usadas. Ao preparar ou reabrir o projeto em outra máquina, o Business OS recria as áreas locais com os mesmos nomes; o Git não restaura pastas ignoradas nem seu conteúdo. Os arquivos de produção precisam de backup separado; ignorar não significa apagar.

## O que vai para o Git

| Local | Regra |
| --- | --- |
| `.business-os/`, exceto `fontes/` | Base revisada: fatos, lacunas, identidade, decisões, referências leves, processos e instruções aprovados |
| `site/` | Código, recursos necessários e configuração; dependências, caches e builds ficam fora |
| Catálogos e arquivos da raiz | Metadados do plugin e orientação para trabalhar com o repositório |
| `planejamento/`, `analises/`, `marketing/`, `atendimento/`, `entregas/`, `tmp/` | Trabalho local; não versionar andamento, análises operacionais, vídeos, renders, carrosséis, projetos de produção ou ZIPs |

Aplique estas regras na `.gitignore` da raiz, preservando as demais regras existentes:

```gitignore
/marketing/
/atendimento/
/entregas/
/tmp/
/planejamento/
/analises/
/.business-os/fontes/
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
!.env.example
```

Antes de versionar, confira os arquivos que de fato entrarão com `git status` e `git diff --cached --stat`. `.gitignore` não remove arquivos já rastreados: identifique-os com `git ls-files` e trate a mudança de rastreamento e de histórico como parte da migração autorizada, preservando os arquivos locais. Não use `git add .` indiscriminadamente para importar um projeto antigo.

No Cloudflare, a raiz do projeto de site e os caminhos que disparam build são configurações distintas. Configure-os conforme o projeto, incluindo dependências compartilhadas reais. Um deploy separado não exige outro repositório; não altere a conta ou a publicação só por organizar as pastas.

## Contexto aprovado e trabalho local

A identidade e as escolhas visuais ficam em `marca.md`. Registre o repertório durável em `referencias/`: URL, autor, o que aproveitar, limites de uso e, quando adequado, um arquivo leve. Acervos completos, downloads e vídeos de referência ficam em `marketing/referencias/`; o contexto aponta para o acervo sem duplicá-lo. Uma referência externa não vira uma regra ou afirmação factual da empresa.

Rascunhos de processos, prompts, simulações e logs ficam em `atendimento/`. Quando o responsável aprovar uma versão, promova o documento para `.business-os/processos/<processo>.md` ou `.business-os/agentes/<nome>/`, registre a decisão no histórico e atualize os caminhos no resumo e nos consumidores. A aprovação do texto não comprova implantação ou teste no CRM. O documento aprovado é a fonte principal; não mantenha duas cópias editadas em paralelo. Ao revisá-lo, mantenha a versão aprovada até a substituição ser aprovada.

Para [continuidade](references/continuar-trabalho.md), reutilize a fonte de andamento existente. Sem uma, use `planejamento/andamento.md`; [revisões](references/revisar-negocio.md) e [conferências de resultado](references/conferir-resultados.md) usam a área existente ou `analises/`. São registros locais com backup separado. Em `momento.md`, guarde somente os apontadores necessários; decisões e aprendizados confirmados seguem para o contexto pelo procedimento [alimentar](alimentar.md). Não copie dados operacionais para o plugin de contexto por conveniência. Preserve caminhos e políticas de versionamento de projetos existentes; não mova nem retire arquivos do Git automaticamente.

## Uma fonte, dois usos

A própria `.business-os/` pode ser a raiz do plugin da empresa: os catálogos na raiz do repositório apontam para ela e a skill de contexto lê os documentos originais. Não é necessário exportar ou duplicar os arquivos para trabalhar no repositório ou instalar pelo marketplace. Veja [plugin no próprio repositório](references/repositorio-plugin.md).

Tudo que for distribuído dentro dessa raiz do plugin deve ser adequado ao destinatário. As fontes brutas locais ficam fora do Git; valide o conteúdo de um clone dos arquivos versionados antes de distribuir. A lista do exportador não filtra o conteúdo da instalação por repositório. Para entregar só uma seleção, use o exportador opcional em `entregas/plugins/`.

Quando houver logo oficial, use-a no ícone: `composerIcon` e `logo` nos metadados OpenAI e `icon` no manifesto Claude Code, com caminhos dentro da raiz do plugin. Prepare uma versão quadrada e legível em PNG ou JPEG. Sem logo oficial, mantenha o ícone padrão; não use a marca de outra empresa.

O repositório é a fonte editável. Os clientes instalam uma cópia versionada, não uma leitura em tempo real: alterar o contexto exige nova versão coerente dos manifestos e atualização do plugin instalado. Não edite caches nem mantenha outro contexto manualmente no pacote.

## Compatibilidade e migração

Métodos antigos podem ter salvo processos em `processos/`, agentes em `agentes/` e projetos em repositórios com outros nomes. Leia esses materiais antes de criar algo novo. Se a tarefa exigir mudar caminhos, mapeie quem os usa, preserve os arquivos e verifique os links antes de encerrar.

Para planejar uma reorganização, apresente o destino concreto e os arquivos afetados. Execute só a etapa autorizada. Arquivos temporários, duplicatas e recursos ainda usados precisam ser distinguidos por evidência, não pelo nome da pasta.
