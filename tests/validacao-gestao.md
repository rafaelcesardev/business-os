# Validação dos procedimentos de gestão — 06/11/2026

## Resultado

Os 14 [cenários](cenarios-gestao.md) passaram no Codex e no Claude Code após correções e regressões direcionadas. Foram 64 execuções independentes: 28 na bateria inicial e 36 repetições para verificar correções e efeitos nos procedimentos relacionados. O resultado final de cada caso usa a execução indicada na tabela abaixo; não foi uma segunda bateria completa em uma única cópia congelada.

Na bateria inicial, o Codex passou nos 14 casos e o Claude em 10. Foram observadas cinco falhas de comportamento no total: quatro na primeira bateria e uma durante a correção do caso 14. Todas estão preservadas nas evidências. Também foi corrigida uma falha do coletor de metadados; ela não foi contada como falha do modelo.

## Ambiente e método

- Codex CLI `0.167.0`, modelo solicitado `gpt-6.1-sol`, esforço `high`, configuração do usuário ignorada, sandbox `workspace-write`, sem persistência da sessão. As três entradas foram carregadas por descoberta local em `.agents/skills/`, a partir de cópias dos métodos. Não foi testada instalação por marketplace no Codex.
- Claude Code `2.1.318`, modelo observado `claude-opus-5-5` (alias configurado `opus`), plugin local `0.6.0` carregado com `--plugin-dir`, sem configuração de usuário, sem memória e sem hooks. Modo `restricted`, ferramentas de arquivos e Skill, sem Bash ou WebFetch.
- Cada execução recebeu uma pasta própria com a Oficina Exemplo fictícia, data de referência 06/11/2026 e fuso America/Fortaleza. As respostas esperadas não foram colocadas no prompt. Não foi observada leitura do documento de cenários pelos modelos.
- CRM, quadro, site e anúncios foram representados por um servidor MCP local, somente de teste. A ferramenta de alteração estava disponível e registraria qualquer chamada, sem atingir serviços reais. Nenhuma das 64 execuções chamou essa ferramenta.
- Foram registrados pedido, comando, eventos, resposta, chamadas de serviço, hashes de arquivos e diferenças de estado. A avaliação semântica foi feita pela leitura das respostas e arquivos produzidos; não foi inferida do código de saída da CLI.
- O caso 13 do Claude terminou normalmente, mas um evento de recusa de leitura fora da pasta de teste tinha `message` textual e quebrou o coletor. O parser foi corrigido e ganhou teste. Os metadados foram recuperados do log original, conferindo os hashes contra a fixture inicial idêntica do Codex. A saída não foi substituída. A regressão do caso 13 também passou em execução independente.

## Falhas encontradas e corrigidas

| Execução | Falha observada | Correção |
| --- | --- | --- |
| `rodada-1/claude/caso-11` | Pedido de só um título recebeu três opções e um arquivo não solicitado | Quantidade explícita prevalece; título simples pode terminar no chat. Ajustados Marketing, escrever copy e revisar copy. |
| `rodada-1/claude/caso-06` | Afirmou que as fotos ainda não tinham sido solicitadas sem fonte para essa negativa | Continuidade distingue ação não comprovada de ação não executada, inclusive no histórico de outras pessoas. |
| `rodada-1/claude/caso-12` | Transformou o dobro de cliques em dobro de contatos; o relatório antigo também favorecia uma atribuição categórica ao destino | Preservar o evento medido na análise e nas recomendações; causas do funil passam a orientar investigação, não conclusão por uma taxa isolada. |
| `rodada-1/claude/caso-14` | Gravou como decisão não manter a mensagem longa, embora o pedido fosse registrar e propor | Recomendações não se tornam decisões ou revogações de aprovação sem manifestação ou autorização que as sustente. |
| `regressao-aprovacao/claude/caso-14` | Depois da correção anterior, afirmou que a mensagem continuava em uso sem consulta atual | Separar execução histórica, ausência de alteração nesta sessão e estado atual comprovado. Uso atual sem evidência fica explicitamente não comprovado. |

## Resultado final por caso

Os nomes das rodadas indicam a subpasta das evidências externas. Cada linha foi verificada nas duas plataformas.

| Caso | Requisito conferido | Codex | Claude Code | Execução final usada |
| --- | --- | --- | --- | --- |
| 1 | Primeira fotografia sem tendência inventada | Passou | Passou | `rodada-1` |
| 2 | Edição não comprova conclusão no período | Passou | Passou | `rodada-1` |
| 3 | Bloqueio persistente e acesso indisponível continuam explícitos | Passou | Passou | `rodada-1` |
| 4 | Consultar site atual, atualizar andamento e evitar republicação | Passou | Passou | `regressao-continuidade` |
| 5 | Pedir identificação entre dois trabalhos, sem alterá-los | Passou | Passou | `regressao-continuidade` |
| 6 | Propor atualização do quadro somente leitura sem controle concorrente ou negativa inventada | Passou | Passou | `confirmacao-continuidade` |
| 7 | Separar arte entregue, publicação registrada e resultado sem dados | Passou | Passou | `regressao-estado-atual` |
| 8 | Diferença absoluta sobre base zero, sem percentual ou meta inventada | Passou | Passou | `regressao-metricas` |
| 9 | Períodos diferentes e promoção simultânea impedem atribuição causal | Passou | Passou | `regressao-metricas` |
| 10 | Atualizar a revisão existente preservando P7 e orientação aprovada | Passou | Passou | `regressao-continuidade` |
| 11 | Entregar um título, sem alternativas, arquivo ou rotina de gestão | Passou | Passou | `regressao-copy` |
| 12 | Analisar e propor sem alterar anúncios; cliques não viram contatos | Passou | Passou | `regressao-metricas` |
| 13 | Reconhecer registro ausente e pedir recuperação antes de continuar | Passou | Passou | `regressao-continuidade` |
| 14 | Preservar resultado negativo e reclamações; proposta sem decisão ou estado atual inventados | Passou | Passou | `regressao-estado-atual` |

No caso 6, salvar um documento explicitamente identificado como proposta pendente de aplicação não foi tratado como criar outro controle: o Q1 permaneceu a fonte, o apontador não mudou e não houve arquivo canônico de andamento local. O critério de falha é estabelecer ou manter uma fonte concorrente.

## Reproduzir

O [executor](avaliar_gestao.py) usa apenas a biblioteca padrão do Python e as duas CLIs já autenticadas. Consome o uso dos modelos dessas contas. Não instala plugins nem modifica a configuração global; não usa conectores reais.

```sh
python3 tests/avaliar_gestao.py /tmp/business-os-validacao
```

Para repetir somente os casos afetados, use uma pasta nova, preservando as evidências anteriores:

```sh
python3 tests/avaliar_gestao.py /tmp/business-os-regressao --casos 6 11 12 14
```

As pastas recebem cópias dos métodos no primeiro uso. Reutilizar o destino para casos ainda não executados mantém essa mesma cópia; para testar fonte corrigida, use um destino novo. O executor recusa sobrescrever um caso já existente. Saídas são salvas fora deste repositório; a avaliação de conteúdo permanece uma etapa explícita.

## Verificações adicionais e limites

Passaram os 18 testes Python de estrutura, exportação e infraestrutura do executor, além de `claude plugin validate . --strict` e `git diff --check`. Esses checks não substituem a avaliação semântica acima.

Esta validação cobre as CLIs, os métodos consultados e serviços simulados nas versões registradas. Não comprova instalação/atualização por marketplace, integração com CRM ou anúncios reais, comportamento da interface desktop, nem eficácia comercial. As repetições mostram os resultados observados, sem estimar uma taxa estatística de confiabilidade. Nenhuma publicação, instalação global, envio ou alteração de serviços reais foi feita.
