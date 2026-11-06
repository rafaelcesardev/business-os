# business-os

Plugin para Claude Code e Codex que organiza o contexto e conduz o trabalho de negócios próprios ou de clientes por três entradas: Business OS, Marketing e Comercial.

## Arquitetura

- **Método no plugin, dados fora.** Este repositório guarda métodos, recursos e testes. O contexto de cada
  negócio mora numa pasta `.business-os/` na raiz da pasta do negócio. Nunca
  colocar contexto de negócio dentro deste repo.
- **Achar o contexto:** a partir da pasta atual, subir pelos diretórios até
  encontrar `.business-os/`, como o git encontra `.git`.
- **Saídas** das skills vão para a pasta do negócio, não para
  dentro de `.business-os/`.
- **Regras de contexto:** campo vazio é lacuna (perguntar, não inventar); o que
  não foi confirmado leva `(hipótese)` ou `(a confirmar)`; provas e frases reais
  citam o arquivo de `fontes/` de onde vieram.

## Estrutura

```text
plugin.json                         manifesto portátil
.agents/plugins/                    catálogo Codex
.codex-plugin/                      manifesto Codex
.claude-plugin/                     manifesto e catálogo Claude Code
skills/business-os/
  SKILL.md                          contexto, organização e encaminhamento
  criar.md, alimentar.md, usar.md   modos de contexto
  modelo/, roteiro-entrevista.md    modelo e entrevista
  nota-agents.md, modelo-readme.md  instruções da empresa
  contexto.md, organizacao.md       regras compartilhadas
  references/                      plugin, e-mail e análise de dados
  scripts/gerar_plugin.py           exportador opcional
skills/marketing/
  SKILL.md                          atração, divulgação e presença digital
  references/                      procedimentos e recursos da área
skills/comercial/
  SKILL.md                          vendas, atendimento e processos
  references/                      procedimentos e recursos da área
tests/                              testes com dados fictícios
```

## Entradas e procedimentos

- Somente `skills/business-os/SKILL.md`, `skills/marketing/SKILL.md` e `skills/comercial/SKILL.md` são entradas. Os demais métodos são referências `.md`, não skills adicionais.
- O Business OS recebe qualquer pedido e encaminha pela finalidade. Marketing e Comercial são atalhos opcionais; não exija que o usuário escolha métodos internos.
- Leia `RESUMO.md` primeiro e carregue somente o contexto e as referências necessários. E-mail e análise de dados são compartilhados: divulgação e campanhas seguem Marketing; oportunidades, cobrança e atendimento seguem Comercial; decisões gerais podem permanecer no Business OS.
- Preserve textos aprovados, limites da empresa e verificações dos procedimentos. Planejar, analisar, produzir, publicar e configurar serviços são ações distintas; uma não autoriza automaticamente a seguinte.

## Convenções

- Skills em português, com acentos corretos.
- O plugin roda no Claude Code e no Codex: nada de instrução que só funcione num
  dos dois sem alternativa pro outro.

## Entregas de contexto e validação

- Cada negócio novo usa um repositório privado com raiz em kebab-case e subpastas curtas. O Git guarda a base revisada `.business-os/`, o código em `site/` e a configuração da raiz; produção e bruto local ficam ignorados, com backup próprio. O padrão completo está em `skills/business-os/organizacao.md`.
- A própria `.business-os/` pode ser a raiz do plugin da empresa, com catálogos Codex e Claude Code no repositório e uma única base editável. O exportador para `entregas/plugins/` continua opcional para entregar uma seleção. Não coloque dados de uma empresa neste repositório de métodos.
- O manifesto portátil é `plugin.json`; mantenha identidade e versão coerentes com `.codex-plugin/plugin.json` e `.claude-plugin/plugin.json`.
- Processos e instruções aprovados ficam na base de contexto; rascunhos e testes ficam na área local de atendimento. Registre os caminhos existentes antes de sugerir reorganização; não mova históricos ou sistemas automaticamente.
- O exportador usa somente a biblioteca padrão do Python. Ao mudá-lo, rode `python3 -m unittest discover -s tests -v`. Nunca use dados reais de uma empresa nos testes ou fixtures deste repositório.
