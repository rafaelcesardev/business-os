# Modelos de imagem estática

Estruturas de anúncio em imagem (feed 4:5, Stories 9:16) pra negócio local e de serviço. O modelo dá a forma; o conteúdo sai do contexto do negócio. Usado pelo [anuncio-meta](anuncio-meta.md) nos criativos em imagem e pelo [carrossel](carrossel.md) no post único.

## Como usar

- **Um modelo diferente por criativo.** Variar o modelo é variar o ângulo: o vencedor raramente é o que se escolheria de olho.
- **Todo conceito diz de onde veio.** Frase de cliente das **Frases reais** (`publico.md`), prova das **Provas** (`mensagem.md`), dor, objeção. Sem fonte, não entra.
- **Pra quem é** indica o ponto de partida, não uma regra: há modelos que costumam abrir conversa com gente nova, e outros que convertem quem já conhece o negócio (remarketing, seguidores). Testar e registrar em `historico.md` o que funcionou.

## Os modelos

| Modelo | Como é | Pra quem | O conteúdo sai de | Cuidado |
| --- | --- | --- | --- | --- |
| **Recado do dono** | Bilhete curto ou texto simples assinado pelo dono, com foto real dele. Fala por que faz e pra quem | Gente nova | Posicionamento (`mensagem.md`), história do negócio (`negocio.md`) | Foto real, nunca banco de imagem. Tom de conversa, não de propaganda |
| **História de origem** | Foto do dono ou da equipe e um texto mais longo: o momento em que o negócio começou ou mudou | Gente nova | `negocio.md` | Um momento específico, não "há 10 anos no mercado" |
| **Frase de impacto** | Uma frase ocupando a maior parte da peça, logo pequeno | Os dois | A dor ou a promessa mais forte, de preferência uma **Frase real** | Só funciona se a frase for muito boa. Passar pelo [revisar-copy](revisar-copy.md) |
| **Problema e solução** | A dor em cima, nas palavras do cliente; o serviço como resposta embaixo | Gente nova | **Dores** e **Frases reais** (`publico.md`) | A dor literal, não parafraseada em marketês |
| **Pergunta frequente** | A objeção como pergunta, em destaque, e a resposta direta embaixo | Quem já conhece | **Objeções** (`publico.md`) | A pergunta do jeito que o cliente pergunta ("Dói?", "Parcela?") |
| **Jeito antigo e jeito novo** | Duas colunas: o jeito comum (apagado) e o do negócio (em cor), 3 a 5 linhas | Quem já conhece | Concorrência e diferencial (`mensagem.md`) | Comparar com o jeito comum, nunca com concorrente pelo nome |
| **Antes e depois** | Imagem dividida com seta: o estado de antes e o de depois | Quem já conhece | **Provas** (`mensagem.md`) | Proibido ou restrito em saúde e estética por vários conselhos de classe: conferir os **Limites** antes. Fora do corpo (agenda, fachada, processo) costuma ser liberado |
| **Número em destaque** | Um número grande e uma linha de contexto | Os dois | **Provas** (`mensagem.md`) | Só número com fonte. Sem prova, outro modelo |
| **Avaliação real** | Print de uma avaliação do Google ou do Instagram, literal | Quem já conhece | **Provas** (`mensagem.md`) | Só a avaliação que surpreende (específica, que ninguém inventaria). "Ótimo atendimento, recomendo" não vale o espaço. Sem mudar uma palavra |
| **Vitrine** | Grade com os produtos, pratos ou serviços, uma imagem limpa | Gente nova | `negocio.md` e `assets/` | Pra negócio com vários itens. Fotos reais do que vende |
| **Setas no que importa** | Foto do produto, do espaço ou do resultado com 3 a 5 rótulos curtos apontando o que é diferente | Os dois | Diferencial (`mensagem.md`), `negocio.md` | Rótulo é fato visível, não adjetivo |
| **Explica num quadro** | Uma imagem que ensina algo verdadeiro: como funciona a primeira consulta, os 3 passos do serviço | Os dois | Como funciona (`negocio.md`), perguntas frequentes | Tem que parecer conteúdo, não anúncio. Uma ideia só |
| **Bilhete** | Post-it, anotação à mão ou texto simples sobre uma foto, com cara de improviso | Quem já conhece | A oferta (`negocio.md`, `momento.md`) | Pra promoção com prazo real. Fora de promoção, perde a força |

Ficam de fora: logos de imprensa ("visto em", exige autorização de cada veículo), lista numerada ("5 motivos pra…", cansou) e comparação citando concorrente pelo nome.

## A frase é o visual

Nos modelos de texto (frase de impacto, número em destaque, pergunta frequente, problema e solução):

- **Uma frase domina.** Fonte grossa e legível, quebras de linha que mantêm as palavras juntas. Logo e nome do negócio ficam pequenos.
- **Fundo que faz a frase saltar:** escuro com texto claro, ou a cor de destaque de `marca.md` com texto em contraste. Sem foto de banco disputando com a frase.
- **A frase não legenda a imagem.** Se a foto mostra a recepção cheia, a frase não diz "recepção cheia": diz o que a foto não mostra ("Ninguém aqui esperou mais de 10 minutos", com prova).
- **Conferir no tamanho do celular.** A peça precisa ser lida inteira, sem zoom, no tamanho em que aparece no feed. Se não der, encurtar a frase ou trocar o layout; nunca diminuir a letra da informação que precisa estar ali.

## Entrega de cada conceito

```markdown
### Criativo <letra> — <modelo>

**Pra quem:** gente nova | quem já conhece
**Frase principal:** <a frase da peça>
**Apoio:** <linha de contexto, se o modelo usa>
**Visual:** <o que aparece, cores de marca.md, fotos de assets/ ou a gerar>
**Fonte:** <Frase real, Prova ou Objeção de onde veio, com o arquivo>
```

*Modelos adaptados do static-ad-templates e do awareness-headlines de [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), reescritos pra negócio local.*

Post único e capa de reels são o formato próprio da imagem conceitual chamativa, em par com a frase (ver [escrever-copy](escrever-copy.md#3-escrever)). Em carrossel, essa intensidade fica na capa e no CTA; o meio é focado no texto ([carrossel](carrossel.md)).
