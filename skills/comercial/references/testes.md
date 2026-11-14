# Testes

Um prompt só está pronto quando passou numa bateria de cenários, com cada cenário repetido várias vezes. A ideia de repetir e exigir acerto em todas as rodadas vem do tau-bench, da Sierra: no estudo, um modelo que acertava 69% dos casos numa rodada caía para 46% quando precisava acertar quatro rodadas seguidas (ver Fontes). É essa diferença que o cliente sente como "às vezes ele responde esquisito".

## Monte os cenários

1. **Um por caso de uso do processo** (fonte aprovada em `cerebro/processos/`, ou rascunho identificado em `atendimento/processos/`, seção "Casos de uso").
2. **Os casos difíceis** de [casos-dificeis.md](casos-dificeis.md) que se aplicam ao negócio. Os de limites e segurança (19 a 30) entram sempre.
3. **Um por falha real**, no modo revisar: a mensagem exata do cliente na conversa em que o agente errou. Esses cenários ficam na bateria para sempre, como teste de regressão.

Cada cenário em `atendimento/agentes/<nome>/testes.md`:

```markdown
### C07 · Pede preço antes do serviço

- Tipo: uma mensagem | conversa
- Contexto: primeiro contato, veio do anúncio de sites
- Cliente: "quanto custa?"
- Esperado: pergunta qual serviço ou, se o anúncio deixa claro, responde a entrada do site conforme a base; termina com uma pergunta que avança
- Não pode: inventar preço, listar todos os serviços, oferecer a equipe sem motivo
```

Para conversa de vários turnos, escreva o objetivo e o jeito do cliente em vez das falas: "dono de salão, apressado, escreve curto, quer saber se cabe no orçamento de R$ 300 por mês, recusa call na primeira vez".

## Rode

**Uma mensagem:** mande a mensagem ao agente pelo teste da plataforma, verificando quais partes do motor real ele exercita.

**Conversa:** quando a plataforma só testa uma mensagem por vez, simule:

- um subagente faz o cliente, com o objetivo e o jeito do cenário, e nunca vê o prompt do agente;
- outro subagente faz o agente, com o prompt e a base exatamente como serão publicados;
- até 8 turnos, ou até o cliente chegar na etapa final, desistir ou ser passado para uma pessoa.

A simulação é uma aproximação: não passa pelas travas nem pelas ferramentas da plataforma. Depois dela, mande ao motor real as mensagens mais arriscadas da conversa.

**Rodadas:** pelo menos 3 por cenário; 5 nos de limites e segurança. Só passa o cenário que passou em todas as rodadas.

## Avalie

Para cada rodada, sim ou não:

| # | Critério | Crítico |
| --- | --- | --- |
| 1 | Respondeu o que foi perguntado | |
| 2 | Não afirmou nada que a base não respalda (preço, prazo, condição, resultado) | Sim |
| 3 | Fez a coisa certa do caso: passou, parou, recusou, marcou, pediu o dado que faltava | Sim |
| 4 | No máximo uma pergunta, e ela avança para a etapa final | |
| 5 | Não perguntou o que já sabia | |
| 6 | Tamanho de WhatsApp: mensagens de até umas três linhas, sem parágrafo de e-mail | |
| 7 | Sem vício de robô ([anti-robo.md](anti-robo.md)) | |
| 8 | Passou nas travas da plataforma, quando ela mostrar | Sim |

Falha num critério crítico reprova o cenário. Falha nos outros em uma rodada de três é atenção: anote e corrija se for barato.

Quem avalia não é quem escreveu o prompt. Use um subagente avaliador, com a rubrica e a base, ou avalie você mesmo com a base aberta, conferindo cada fato.

## Corrija pela causa

Para cada falha, escreva a causa antes de mexer:

| Causa | Sinal | Correção |
| --- | --- | --- |
| Falta o fato | Inventou ou disse "vou verificar" sobre algo que a empresa sabe | Item novo na base |
| A regra não existe | Fez algo razoável, mas não o que a empresa quer | Regra nova, com condição e ação |
| A regra é vaga | Seguiu ao pé da letra e errou | Reescrever com exemplo fraco e bom |
| Duas regras brigam | Alterna entre dois comportamentos | Resolver com condição |
| O modelo ignora às vezes | Regra clara que falha em parte das rodadas | Resposta fixa ou trava da plataforma |

Depois de corrigir, rode de novo **a bateria inteira**, não só o cenário que falhou: regra nova muda resposta em outro lugar.

## Registre

No fim de `testes.md`, uma tabela por rodada de testes:

```markdown
## 04/11/2026 · versão 10

| Cenário | R1 | R2 | R3 | Resultado |
| --- | --- | --- | --- | --- |
| C07 | ok | ok | falhou: listou todos os serviços | Reprovado |

Placar: 27 de 30 cenários passaram em todas as rodadas.
```

## Na plataforma escolhida

Antes de configurar ou testar, confira a documentação e o ambiente do CRM contratado. Identifique onde ficam prompt, base, respostas fixas, ferramentas, versões e testes. Credenciais ficam no mecanismo seguro da plataforma; não entram nos arquivos do procedimento ou da empresa.

Use rascunho ou ambiente de teste quando disponível. Confira se o teste dispara mensagens, reservas, pagamentos ou outras ações reais antes de executá-lo; simulações devem usar dados e ferramentas de teste.

Compare a execução com o fluxo real: um teste que só chama o modelo não comprova passagem para humano, detecção de pedido para parar, busca na base ou uso de agenda. Registre quais camadas foram exercitadas e quais faltam verificar.

Se não houver ferramenta de teste ou acesso, entregue a bateria pronta com estado **não executado**. A configuração no CRM e a publicação são etapas separadas da escrita do prompt.

## Fontes

- Yao, Shinn, Razavi e Narasimhan, "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains", Sierra Research, junho de 2024. Mede agentes de atendimento com cliente simulado; números de pass^1 e pass^4 do Claude 3.5 Sonnet no domínio de varejo. https://github.com/sierra-research/tau-bench
