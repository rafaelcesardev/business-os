# SEO completo + GEO + Google Ads

Localize a empresa e siga as regras gerais do [Cérebro da empresa](../../cortex/contexto.md). Leia `RESUMO.md` primeiro e depois os arquivos listados em Dependências; os caminhos de saída partem da pasta da empresa.

## Dependências

- **Público:** `cerebro/publico.md` (dores, objeções, frases reais)
- **Negócio e oferta:** `cerebro/negocio.md`
- **Tom de voz e limites:** `cerebro/mensagem.md`
- **Estratégia atual:** `cerebro/momento.md`
- **Ferramentas:** busca na web e leitura de páginas, nativas do ambiente (Claude Code e Codex têm)
- **Outputs vão em:** `marketing/seo/`

---

## Workflow

### Passo 1 — DEMANDA: O que as pessoas buscam nesse nicho?

**Objetivo:** Entender se existe demanda real e como as pessoas buscam.

1. Ler `cerebro/negocio.md` (produtos/serviços, região, diferenciais) e `cerebro/publico.md` (quem compra e, em **Onde ela está**, o que pesquisa no Google)
2. Gerar uma lista inicial de **30-50 termos-semente** baseados em:
   - Categorias de produto/serviço
   - Intenção de busca (informacional, comercial, transacional)
   - Localização (cidade, região, estado)
   - Uso final / contexto do cliente
3. Fazer **buscas na web** pra cada grupo de termos:
   - Buscar `"[termo] site:trends.google.com"` pra ver sazonalidade
   - Buscar `"[termo]"` pra ver o que aparece (orgânico, ads, maps)
   - Buscar `"[termo] related searches"` pra expandir a lista
4. Classificar cada termo por:
   - **Volume estimado:** alto / médio / baixo / micro
   - **Intenção:** informacional, comercial, transacional, navegacional
   - **Dificuldade:** quantos concorrentes fortes aparecem?
   - **Relevância:** direto (produto exato) / indireto (nicho relacionado) / tangencial

**Output:** Salvar em `marketing/seo/01-pesquisa-demanda.md` com:
- Tabela de termos classificados
- Top 10 termos prioritários (volume + intenção transacional + baixa concorrência)
- Termos sazonais
- Termos descartados e por quê

---

### Passo 2 — CONCORRÊNCIA: Quem aparece pra essas buscas?

**Objetivo:** Mapear quem domina os resultados e onde estão os gaps.

1. Pegar os **top 10 termos** do Passo 1
2. Pra cada termo, fazer a **busca na web** e analisar:
   - **Top 5 resultados orgânicos:** quem são, que tipo de página (site institucional, marketplace, blog, diretório)
   - **Resultados do Maps/Local Pack:** quem aparece, quantas avaliações, nota
   - **Google Ads:** alguém anuncia? qual a copy?
3. Pra cada concorrente relevante (máx 5-8, começando pelos da tabela **Concorrência** de `cerebro/mensagem.md`), **abrir o site** e analisar:
   - Estrutura do site (páginas, blog, catálogo)
   - Meta titles e descriptions das páginas principais
   - Conteúdo: falam de quê? com que profundidade?
   - Schema markup: usam dados estruturados?
   - GMB: perfil completo? fotos? posts? avaliações?
4. Identificar:
   - **Gaps:** o que nenhum concorrente faz bem
   - **Oportunidades:** termos onde ninguém domina
   - **Ameaças:** concorrentes fortes demais pra competir de frente
   - **Benchmark:** o padrão mínimo que o negócio precisa atingir
5. Concorrente novo ou informação nova sobre um conhecido: oferecer levar pra `cerebro/mensagem.md` com o `cortex`.

**Output:** `marketing/seo/02-analise-concorrencia.md` com:
- Tabela de concorrentes
- Mapa de gaps e oportunidades
- Recomendações: onde atacar primeiro

---

### Passo 3 — GMB: Google Meu Negócio (resultado mais rápido)

**Objetivo:** Montar o perfil completo do Google Business Profile pra aparecer no Maps e Local Pack.

1. Pesquisar como está o perfil atual (se existir): buscar o nome da empresa no Google
2. Criar documento com **tudo que precisa ser preenchido/otimizado:**

   **Informações básicas:**
   - Nome (idêntico ao registrado)
   - Categoria principal + secundárias (sugerir as melhores pro nicho)
   - Endereço, telefone, site, horário (de `cerebro/negocio.md`)
   - Área de atendimento

   **Descrição do negócio:**
   - Descrição otimizada (750 caracteres) com palavras-chave naturais
   - Tom: conforme `cerebro/mensagem.md`

   **Atributos e serviços:**
   - Serviços relevantes
   - Atributos (entrega, atacado, produção própria, etc.)

   **Fotos recomendadas:**
   - Checklist (fachada, interior, produtos, equipe, produção)
   - Especificações

   **Posts GMB:**
   - 4 posts iniciais sugeridos
   - Calendário de posts recorrentes

   **Estratégia de avaliações:**
   - Como pedir avaliações dos clientes atuais
   - Template de resposta (positivas e negativas) — usar [responder-avaliacoes](responder-avaliacoes.md)

   **Citações e diretórios:**
   - Lista de diretórios relevantes pro nicho
   - NAP consistente (Name, Address, Phone) pra todas as listagens

**Output:** `marketing/seo/03-google-meu-negocio.md`

---

### Passo 4 — ON-PAGE: Otimizar o site

**Objetivo:** Garantir que cada página esteja otimizada pras palavras-chave certas.

1. Ler a estrutura atual do site: projeto do site na pasta do negócio ou URL em **Presença** de `cerebro/negocio.md`; sem nenhum dos dois, perguntar as páginas
2. Pra cada página:

   **Mapeamento de palavras-chave por página**

   **Meta tags otimizadas:**
   - Title (50-60 caracteres, keyword no início)
   - Meta description (150-160 caracteres, com CTA)
   - H1, H2, H3 sugeridos

   **Schema Markup (dados estruturados):**
   - LocalBusiness schema (JSON-LD)
   - Product schema pros produtos
   - FAQ schema se tiver seção de perguntas

   **Checklist técnico:**
   - URLs amigáveis
   - Alt text das imagens
   - Velocidade de carregamento
   - Mobile-friendly
   - Sitemap.xml, robots.txt, canonical, Open Graph

   **Internal linking:** mapa de links internos sugerido

**Output:** `marketing/seo/04-otimizacao-on-page.md` com:
- Tabela: página → keyword principal → title → description → H1
- Schema markup pronto pra copiar (JSON-LD)
- Checklist técnico com status (feito / pendente)

---

### Passo 5 — CONTEÚDO: Estratégia de autoridade

**Objetivo:** Criar plano de conteúdo que posicione a empresa como referência no nicho.

1. Baseado nos termos do Passo 1 (especialmente os informacionais):

   **Páginas/posts evergreen:**
   - 5-10 ideias que respondem dúvidas reais do público
   - Pra cada ideia: título otimizado, keyword-alvo, estrutura de headings, estimativa de tamanho

   **Cluster de conteúdo:**
   - Página pilar
   - Páginas satélite que linkam pra pilar
   - Estrutura de internal linking

   **Calendário editorial:**
   - Prioridade de publicação
   - Frequência sugerida
   - Formato (blog post, guia, FAQ, comparativo)

   **Conteúdo local:**
   - Páginas de área de atendimento (se fizer sentido)
   - Conteúdo com referências locais

**Output:** `marketing/seo/05-estrategia-conteudo.md`

> Essa lista é o insumo do procedimento [publicar-tema](publicar-tema.md) — cada item dessa estratégia vira artigo + carrossel + legendas com um único comando.

---

### Passo 6 — GOOGLE ADS: pesquisa aplicada a anúncios

Esta etapa só entra quando o pedido inclui mídia paga. Use o procedimento [Google Ads](anuncio-google.md) para a estrutura, os textos e os CSVs; não mantenha outra versão dessas regras dentro de SEO.

Entregue a esse procedimento a pesquisa de demanda, os clusters e a análise de concorrência já disponíveis. Se existir `marketing/seo/06-google-ads.md` com planejamento anterior, reaproveite-o como insumo. As saídas da campanha seguem a pasta definida no procedimento de Google Ads.

---

### Passo 7 — MONITORAMENTO: Checklist mensal

**Objetivo:** Garantir que o trabalho continue dando resultado.

**Semanal:**
- Posição nos top 10 termos
- Responder avaliações no GMB
- Postar no GMB (1x/semana mínimo)

**Mensal:**
- Revisar métricas do Google Ads (CTR, CPC, conversões, custo/lead) — usar [relatorio-ads](relatorio-ads.md)
- Verificar tráfego orgânico (Google Search Console)
- Atualizar palavras-chave negativas
- Publicar 1-2 conteúdos do calendário editorial
- Verificar citações/diretórios

**Trimestral:**
- Refazer pesquisa de concorrência (Passo 2 resumido)
- Atualizar fotos e posts do GMB
- Revisar estratégia de conteúdo
- Avaliar novas oportunidades de keywords

**Output:** `marketing/seo/07-checklist-monitoramento.md`

---

### Passo 8 — GEO: Aparecer nas respostas de IAs

**Objetivo:** Otimizar a presença pra que IAs generativas (ChatGPT, Gemini, Perplexity, Copilot) citem a empresa quando alguém perguntar sobre o nicho.

**Por que importa:** Cada vez mais clientes perguntam pra IAs "qual o melhor fornecedor/serviço de X em Y?" — quem aparece ganha lead qualificado sem pagar ads.

1. **Auditoria GEO:**
   - Buscar os top 10 termos em engines de IA (Perplexity, etc.)
   - Verificar se a empresa (ou concorrentes) aparece
   - Mapear quais fontes as IAs citam pra esse nicho

2. **Conteúdo otimizado pra IA:**
   - Cada artigo do Passo 5 deve ter **respostas diretas** nas primeiras linhas
   - Incluir **dados concretos** (números, certificações, endereços, fatos verificáveis)
   - Estruturar com **perguntas como H2/H3** (formato Q&A)
   - Evitar texto vago — IAs descartam genérico

3. **FAQ Schema no site:**
   - Seção de FAQ com perguntas reais do nicho
   - Implementar FAQPage schema (JSON-LD)
   - 5-10 perguntas sugeridas baseadas no que o público pergunta

4. **Citações externas (menções):**
   - As IAs pesam menções em fontes confiáveis
   - Ações: diretórios, sites de avaliação, guest posts, menções em blogs do nicho, aparições em mídia

5. **Dados estruturados reforçados:**
   - LocalBusiness, FAQPage, Product, Article schemas

6. **Monitoramento GEO:**
   - A cada 30 dias, testar os top 5 termos no ChatGPT, Gemini, Perplexity
   - Registrar: a empresa apareceu? quem apareceu? fonte citada?
   - Ajustar conteúdo com base nos resultados

**Output:** `marketing/seo/08-geo-otimizacao-ia.md` com auditoria, FAQ + schema JSON-LD, lista de ações pra aumentar citações, checklist de monitoramento.

---

## Execução

Escolha somente as etapas que atendem ao pedido. Um pedido de Google Business Profile usa a etapa 3; não exige pesquisar e produzir as outras sete. Em um diagnóstico completo de presença nas buscas, encadeie as etapas pertinentes e use a etapa de anúncios somente se mídia paga fizer parte do escopo. Salve as saídas correspondentes e apresente os achados relevantes.

O usuário pode dizer “melhore meu perfil no Google” ou “quero aparecer nas respostas de IA”; identifique a etapa sem pedir seu número nem o nome do procedimento.

Ao finalizar, apresentar **resumo executivo** com:
- Top 5 oportunidades encontradas
- Ações prioritárias (o que fazer primeiro)
- Estimativa de investimento em ads
- Próximos passos recomendados

---

## Regras

- Toda pesquisa deve ser real (busca na web e páginas abertas de verdade), nunca inventar dados de volume ou concorrência
- Copies e textos seguem `cerebro/mensagem.md` estritamente
- Termos em português do Brasil, como o público busca
- Quando um dado não puder ser obtido (ex: volume exato), deixar claro que é estimativa e explicar a lógica
- Focar em termos com intenção comercial/transacional pra negócio B2C/B2B local
- Schema markup em formato JSON-LD (padrão Google)
- Google Ads: nunca inventar CPC ou estimativas de custo sem base real
