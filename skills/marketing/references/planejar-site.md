# Plano de site ou landing page

Para localizar a empresa e usar contexto local ou fornecido por um plugin, siga [contexto do negócio](../../business-os/contexto.md).

Entrega o plano completo antes de qualquer código: o que o site precisa fazer, quais páginas e seções, os textos de cada uma e o briefing pra quem vai desenvolver. Cada seção existe por um motivo que vem do contexto do negócio.

## Contexto do negócio

Procurar a pasta `.business-os/` na pasta atual e, se não estiver ali, nas pastas acima. A pasta que contém `.business-os/` é a **pasta do negócio**: caminhos de saída como `marketing/...` são relativos a ela (sem `.business-os/`, à pasta atual). Ler `.business-os/RESUMO.md` primeiro e depois os arquivos listados em Dependências.

Se não houver `.business-os/` nem contexto fornecido por um plugin da empresa, avisar que o `business-os` monta o contexto e seguir com o que o usuário informar. Campo vazio é lacuna: perguntar, não inventar. Nada marcado `(hipótese)` ou `(a confirmar)` vira afirmação pública.

## Dependências

Todos os arquivos da `.business-os/`: um site usa o contexto inteiro.

- **Pesquisa SEO (se existir):** `marketing/seo/01-pesquisa-demanda.md` e `04-otimizacao-on-page.md`
- **Outputs vão em:** `planejamento/site-<YYYY-MM-DD>.md`

---

## Workflow

### Passo 1 — Tipo e objetivo

| Tipo | Quando |
| --- | --- |
| Landing page | Uma oferta, um público, uma ação. Ideal pra anúncio |
| Site institucional | Vários serviços, credibilidade, busca no Google |
| Site funcional | Precisa agendar, vender ou cadastrar dentro do site |

Definir a **ação principal** (chamar no WhatsApp, preencher formulário, agendar, comprar). Toda página empurra pra ela.

Se já existe site (**Presença** em `negocio.md`), abrir e listar o que funciona e o que falta antes de propor o novo.

### Passo 2 — Mapa do site

Landing page é uma página só. Institucional: listar as páginas, cada uma com objetivo e palavra-chave principal (da pesquisa SEO, se houver). Começar pelo mínimo que cumpre o objetivo; página que ninguém vai visitar não entra.

### Passo 3 — Seções

Ordem padrão de uma página de venda. Cada seção indica de onde vem o conteúdo:

| Seção | Conteúdo | Fonte |
| --- | --- | --- |
| Hero | Promessa central, prova curta, botão da ação principal | `mensagem.md` |
| Problema | As dores, com as palavras do público | `publico.md` |
| Solução | O que o negócio faz e pra quem | `negocio.md` |
| Como funciona | 3 a 4 passos do primeiro contato até o resultado | `negocio.md` |
| Provas | Depoimentos, números, cases, certificações | `mensagem.md` |
| Objeções / FAQ | Cada objeção da tabela com a resposta que funciona | `publico.md` |
| Quem faz | Equipe, história, local | `negocio.md` |
| CTA final | Ação principal de novo, com o contato | `negocio.md` |

Adaptar a ordem ao caso: em institucional, o hero pode ser mais amplo e os serviços ganham página própria.

### Passo 4 — Textos

Escrever o texto de cada seção, pronto pra usar:
- Títulos com as **Frases reais** de `publico.md` sempre que der.
- Toda promessa amarrada a uma **Prova**. Sem prova, promessa mais modesta.
- Onde faltar conteúdo, marcar `[FALTA: depoimento em vídeo de cliente]`, nunca preencher com texto genérico ou inventado.
- Com tudo escrito, revisar os textos seguindo o procedimento [revisar-copy](revisar-copy.md) (modo rápido).

### Passo 5 — Briefing técnico e visual

- **Visual:** cores, fontes e logo de `marca.md`; lista de imagens necessárias, dizendo quais o cliente já tem em `assets/` e quais faltam.
- **Integrações:** WhatsApp com mensagem pronta, formulário, agenda, pixel da Meta, Google Analytics, Search Console.
- **SEO básico:** title e description de cada página.
- **Infraestrutura:** domínio e hospedagem no nome do dono do negócio.
- **Mobile primeiro:** a maior parte do público chega pelo celular.

### Passo 6 — Entrega

Salvar em `planejamento/site-<YYYY-MM-DD>.md`, com as lacunas reunidas no fim. Mostrar o mapa e as lacunas no chat.

O plano serve de especificação. Se o usuário quiser construir, perguntar a stack e onde vai morar o projeto (por exemplo `site/` na pasta do negócio). Nunca começar o código sem esse ok.

---

## Regras

- Uma ação principal por página. Dois botões competindo dividem o clique.
- Nada de lorem ipsum ou texto de exemplo no plano: lacuna marcada é mais útil.
- Nada que cruze os **Limites** de `mensagem.md`.
- Quando o site for ao ar, oferecer registrar em `.business-os/historico.md` e atualizar **Presença** em `negocio.md`.

## Quando o pedido inclui desenvolver o site

Depois de definir o plano e a copy, prossiga com a implementação quando ela estiver no pedido do usuário. Use a ferramenta ou o projeto adequado, reutilizando o que já existe e seguindo as instruções do repositório. Salve o código na pasta de site registrada no negócio. Um briefing entregue não é um site implementado; informe separadamente o estado de implementação, testes e publicação. Se o pedido for apenas planejar, encerre no plano.
