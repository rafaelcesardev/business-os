# Pipeline de conteúdo SEO + redes sociais

Para localizar a empresa e usar contexto local ou fornecido por um plugin, siga [contexto do negócio](../../business-os/contexto.md).

Skill orquestradora. Pega um tema → entrega artigo no blog + carrossel + 3 legendas (Insta, FB, LinkedIn), tudo conectado.

## Contexto do negócio

Procurar a pasta `.business-os/` na pasta atual e, se não estiver ali, nas pastas acima. A pasta que contém `.business-os/` é a **pasta do negócio**: caminhos de saída como `marketing/...` são relativos a ela (sem `.business-os/`, à pasta atual). Ler `.business-os/RESUMO.md` primeiro e depois os arquivos listados em Dependências.

Se não houver `.business-os/` nem contexto fornecido por um plugin da empresa, avisar que o `business-os` monta o contexto e seguir com o que o usuário informar. Campo vazio é lacuna: perguntar, não inventar. Nada marcado `(hipótese)` ou `(a confirmar)` vira afirmação pública.

## Dependências

- **Público:** `.business-os/publico.md` (dores, objeções, frases reais)
- **Estratégia de conteúdo:** `marketing/seo/05-estrategia-conteudo.md` (lista mestra de temas, criada pelo [seo](seo.md))
- **Outras pesquisas SEO:** `marketing/seo/01-pesquisa-demanda.md`, `02-analise-concorrencia.md`, `08-geo-otimizacao-ia.md`
- **Skill carrossel:** [carrossel](carrossel.md) deste plugin — usar pra fase do carrossel
- **Site (blog):** projeto do site dentro da pasta do negócio, se houver (ver Passo 2). Se não tiver site, perguntar antes
- **Tom de voz e limites:** `.business-os/mensagem.md`
- **Contexto:** `.business-os/negocio.md`, `.business-os/marca.md`

---

## Workflow

### Passo 0 — Escolher o tema

Se o usuário passou um tema explícito → usar.

Se não passou nada → ler `marketing/seo/05-estrategia-conteudo.md`, listar os artigos satélite + a página pilar, e perguntar:

> "Qual tema da estratégia? (lista de opções)"

Sem estratégia do [seo](seo.md), sugerir 3 a 5 temas a partir das dores, objeções e perguntas de `.business-os/publico.md`, priorizando o que serve ao objetivo de `.business-os/momento.md`.

Marcar mentalmente quais já viraram blog (checar pasta do blog) pra não duplicar.

### Passo 1 — Pesquisa rápida

Antes de escrever, ler o que tem nas pesquisas SEO sobre esse tema:
- Keyword principal e variações (`01-pesquisa-demanda.md`)
- Como concorrentes tratam (`02-analise-concorrencia.md`) — pra fugir do óbvio
- Ângulo GEO se aplicável (`08-geo-otimizacao-ia.md`) — perguntas que IAs respondem

Sem pesquisa SEO, seguir só com o contexto do negócio.

### Passo 2 — Escrever o blog post

**Destino:** procurar o projeto do site na pasta do negócio e descobrir onde ficam os posts pelos arquivos que já existem. Padrões comuns:
- Astro: `src/content/blog/<slug>.md`
- Next.js com MDX: `content/` ou `posts/`
- Hugo: `content/posts/<slug>.md`
- Site fora da pasta (WordPress, Wix, outro CMS): salvar o markdown em `marketing/conteudo/<pasta>/` pro usuário colar no editor
- Na dúvida, confirmar com o usuário

**Slug:** kebab-case curto, sem stopwords. Ex: "Como conservar carne salgada no restaurante" → `conservar-carne-salgada`.

**Frontmatter (se o stack usa markdown com frontmatter):**

```yaml
---
title: "Título atrativo, próximo da keyword"
description: "Meta description 150-160 caracteres, com keyword e benefício pro leitor"
publishedAt: YYYY-MM-DD
author: "<quem assina o blog — perguntar se não estiver claro>"
keywords:
  - keyword principal
  - variação 1
  - variação 2
draft: true
---
```

**Sempre começar com `draft: true`.** O usuário revisa e flipa pra `false` quando aprovar.

**Estrutura do artigo (800-1500 palavras):**

1. **Lead (1-2 parágrafos):** problema concreto do público, sem enrolação
2. **H2 explicativo:** o quê e por quê
3. **H2 prático:** como fazer / o que olhar
4. **H2 comparativo ou de detalhe técnico** (opcional)
5. **H2 onde a empresa se encaixa:** conexão natural com o produto, sem ser propaganda
6. **CTA final:** link WhatsApp / formulário / contato de `.business-os/negocio.md`

**Regras de escrita** (seguir Voz e Limites de `.business-os/mensagem.md` estritamente):
- Sem jargão de marketing/inglês quando o público não usa
- Lead e títulos com as palavras do público: usar as **Frases reais** de `publico.md`
- Frases curtas, parágrafos de 2-4 linhas
- Concreto: números, certificações, cases — só os que estão em **Provas** de `mensagem.md`
- Markdown limpo: `##` pra H2, `###` pra H3, listas com `-`, links em `[texto](../../publicar-tema/url)`

### Passo 3 — Carrossel resumo

Quando o pedido incluir artigo e derivados, produza o carrossel pelo procedimento [carrossel](carrossel.md), aproveitando a identidade e as referências da empresa. Um pedido apenas de artigo não inicia a produção visual.

**Pasta:** `marketing/conteudo/<slug-do-blog>-<YYYY-MM-DD>/`

Estrutura de slides do resumo:
- **Slide 1 — capa:** mesmo título do blog (ou variação enxuta)
- **Slides 2-6:** os pontos-chave do blog (1 ideia por slide, frase natural, não bullet seco)
- **Slide final — CTA pro blog:** "Texto completo no nosso blog" + URL `<dominio>/blog/<slug>`

**Capa:** seguir a identidade e as referências do negócio, com hierarquia e intensidade adequadas à mensagem. Não impor alternância de fundos ou formato de texto puro.

### Passo 4 — Legendas (3 versões)

Salvar todas em `marketing/conteudo/<pasta-do-carrossel>/`:

**`legenda.md`** (Instagram + Facebook — mesmo texto):
- Hook na primeira linha
- 2-3 parágrafos de contexto (frases naturais, sem corporativês)
- CTA pro carrossel ("Arraste pro lado") + CTA pro blog ("Texto completo no link da bio" ou URL direta)
- Bloco oferta da empresa (diferencial de `mensagem.md`, contato de `negocio.md`)
- Hashtags somente quando úteis ao objetivo e adequadas ao pedido; sem quantidade obrigatória

**`legenda-linkedin.md`** (LinkedIn — mais formal, sem hashtags):
- Hook (pode ser provocativo, profissional)
- 3-5 parágrafos analíticos — LinkedIn aceita texto longo
- Sem "arraste pro lado" (público diferente, comportamento diferente)
- CTA: link direto pro blog
- Sem bloco de oferta agressivo — fechar com 1 linha de quem é a empresa
- Máx 3 hashtags no final, do nicho profissional

Antes do resumo, revisar o post e as legendas seguindo o procedimento [revisar-copy](revisar-copy.md) (modo rápido). O carrossel já é revisado dentro do [carrossel](carrossel.md).

### Passo 5 — Resumo de entrega

No fim, mostrar pro usuário uma lista clara:

```
✓ Blog post: <caminho>/<slug>.md (draft)
✓ Carrossel: marketing/conteudo/<pasta>/
  - carrossel.html + render.js
  - PNGs em instagram/
✓ Legendas:
  - legenda.md (Insta + FB)
  - legenda-linkedin.md

Pra publicar:
1. Revisar o blog → flipar draft: false
2. Rebuild do site (se Astro/Hugo/etc) ou copiar pro CMS
3. Renderizar PNGs do carrossel: cd marketing/conteudo/<pasta> && node render.js
4. Postar carrossel no Insta + FB com legenda.md
5. Postar texto + link no LinkedIn com legenda-linkedin.md
```

---

## Quando NÃO usar esse procedimento

- Pedido de carrossel avulso (sem blog) → usar [carrossel](carrossel.md) direto
- Atualização de artigo existente → editar direto o .md
- Post único, frase de impacto → [carrossel](carrossel.md)

## Princípios

1. **Blog é a peça-mãe.** Carrossel e legendas são derivados dele, não o contrário.
2. **Tudo conectado.** Cada peça referencia a outra (carrossel linka pro blog, blog tem CTA pro contato).
3. **Draft sempre.** Nunca publicar automaticamente — usuário revisa antes.
4. **Linguagem do público real.** Sem corporativês. Sempre.
