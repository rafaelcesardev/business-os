# Regras do prompt

Como organizar o prompt de um atendente e como escrever cada regra. A estrutura foi extraída de um agente de atendimento revisado em 04/11/2026; a forma de escrever as regras segue o guia de instruções do Intercom Fin e as ideias de regras por situação e respostas pré-aprovadas do Parlant (ver Fontes).

## Estrutura

Seções curtas, com título em maiúsculas, nesta ordem. Remova as que não se aplicam.

| Seção | O que diz |
| --- | --- |
| IDENTIDADE E PAPEL | Nome do agente, empresa, o que ela oferece em uma frase, o trabalho do agente (até onde ele vai e onde passa) e quem cuida de cada assunto |
| COMO ESCREVER | Tamanho, uma pergunta por mensagem, o que não fazer (espelhar, elogiar, resumir), exemplos fraco e bom |
| QUALIFICAÇÃO | O mínimo que precisa saber antes do próximo passo, e que informações já recebidas contam como resposta |
| Uma seção por serviço ou assunto | A pergunta principal, o que consultar na base, o que nunca prometer, para onde levar |
| PRÓXIMO PASSO | Como propor a etapa final (agenda, horários, confirmação) e o que fazer quando a pessoa recusa |
| PASSAGEM PARA UMA PESSOA | Os sinais, o que dizer e o que registrar para quem assume |
| CASOS ESPECIAIS | Quem não tem perfil, quem já é cliente, quem procura outra coisa (por exemplo, atendimento de saúde numa empresa que não é clínica) |
| REGISTRO E LIMITES | O que registrar no sistema, de onde vêm preços e condições, o que nunca prometer ou pedir |
| RETORNOS | Quando combinar um retorno, fuso e datas |

Quando o prompt crescer, procure regras repetidas e fatos que deveriam estar na base. O tamanho adequado depende da tarefa e das capacidades da plataforma.

## Como escrever cada regra

### Uma regra, um objetivo

Fraco: "Seja cordial, pergunte o serviço e, se a pessoa ficar irritada, passe para a equipe."
Bom: três regras separadas, uma para tom, uma para a pergunta e uma para a passagem.

**Por quê:** regra que mistura objetivos é seguida pela metade, e fica impossível saber qual parte falhou.

### Condição e ação

Escreva quando a regra vale e o que fazer: "Se a pessoa pedir o preço antes de dizer o serviço, pergunte qual serviço ela quer."

**Por quê:** a regra sem condição é aplicada em toda mensagem, inclusive onde não cabe.

### Fale com o agente

Fraco: "O assistente deve evitar repetir o que o cliente disse."
Bom: "Não repita nem confirme por paráfrase o que a pessoa acabou de dizer."

### Tom por exemplo

Fraco: "Tom simpático e profissional."
Bom: o que fazer, o que não fazer e um par de exemplos:

> - A pessoa informa que tem um salão e quer anúncios: pergunte o dado que falta, como "Em qual cidade fica o salão?". Não diga "Que bom saber do seu interesse em anúncios para o seu salão".

**Por quê:** adjetivo cada modelo interpreta de um jeito. Exemplo mostra.

### A pergunta antes da resposta

Para cada tema em que a resposta depende de um dado, diga qual pergunta fazer primeiro: o serviço antes do preço, a cidade antes da disponibilidade, o tipo de site antes do prazo. E diga o que **não** presumir ("Não presuma clínica ou pacientes").

### O que já veio conta

"Não pergunte de novo o que a pessoa já informou na mensagem, no formulário ou no cadastro." Sem isso, o agente segue a ordem da qualificação como ficha.

### Passagem situacional

Liste os sinais concretos (pediu uma pessoa, irritação, mesma dúvida duas vezes sem resposta, assunto contratual, pedido que a base não cobre). Não mande oferecer a equipe em toda resposta: isso derruba a resolução e soa como fuga.

### Uma regra para quem insiste fora do escopo

"Se a pessoa insistir num assunto fora do que a empresa faz depois de você explicar, passe para a equipe." Sem isso, o agente discute.

### Exemplos marcados e variados

Frases de exemplo viram bordão: o modelo repete a mesma abertura em toda conversa. Marque como exemplo, dê duas ou três variações, ou descreva o efeito em vez de dar a frase. Se aparecer bordão nos testes, tire o exemplo que o causou.

### Porquê curto quando a regra parece estranha

"Não reserve horário só porque pediram uma mensagem depois: retorno por mensagem não é reunião." O porquê ajuda o modelo a aplicar a regra em casos que ela não lista.

### Ênfase com moderação

MAIÚSCULAS e "IMPORTANTE" só nas duas ou três regras que não podem falhar. Se tudo é importante, nada é. Regra que falha mesmo com ênfase vira resposta fixa ou trava da plataforma.

### Sem regra encadeada

Não escreva "depois de aplicar a regra anterior, faça...". Cada regra precisa funcionar sozinha.

### Sem contradição

Antes de entregar, leia procurando pares que brigam: "sempre proponha a call" e "não insista na call"; "responda curto" e "explique todas as condições". Resolva com condição ("Proponha a call quando houver base; se a pessoa recusar, não repita o convite").

## Fatos

- Nenhum preço, prazo ou condição no prompt. O prompt diz **onde** consultar ("Consulte o material X antes de informar preços").
- Quando a base não cobre, o prompt diz o que fazer: "explique que será alinhado na conversa, sem inventar um número".
- Nome de concorrente, tecnologia de terceiros e custo interno ficam fora, salvo decisão explícita da empresa.

## Respostas fixas

Use texto fixo, ou um esqueleto rígido, onde a frase errada custa caro (ver passo 4 do procedimento). No prompt, a regra aponta o texto: "Quando a pessoa pedir uma pessoa, responda com o texto de passagem e registre o pedido." Na plataforma que tiver respostas prontas ou travas, prefira lá.

## Fontes

- Intercom, "Fin Guidance best practices and examples", consultado em 04/11/2026: https://fin.ai/help/en/articles/10644781-fin-guidance-best-practices-and-examples
- Parlant (emcie-co/parlant, Apache-2.0): regras ligadas a situações, roteiros de vários turnos e respostas pré-aprovadas. https://github.com/emcie-co/parlant
- OpenAI, "Realtime prompting guide": frases de exemplo viram bordão; peça variação. https://developers.openai.com/cookbook/examples/realtime_prompting_guide
