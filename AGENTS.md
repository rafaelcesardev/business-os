# cortex

Plugin para Claude Code e Codex. É a caixa de ferramentas que cria e mantém o **Cérebro** de cada empresa (contexto, decisões, marca, processos e conhecimento) e conduz o trabalho com ele por quatro entradas: Cortex, Iniciar, Marketing e Comercial.

## Arquitetura

- **Método no plugin, dados fora.** Este repositório guarda métodos, recursos e testes. O Cérebro de cada
  empresa mora na pasta `cerebro/` do repositório dela. Nunca colocar dados de uma empresa aqui.
- **Achar o Cérebro:** a partir da pasta atual, subir pelos diretórios até encontrar `cerebro/RESUMO.md`,
  como o git encontra `.git`. `.business-os/` é o nome antigo e continua aceito.
- **O Cérebro anda sozinho.** O `AGENTS.md` da empresa leva qualquer IA aos arquivos sem este plugin, e
  `cerebro/` é a raiz do plugin que a equipe instala. O Cérebro não carrega métodos.
- **Regras gerais** (lacuna, hipótese, prova, fonte única, autorização por ação) ficam só em
  `skills/cortex/contexto.md`. Os procedimentos apontam para lá; não as repita.

## Estrutura

```text
plugin.json                         manifesto portátil
.agents/plugins/                    catálogo Codex
.codex-plugin/                      manifesto Codex
.claude-plugin/                     manifesto e catálogo Claude Code
skills/cortex/
  SKILL.md                          encaminhamento pela finalidade do pedido
  contexto.md                       localizar o Cérebro e regras gerais
  criar.md, alimentar.md, usar.md   criar, atualizar e usar o Cérebro
  organizacao.md                    estrutura do repositório da empresa e Git
  modelo/, roteiro-entrevista.md    modelo do Cérebro e entrevista
  nota-agents.md, modelo-readme.md  bloco do AGENTS.md e README da empresa
  references/                       plugin da empresa, gestão, e-mail e análise de dados
  scripts/caixa.py                  monta (iniciar) e confere (conferir) o Cérebro
  scripts/gerar_plugin.py           exportador opcional de pacote separado
skills/iniciar/SKILL.md             atalho para criar o Cérebro
skills/marketing/
  SKILL.md                          posicionamento, divulgação e presença digital
  references/                       procedimentos e recursos da área
skills/comercial/
  SKILL.md                          prospecção, vendas, atendimento e processos
  references/                       procedimentos e recursos da área
tests/                              testes com dados fictícios
```

## Entradas e procedimentos

- As entradas são os quatro `SKILL.md`. Os demais métodos são referências `.md`, não skills adicionais.
- O Cortex recebe qualquer pedido e encaminha pela finalidade. Iniciar, Marketing e Comercial são atalhos opcionais; não exija que o usuário escolha métodos internos.
- E-mail e análise de dados são compartilhados: divulgação e campanhas seguem Marketing; oportunidades, cobrança e atendimento seguem Comercial; decisões gerais podem permanecer no Cortex.
- Conhecimento novo entra de duas formas: o princípio vira método ou checagem num procedimento, em texto próprio e com crédito à fonte; o resumo original fica no `cerebro/conhecimento/` da empresa que o estudou.

## Convenções

- Skills em português, com acentos corretos.
- O plugin roda no Claude Code e no Codex: nada de instrução que só funcione num
  dos dois sem alternativa pro outro.
- Escreva os métodos em tom direto. Ressalvas repetidas viram ressalvas repetidas no Cérebro das empresas.
- O que é determinístico na estrutura do Cérebro mora no `caixa.py`, não em exemplos em prosa. Mudou o
  bloco do `AGENTS.md`, aumente a versão no marcador de `nota-agents.md`.
- Mantenha identidade e versão iguais em `plugin.json`, `.codex-plugin/plugin.json` e `.claude-plugin/plugin.json`.
- Os scripts usam somente a biblioteca padrão do Python. Ao mudá-los, rode `python3 -m unittest discover -s tests -v`. Nunca use dados reais de uma empresa nos testes.
