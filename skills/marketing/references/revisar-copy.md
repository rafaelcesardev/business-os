# Revisão de copy

Para localizar a empresa e usar contexto local ou fornecido por um plugin, siga [contexto do negócio](../../business-os/contexto.md).

Para criar a peça a partir de um briefing ou pesquisar referências e ganchos, use [escrever-copy](escrever-copy.md). Este procedimento preserva o foco na revisão de um texto existente.

Pega um texto pronto (colado pelo usuário ou saído de outro procedimento) e devolve a versão que vende melhor, com o motivo de cada mudança. Não reescreve por gosto: cada mudança precisa de uma razão que caiba numa linha.

## Contexto do negócio

Procurar a pasta `.business-os/` na pasta atual e, se não estiver ali, nas pastas acima. A pasta que contém `.business-os/` é a **pasta do negócio**: caminhos de saída como `marketing/...` são relativos a ela (sem `.business-os/`, à pasta atual). Ler `.business-os/RESUMO.md` primeiro e depois os arquivos listados em Dependências.

Se não houver `.business-os/` nem contexto fornecido por um plugin da empresa, avisar que o `business-os` monta o contexto e seguir com o que o usuário informar. Campo vazio é lacuna: perguntar, não inventar. Nada marcado `(hipótese)` ou `(a confirmar)` vira afirmação pública.

## Dependências

- **Público:** `.business-os/publico.md` (quanto já sabe, dores, objeções, frases reais)
- **Voz, provas, limites e concorrência:** `.business-os/mensagem.md`
- **Oferta:** `.business-os/negocio.md`
- **Padrões de texto de IA:** [anti-ia.md](anti-ia.md)
- **Outputs:** texto colado no chat volta no chat. Arquivo revisado é salvo ao lado do original como `<nome>-revisado.md`, sem apagar o original.

---

## Workflow

### Passo 1 — Diagnóstico

Antes de mexer, decidir qual é a situação e dizer em uma linha, com a evidência:

| Situação | O que chegou | O que fazer |
| --- | --- | --- |
| **A. Genérico** | Texto que serviria pra qualquer concorrente, ou pedido de uma linha | Reconstruir a partir do contexto. Liberdade no ângulo, nenhuma nos fatos |
| **B. Tem voz** | Texto com opinião, jeito de falar ou ângulo próprio, mesmo mal acabado | Preservar. Manter o argumento e as palavras do autor; consertar o que esconde a ideia |
| **C. Ajuste pontual** | "Só melhora o título", "encurta esse parágrafo" | Mexer só no que foi pedido e no mínimo em volta pra encaixar. O resto volta igual |

Exemplo: "B: o texto fala como a dona da clínica, usa 'a gente' e 'sem enrolação'; vou manter isso e trocar o título."

Em B e C, o texto do usuário é a prova do gosto dele: a palavra que ele usa fica (não trocar "coisa" por "solução"), onde ele gastou mais palavras é a prioridade, e seção que ele não pôs não entra. No ajuste pontual, aplique as passadas somente ao trecho solicitado e ao mínimo necessário para encaixá-lo; o restante aprovado volta igual.

### Passo 2 — Pra quem e contra quem

Duas perguntas definem que tipo de título e gancho funciona. Responder com o contexto; se não der, marcar como `(hipótese)` e oferecer duas versões.

Em um ajuste pontual, use o contexto disponível sem abrir pesquisa ou entrevista de concorrência como etapa obrigatória. Pergunte somente se faltar um fato necessário para o trecho pedido.

**Quanto o público já sabe** (campo **Quanto já sabe** de `publico.md`; se estiver vazio, deduzir de **O que acontece antes de comprar**):

| Nível | A pessoa… | O título… | Exemplo de estrutura (inventado) |
| --- | --- | --- | --- |
| Não sabe do problema | vive a situação mas não deu nome | descreve a cena que ela vive | "Mais um domingo respondendo cliente no WhatsApp." |
| Sabe do problema | sente a dor, não sabe que tem saída | nomeia a dor e aponta a saída | "Dor no joelho ao subir escada tem tratamento sem cirurgia." |
| Conhece as soluções | está comparando caminhos | mostra como esse jeito é diferente | "Alinhador ou aparelho fixo: o que muda no seu dia a dia." |
| Conhece o negócio | já segue, já perguntou o preço | tira a objeção que falta, com prova | "Parcelamos em 10x e a primeira avaliação é sem custo." |
| Pronto pra comprar | só precisa do empurrão | oferta e ação, direto | "Últimos 4 horários de dezembro. Chama no WhatsApp." |

Anúncio pra gente nova costuma estar nos dois primeiros níveis; remarketing e post pra quem já segue, nos últimos. O erro mais comum é falar de preço e diferencial com quem ainda nem reconhece o problema.

**Quantos concorrentes já prometem a mesma coisa** (coluna **O que promete** da tabela **Concorrência** de `mensagem.md`; vazia, abrir o site dos concorrentes listados ou perguntar):

- **Nenhum ou um:** prometer direto. Ser claro ganha.
- **De dois a quatro:** a promessa sozinha virou papel de parede. Mostrar **como** o resultado acontece (o método, o passo a passo, o que é feito diferente).
- **Cinco ou mais:** parar de prometer. Mudar o enquadramento ou falar com a identidade de quem compra ("Pra quem já tentou três dietas e desistiu de todas").

### Passo 3 — Três perguntas por frase

Passar cada frase que fica (título, gancho, subtítulo, frase de cada seção, CTA) por três perguntas:

1. **Dá pra ver?** Uma cena, um objeto, um número ganha de uma ideia abstrata.
2. **Dá pra provar se é verdade ou mentira?** Afirmação verificável é argumento; "atendimento diferenciado" é enfeite.
3. **Um concorrente assinaria igual?** Se sim, a frase não diz nada sobre este negócio.

Passou nas três, fica. Em duas, afiar a que falhou. Em uma ou nenhuma, reescrever a partir dos fatos do contexto ou marcar a lacuna.

Ritmo: a maioria das frases é simples e direta. A peça tem um ou dois momentos de impacto, geralmente o título e mais um. Quando toda frase tenta impressionar, nenhuma impressiona.

### Passo 4 — Passadas

Uma passada por vez, nesta ordem. Cada uma procura um tipo de problema só.

1. **Clareza.** Quem lê entende de primeira? Frase com duas ideias vira duas frases. Jargão do setor vira a palavra do público (**Frases reais**). O principal vem primeiro.
2. **E daí?** Toda característica responde "e daí pra mim?". Perguntar "e daí?" até chegar em algo que a pessoa sente ou no bolso dela: "agenda online" → "marca sem ligar" → "marca às 23h, deitada, quando lembrou". Quando a dor tem tamanho, mostrar a conta ("3 horas por dia respondendo as mesmas perguntas").
3. **Prova.** Toda promessa amarrada a uma **Prova** de `mensagem.md`. Sem prova, não escrever a promessa nem sumir com ela em silêncio: trocar pela versão mais modesta que se sustenta e marcar `[FALTA: <prova> — libera "<promessa>"]`, dizendo o que destrava (print de avaliações, número do sistema, autorização de uso de depoimento).
4. **Risco zero.** Perto do botão, a pessoa sabe o que acontece depois de clicar ("cai no WhatsApp da recepção, resposta em até 1 hora")? A objeção mais forte de `publico.md` foi respondida antes do pedido? O tamanho do pedido combina com o nível do Passo 2 ("Ver horários" pede menos que "Agendar agora")?
5. **Texto de IA.** Rodar a [anti-ia.md](anti-ia.md) inteira, por último, porque as outras passadas reescrevem frases.

Antes de entregar, **teste do deixar quieto:** olhar cada mudança e perguntar se ficou melhor ou só diferente. Desfazer a que não tem motivo. Vale mais em B e C.

### Passo 5 — Entrega

```markdown
**Diagnóstico:** <A, B ou C> — <evidência em uma linha>
**Público:** <nível de consciência> · **Concorrência:** <promessa nova, comum ou saturada>

<texto revisado, completo>

**O que mudou**
- <mudança> — <motivo>

**Lacunas**
- [FALTA: <prova> — libera "<promessa>"]
```

Pedido de título ou gancho: entregar 3 opções de **tipos diferentes** (cena, dor + saída, número, pergunta que o público digita no Google, prova primeiro), não três jeitos de dizer a mesma coisa, e indicar a recomendada.

### Chamada por outro procedimento (modo rápido)

Quando [anuncio-meta](anuncio-meta.md), [roteiro-reels](roteiro-reels.md), [carrossel](carrossel.md), [planejar-site](planejar-site.md) ou outro procedimento pedir a revisão do próprio texto: rodar os Passos 3 e 4 sem o relatório completo e voltar o texto pronto para o procedimento que chamou. Só listar o que mudou se for algo que o usuário precisa saber (promessa cortada por falta de prova, lacuna nova).

---

## Regras

- Nunca inventar número, depoimento, caso, prazo ou escassez pra deixar o texto mais forte. Frase de cliente tirada de `publico.md` serve de vocabulário; só vira depoimento publicado se estiver em **Provas**.
- Nada que cruze os **Limites** de `mensagem.md` (conselhos de classe, Anvisa, CDC, políticas da Meta e do Google), mesmo que soe melhor.
- Em B e C, a voz do autor ganha da regra geral. A [anti-ia.md](anti-ia.md) cede às **Frases reais** e à Voz.
- Respeitar o formato de origem: limite de caracteres do anúncio, duração do vídeo, tamanho do slide.

*Ideias adaptadas e reescritas em português a partir de [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (copywriting e copy-editing, MIT) e [avectats7/copy-that-sells](https://github.com/avectats7/copy-that-sells) (MIT).*
