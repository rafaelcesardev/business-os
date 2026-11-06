# Validação dos procedimentos de gestão — 06/11/2026

## Resultado

Os 14 [cenários](cenarios-gestao.md) passaram no Codex e no Claude Code em duas rodadas.

- **Primeira rodada:** 64 execuções, Claude em Opus 5.5.
- **Rodada independente:** 131 execuções.
  - Pastas `independente-01` a `-10`: 88 execuções, com o Claude em Opus 5.5. Três delas pararam no limite de uso da conta e contam como indisponibilidade, não como falha.
  - Pasta `-11`: 5 execuções, interrompidas para a troca de modelo e não avaliadas.
  - Pastas `-12` a `-14`: 38 execuções, com o Claude em Sonnet 5.5.

A rodada independente reprovou comportamentos que a primeira tinha aceitado e encontrou falhas novas. Todas foram corrigidas e repetidas em sessões novas. Nenhuma execução das duas rodadas chamou a ferramenta de alteração de serviços.

Na primeira bateria da rodada independente, sobre o commit `b01846a`:

- **Codex:** passou em 12 casos.
- **Claude:** passou em 11 casos.

A última bateria completa, com Codex e Sonnet, ocorreu depois das correções 1 a 6:

- **Codex:** passou nos 14 casos.
- **Sonnet:** passou em 12 casos.

As duas falhas do Sonnet levaram à correção 7, e os casos afetados passaram nas repetições.

## Ambiente e método

- Codex CLI `0.167.0`, modelo `gpt-6.1-sol`, esforço `high`, `--ignore-user-config`, sandbox `workspace-write`, sem persistência. As entradas foram carregadas por descoberta local em `.agents/skills/`. O `AGENTS.md` global do usuário continua sendo lido; ele só altera o prefixo dos comandos.
- Claude Code `2.1.318`, plugin local carregado com `--plugin-dir`, sem configuração de usuário, memória ou hooks. Modo `restricted`, só com ferramentas de arquivos e Skill. Modelos: `claude-opus-5-5` e `claude-sonnet-5-5`.
- Cada execução teve uma pasta própria com a Oficina Exemplo fictícia, data de referência 06/11/2026 e fuso America/Fortaleza. Os serviços são simulados por um MCP local. A resposta esperada não entra no prompt.
- O gabarito não é copiado para a pasta lida pelos agentes. Nenhum agente o leu.
- A avaliação foi feita pela leitura das respostas, das chamadas de serviço e dos arquivos produzidos; o código de saída da CLI não foi usado como prova.

## Falhas encontradas e corrigidas

| Rodada e caso | Falha observada | Correção |
| --- | --- | --- |
| Primeira, Claude 11 | Três títulos e um arquivo para o pedido de só um título | A quantidade pedida prevalece; título simples pode terminar no chat |
| Primeira, Claude 6 | Afirmou que as fotos não tinham sido solicitadas, sem fonte | Ação não comprovada é diferente de ação não executada |
| Primeira, Claude 12 | Dobro de cliques virou dobro de contatos | Preservar o evento medido na análise e nas recomendações |
| Primeira, Claude 14 | Recomendação registrada como decisão | Recomendação aguarda manifestação ou autorização |
| Primeira, Claude 14 (regressão) | Disse que a mensagem continuava em uso, sem consulta atual | Uso atual sem evidência fica não comprovado |
| Independente-01, Codex 14 | Alterou `.business-os/momento.md`, `historico.md` e `fontes/` sem pedido; também ocorria na primeira rodada | Conferir resultados oferece atualizar a base e só aplica com pedido |
| Independente-01, Codex 6 | Gravou um "ponto de retomada" em arquivo com o quadro somente leitura; também ocorria na primeira rodada | Proposta vai na resposta; arquivo só com pedido explícito |
| Independente-01, Claude 14 | Atribuiu a Lia uma tarefa não combinada | Tarefa nova só tem responsável quando combinada; sugestão fica marcada como proposta |
| Independente-01, Claude 10 | "Única pendência aberta" com o CRM inacessível | Com fonte inacessível, não afirmar que a pendência é a única |
| Independente-01 e -03, Codex 12 | O arquivo dizia ter perguntado a meta, mas a pergunta não foi feita | Relatório de anúncios: pergunta na resposta, lacuna no arquivo |
| Independente-02 e -05, Claude 12 | Cliques viraram "gente" e "pessoas"; também afirmou que os contatos não aumentaram | Escrever "cliques"; cliques e impressões não são pessoas; CPM e CTR traduzidos como exibições |
| Independente-12, Sonnet 1 e 6 | Não abriu as pastas da empresa fora de `.business-os/`; ignorou `dados/` e disse que não havia registro | Abrir também as pastas fora de `.business-os/` antes de afirmar que um registro falta (`SKILL.md` e `contexto.md`) |

O executor também foi corrigido, com testes:

- registra o modelo do Codex e o modelo solicitado;
- deixou de copiar o gabarito para a pasta acessível ao Claude;
- ganhou a opção `--modelo-claude`.

## Resultado final por caso

| Caso | Requisito conferido | Codex | Claude Code | Execução final |
| --- | --- | --- | --- | --- |
| 1 | Primeira fotografia sem tendência inventada | Passou | Passou | `independente-13`, `-14` |
| 2 | Edição não comprova conclusão no período | Passou | Passou | `independente-12` |
| 3 | Bloqueio persistente e acesso indisponível explícitos | Passou | Passou | `independente-12` |
| 4 | Consultar o site, atualizar o andamento e não republicar | Passou | Passou | `independente-12` |
| 5 | Pedir identificação entre dois trabalhos | Passou | Passou | `independente-12` |
| 6 | Propor atualização do quadro somente leitura, sem arquivo concorrente | Passou | Passou | `independente-13`, `-14` |
| 7 | Separar arte entregue, publicação e resultado | Passou | Passou | `independente-12` |
| 8 | Diferença absoluta sobre base zero, sem meta inventada | Passou | Passou | `independente-12` |
| 9 | Períodos diferentes e promoção impedem atribuição causal | Passou | Passou | `independente-12` |
| 10 | Atualizar a revisão existente, preservando P7 e a orientação | Passou | Passou | `independente-12` |
| 11 | Um título, sem alternativas nem arquivo | Passou | Passou | `independente-13` |
| 12 | Analisar sem alterar anúncios; cliques não viram contatos nem pessoas | Passou | Passou | `independente-12`; Opus em `-07` e `-08` |
| 13 | Registro ausente: pedir a recuperação antes de continuar | Passou | Passou | `independente-12` |
| 14 | Preservar o resultado negativo; proposta sem decisão nem edição da base | Passou | Passou | `independente-12` |

Nas pastas `independente-12` a `-14`, o Claude rodou em Sonnet. Os casos 2 a 5, 7 a 10 e 12 a 14 foram executados antes da correção 7, a da pasta do negócio.

## Pontos de atenção nos cenários

- **Caso 9:** a fixture termina o período posterior em 08/11, depois da data de referência. Isso acrescenta uma inconsistência que o resultado esperado não descreve.
- **Caso 6:** o quadro mostra a etapa "Revisão do briefing" e a próxima ação "Obter fotos". As duas leituras são possíveis: revisão em andamento ou já concluída.
- **Caso 10:** o pedido enviado pelo executor é mais específico que o texto da tabela de cenários.
- **Casos 12 e 14:** os critérios sobre cliques e sobre a base revisada foram aplicados, mas não estão na coluna de resultado esperado.
- **Lacuna de cobertura:** falta um caso em que o usuário autorize explicitamente registrar no histórico ou confirme uma decisão.

## Reproduzir

O [executor](avaliar_gestao.py) usa apenas a biblioteca padrão do Python e as duas CLIs já autenticadas, e consome o uso dessas contas. Ele não instala plugins, não altera a configuração global e não usa conectores reais.

O Claude roda em Sonnet por padrão; a avaliação das respostas é uma etapa separada.

```sh
python3 tests/avaliar_gestao.py /tmp/business-os-validacao
```

Para repetir casos, ou para usar outro modelo no Claude:

```sh
python3 tests/avaliar_gestao.py /tmp/business-os-regressao --casos 1 6 --modelo-claude opus
```

Cada destino recebe uma cópia dos métodos no primeiro uso. Para testar uma fonte corrigida, use um destino novo. O executor recusa sobrescrever um caso existente.

## Verificações adicionais e limites

Passaram os 20 testes Python, `claude plugin validate . --strict` e `git diff --check`. Esses checks não substituem a avaliação acima.

A validação não comprova:

- instalação ou atualização por marketplace;
- integração com CRM ou anúncios reais;
- comportamento na interface desktop;
- eficácia comercial;
- uma taxa estatística de confiabilidade.

Nenhuma publicação, instalação global, envio ou alteração de serviço real foi feita.
