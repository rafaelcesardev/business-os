# Criar atendente com IA

Localize a empresa e siga as regras gerais do [Cérebro da empresa](../../cortex/contexto.md).

## Contexto e plataforma

Localize a pasta do negócio como na skill [cortex](../../cortex/SKILL.md). Leia o contexto antes de entrevistar novamente, inclusive instruções aprovadas em `cerebro/agentes/<nome>/`. Salve rascunhos, revisões e resultados de testes em `atendimento/agentes/<nome>/`, local e ignorado pelo Git. Após aprovação, promova as instruções e bases para o contexto conforme a [organização](../../cortex/organizacao.md), mantendo uma única fonte principal. Reutilize documentos legados em `agentes/` sem movê-los automaticamente. Pergunte o CRM ou plataforma contratada e confira suas capacidades e documentação antes de preparar campos ou ferramentas. O método não pressupõe um fornecedor. Sem acesso ao motor real, entregue as instruções, a base e os cenários, identificando o que não foi executado; nunca declare testes aprovados sem rodá-los.

Um atendente bom faz a pergunta certa, responde o que perguntaram, leva a conversa para a etapa final e não inventa. Quase toda resposta ruim vem de uma de cinco causas: falta o fato, a regra não existe, a regra é vaga, duas regras brigam, ou o modelo ignora a regra às vezes. Este procedimento acha a causa e corrige na camada certa, e só considera pronto o que passou nos testes.

## Três modos

- **Criar:** agente novo, a partir do processo mapeado.
- **Revisar:** agente no ar com respostas ruins. Parta das conversas reais.
- **Testar:** só rodar a bateria antes de publicar uma mudança.

Diga em uma linha qual modo vai seguir e por quê. Na dúvida entre criar e revisar, revise: reescrever do zero joga fora regras que nasceram de erro real.

## 1. Junte o material

- **O processo:** fonte aprovada em `cerebro/processos/`, ou rascunho identificado em `atendimento/processos/`, gerado pelo procedimento [mapear-processo-comercial](mapear-processo-comercial.md). Sem processo não há etapa final, e sem etapa final não há como saber se uma resposta avança. Se não existir, mapeie antes, ou pelo menos defina etapa final, serviços, regra de preço e gatilhos de passagem para uma pessoa.
- **A base de conhecimento:** preços, condições, perguntas frequentes.
- **O prompt atual**, se houver.
- **Conversas reais**, se houver. São a melhor fonte: mostram como os clientes escrevem e onde o agente erra. No modo revisar, são obrigatórias; peça à pessoa ou leia na plataforma.

## 2. Ponha cada coisa na camada certa

| Camada | O que guarda | Exemplo |
| --- | --- | --- |
| Prompt | Comportamento: papel, tom, o que perguntar, quando passar, limites | "Se perguntarem o preço da gestão de anúncios, explique que a verba é separada e ofereça a call." |
| Base de conhecimento | Fatos que mudam: preços, prazos, condições, o que está incluso | "O site de página única começa em R$ 500." |
| Respostas fixas | Momentos em que errar custa caro e o texto precisa sair sempre igual | Passagem para uma pessoa, recusa de atendimento de saúde, aviso de prazo |
| Travas da plataforma | O que precisa ser garantido, não pedido: promessa sem respaldo, horário de envio, pedido de parar | Validação de agenda, autorização de ferramentas e vetos antes do envio, quando a plataforma oferecer |

Fato no prompt envelhece e passa a contradizer a base. Regra de comportamento na base não é seguida, porque a base só entra quando a busca a encontra. Se uma regra importante continua falhando depois de bem escrita, ela vira resposta fixa ou trava, não mais uma frase em maiúsculas.

Uma pergunta por item na base, com a resposta inteira. Ao mudar uma condição, mude a base e confira se o prompt não repete a versão antiga.

## 3. Escreva o prompt

Siga [regras-do-prompt.md](regras-do-prompt.md): a estrutura das seções e como escrever cada regra. O essencial:

- Uma regra por objetivo, no formato condição e ação: "Se a pessoa pedir o preço antes de dizer o serviço, pergunte qual serviço."
- Fale direto com o agente ("Pergunte", "Não prometa"), não sobre ele.
- Tom definido por exemplo fraco e bom, nunca por adjetivo ("simpático e profissional" não diz nada).
- Para cada tema, a pergunta que o agente faz antes de responder.
- Passagem para uma pessoa em sinais claros, não oferecida em toda mensagem.
- Exemplos variados e marcados como exemplo, para não virarem bordão.

No modo revisar, mexa só no que os testes e as conversas mostraram. Para cada resposta ruim, escreva a causa (uma das cinco) e a correção, na camada certa.

## 4. Defina as respostas fixas

Liste os momentos críticos do processo e escreva o texto aprovado de cada um, ou um esqueleto rígido com as partes que variam. Em geral: passagem para uma pessoa, pedido para parar de receber mensagens, assunto que exige profissional (saúde, jurídico), cliente irritado, preço quando a regra é não falar, e confirmação de agendamento. Peça aprovação da pessoa para cada texto.

## 5. Teste

Siga [testes.md](testes.md). Monte os cenários a partir dos casos de uso do processo e dos [casos difíceis](casos-dificeis.md), rode cada um **pelo menos 3 vezes** e avalie com a rubrica. Um cenário só passa se passar em todas as rodadas: o problema "às vezes responde esquisito" só aparece na repetição.

Se a plataforma tiver teste no motor real, use. Prefira o teste do motor real da plataforma escolhida. Diferencie teste de mensagem, simulação de conversa e verificação de ferramentas e travas; uma aproximação não comprova o fluxo em produção.

## 6. Tire o jeito de robô

Revise as respostas dos testes e os exemplos do prompt com [anti-robo.md](anti-robo.md). Corrija no prompt a causa do vício, não só a frase.

## 7. Entregue

Salve na raiz do negócio:

- `atendimento/agentes/<nome>/prompt.md`: o prompt completo, pronto para colar.
- `atendimento/agentes/<nome>/respostas-fixas.md`: os textos aprovados e onde entra cada um.
- `atendimento/agentes/<nome>/testes.md`: cenários, rodadas, resultado e, no modo revisar, a causa e a correção de cada falha.
- Se a base mudou: `atendimento/agentes/<nome>/base.md`, uma pergunta por item.

Quando o responsável aprovar, promova `prompt.md`, `base.md` e `respostas-fixas.md` pertinentes para `cerebro/agentes/<nome>/`, registre a versão e atualize as referências. Cenários aprovados podem acompanhar esse contexto; conversas brutas, resultados de execução e logs continuam locais. Não substitua a versão aprovada por uma revisão ainda em teste e não confunda aprovação do texto com publicação no CRM.

Responda com o que mudou e por quê, o placar dos testes (quantos cenários passaram em todas as rodadas), o que falhou e ficou pendente, e o próximo passo. **Publicar é decisão da pessoa:** prepare a versão e o teste, e só publique quando ela disser. Depois de publicar, sugira acompanhar as primeiras conversas reais e voltar com o modo revisar.

## Limites

- Não invente fato para preencher o prompt ou a base. O que a empresa não decidiu vira pendência.
- Não copie regras de outro cliente sem conferir se valem para este negócio.
- Não cole token, senha ou dado de cliente em arquivo do procedimento ou na conversa.
