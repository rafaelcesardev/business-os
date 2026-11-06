# Usar o contexto em qualquer tarefa

Toda criação pra um negócio parte do que já se sabe sobre ele. Esta skill encontra a `.business-os/`, lê o que a tarefa pede e aplica esse contexto. Pedidos de divulgação e criação seguem [Marketing](../marketing/SKILL.md); vendas e atendimento seguem [Comercial](../comercial/SKILL.md). Este modo cobre consultas e decisões gerais, sem exigir que o usuário escolha um método.

## Workflow

### Passo 1 — Achar o contexto

Procurar `.business-os/` na pasta atual e nas pastas acima. A pasta que contém `.business-os/` é a **pasta do negócio**. Se o usuário citar um negócio que não é o dessa pasta, perguntar o caminho da pasta dele. Se não existir `.business-os/`, confira se o contexto foi fornecido pelo plugin da empresa conforme [contexto.md](contexto.md). Sem nenhuma fonte de contexto, ofereça o levantamento ([criar.md](criar.md)) ou siga com o que o usuário informou.

### Passo 2 — Ler o que a tarefa pede

`RESUMO.md` sempre, primeiro. Depois:

| Tarefa | Ler também |
| --- | --- |
| Conteúdo, roteiro, post, legenda | `publico.md`, `mensagem.md`, `marca.md` |
| Anúncio, campanha, oferta, promoção | `negocio.md`, `publico.md`, `mensagem.md`, `momento.md` |
| Site, landing page | todos |
| Sistema, automação, atendimento, CRM | `negocio.md` (operação), `publico.md`, limites em `mensagem.md` e processos existentes de atendimento |
| Proposta, planejamento, estratégia | `negocio.md`, `momento.md`, `historico.md` |
| Retomar trabalho, revisar prioridades ou conferir resultados | `momento.md`, a fonte de andamento indicada e as evidências do trabalho |
| Pergunta sobre o negócio | o arquivo do assunto |

Na dúvida, ler mais. Os arquivos são curtos e cada um evita uma suposição.

### Passo 3 — Lacunas

Listar o que a tarefa precisa e o contexto não tem. Perguntar só o que muda o resultado (sem o preço, uma landing page de venda não fecha; sem o tom, dá pra seguir com o padrão e ajustar depois). O resto segue marcado como lacuna na entrega. Nunca preencher com invenção plausível.

### Passo 4 — Criar com o contexto

- Escrever com as palavras do público: as **Frases reais** de `publico.md` valem mais que qualquer copy inventada.
- Toda promessa se apoia numa **Prova** de `mensagem.md`. Sem prova, a promessa fica mais modesta.
- **Limites** de `mensagem.md` são inegociáveis, mesmo que o usuário peça algo que os cruze: avisar antes.
- Alinhar ao **Momento**: o que serve ao objetivo atual vem primeiro.
- O que estiver marcado `(hipótese)` ou `(a confirmar)` não vira afirmação pública.
- Saídas vão para os locais registrados no negócio, separados da `.business-os/`; veja [organizacao.md](organizacao.md).
- O contexto também pode ser fornecido por um plugin da empresa. Use sua versão como referência e não edite o cache instalado para manter uma base paralela.

### Passo 5 — Devolver ao contexto

Ao terminar:
- Se houver continuidade ou acompanhamento solicitado, registre o estado na fonte de trabalho conforme [continuar trabalho](references/continuar-trabalho.md); para avaliar o efeito da entrega, use [conferir resultados](references/conferir-resultados.md). Não confunda andamento com contexto aprovado.
- Se a conversa trouxe informação nova sobre o negócio (decisão, preço, público, resultado), oferecer guardar seguindo [alimentar.md](alimentar.md).
- Se a entrega é relevante (site no ar, campanha lançada, proposta enviada), oferecer registrar em `historico.md`.
