# Fontes e escolhas dos procedimentos de gestão

Pesquisa realizada em 6 de novembro de 2026, antes da implementação. Escopo: revisão do negócio, continuidade do trabalho e acompanhamento de resultados. Propostas comerciais, entrega ao cliente e financeiro não foram ampliados nesta etapa.

## O que a pesquisa comprova

As fontes abaixo documentam práticas e instruções existentes. Não comprovam que uma adaptação ao Cortex melhora resultados. Instalações e estrelas ajudam a selecionar candidatos para leitura; não medem a qualidade das respostas nem a eficácia numa empresa. A validação local continua necessária.

## Skills avaliadas

Busca no catálogo [skills.sh](https://skills.sh/) e com `npx skills find`: `weekly review`, `session handoff` e `retrospective`. Os candidatos selecionados tiveram o corpo das instruções lido; uma listagem de busca sozinha não sustentou a decisão.

| Skill e origem | Sinal observado na consulta | O que aproveitar | Decisão e limites |
| --- | --- | --- | --- |
| [metrics-review — Anthropic](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/metrics-review/SKILL.md) | Cerca de 3 mil instalações; repositório oficial, cerca de 34,9 mil estrelas; Apache-2.0 | Comparar valor atual, período anterior e meta; registrar qualidade dos dados e cautela com atribuição | Referência para conferir resultados. Não importar a hierarquia de métricas de software, benchmarks ou metas universais para qualquer empresa. |
| [weekly-wrap — Anthropic](https://github.com/anthropics/knowledge-work-plugins/blob/main/sales/skills/weekly-wrap/SKILL.md) | 307 instalações; mesmo repositório e licença | Revisar mudanças, pendências e próximos compromissos a partir de registros | Aproveitar a estrutura de revisão. Rejeitar a aproximação de mudança de etapa pela data de edição: edição não comprova progresso. Não importar regras de conectores ou envio. |
| [session-handoff — Leonardo Flores / Softaworks](https://github.com/softaworks/agent-toolkit/blob/main/skills/session-handoff/SKILL.md) | Cerca de 4,2 mil instalações e 2,6 mil estrelas; MIT | Registrar estado, decisões, arquivos e próximo passo; conferir se o estado ainda vale ao retomar | Referência para continuidade. Não adotar scripts, pontuação de qualidade ou armazenamento exclusivo em `.claude/`. |
| [weekly-review — Cursor](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/weekly-review/SKILL.md) | Cerca de 2,5 mil instalações; repositório oficial com cerca de 15,5 mil estrelas | Limitar afirmações à evidência disponível | Não adotar como revisão empresarial: seu insumo é histórico de commits. Licença específica não foi verificada, pois não será incorporado. |
| `design-kpis` — plugin Data instalado | Instruções locais lidas; não foi levantado número de instalações | Escolher medidas pela decisão, explicar cálculo e fonte, separar seleção da métrica de definição da meta | Referência complementar; não torna Data uma dependência. Não importar suas rotas de apresentação. |
| `notion-weekly-project-digest` — plugin Notion instalado | Instruções locais lidas; não foi levantado número de instalações | Comparar observações datadas, carregar bloqueios persistentes e reconhecer a primeira fotografia | Referência complementar; sem exigir Notion nem importar seus comandos. |

Para reconsulta do conteúdo externo: a árvore Git consultada da Anthropic foi `ab4cb1cd383b4eb87383be8cf4e70cb5b2a2348d`; os blobs de `metrics-review` e `weekly-wrap` foram, respectivamente, `42416640d925635863da3738107973996d43b6a1` e `050aceabf8f83355d18414f248d67ab1a7e8b85d`. O blob do `weekly-review` do Cursor foi `216e855f7831afacac92c46345fee2ea4ba14629`. São identificadores de árvore/arquivo, não versões de lançamento. Softaworks foi consultado na branch `main`, sem fixação de commit.

## Conteúdo dos profissionais e instituições

| Fonte primária | Prática documentada | Aplicação e limite |
| --- | --- | --- |
| [David Allen — revisão semanal GTD](https://gettingthingsdone.com/2018/08/episode-43-the-power-of-the-gtd-weekly-review/) | Revisar ações, calendário, itens aguardando retorno e projetos com próxima ação | Sustenta a revisão de pendências e continuidade. É uma prática de produtividade; não prova resultado comercial. |
| [EOS Worldwide — Level 10 Meeting](https://www.eosworldwide.com/level-10-meeting) | Cadência semanal com indicadores, prioridades, compromissos e problemas a resolver | Sustenta uma revisão que termine em decisões. Não reproduzir a agenda proprietária nem chamar a adaptação de EOS/Level 10; duração e frequência dependem do negócio. |
| [IHI — Model for Improvement, desenvolvido por Associates in Process Improvement](https://www.ihi.org/library/model-for-improvement) | Relacionar objetivo, evidência de melhoria e mudanças testáveis | Sustenta a ligação entre entrega e resultado esperado. A aplicação aqui é uma adaptação, não validação pelo IHI. |
| [IHI — definição de medidas](https://www.ihi.org/library/model-for-improvement/establishing-measures) | Distinguir resultado, execução do processo e efeitos indesejados | Sustenta a escolha das medidas e seus limites. Não importar indicadores clínicos nem uma quantidade fixa de métricas. |
| [IHI — testes de mudança com PDSA](https://www.ihi.org/library/model-for-improvement/testing-changes) | Planejar um teste pequeno, registrar previsão e execução, estudar o observado e ajustar | Sustenta o acompanhamento de uma mudança. Uma comparação antes/depois sozinha não prova causalidade. |
| [Atlassian — retrospectivas](https://www.atlassian.com/agile/scrum/retrospectives/) | Transformar reflexão em ações com responsáveis e datas, acompanhando sua execução | Sustenta o fechamento de revisões. Não exigir sprints, cerimônias ou Jira. |

## O que foi criado no Cortex

Estas são escolhas de implementação locais, sem alegação de serem exigidas pelas fontes:

- Manter três entradas e acrescentar referências compartilhadas: [revisar negócio](revisar-negocio.md), [continuar trabalho](continuar-trabalho.md) e [conferir resultados](conferir-resultados.md).
- Reutilizar a ferramenta de trabalho existente. Sem uma, usar `planejamento/andamento.md`; revisões ficam em `analises/`. Os caminhos são convenções locais, não práticas comprovadas por uma skill externa.
- Guardar somente apontadores no contexto revisado; andamento, números operacionais e rascunhos ficam na fonte de trabalho. Um plugin instalado não oferece estado em tempo real.
- Não obrigar um pedido simples de texto ou imagem a passar por uma revisão de gestão. O acompanhamento entra quando o pedido ou o trabalho continuado o exigir.
- Não instalar skills externas, executar seus scripts ou adicionar serviços para reaproveitar uma prática.

Os procedimentos foram escritos em português para a arquitetura do Cortex, com atribuição às referências, sem incorporar arquivos, scripts ou templates de terceiros. Os nomes dos métodos e autores identificam a origem, sem sugerir parceria ou certificação.

## Como validar

Os [cenários fictícios](../../../tests/cenarios-gestao.md) cobrem dados ausentes, histórico incompleto, retomada desatualizada, duplicação e separação entre entrega e resultado. São casos para avaliação de respostas, não prova automática de eficácia. A primeira revisão de um negócio real deve registrar a base observada; só revisões posteriores permitem avaliar continuidade e utilidade. Testes de estrutura e exportação não validam comportamento do modelo ou resultado empresarial.
