# Análise de Arquivo

Para localizar a empresa e usar contexto local ou fornecido por um plugin, siga [contexto do negócio](../contexto.md).

## Contexto do negócio

Procurar a pasta `.business-os/` na pasta atual e, se não estiver ali, nas pastas acima. A pasta que contém `.business-os/` é a **pasta do negócio**: caminhos de saída como `marketing/...` são relativos a ela (sem `.business-os/`, à pasta atual). Ler `.business-os/RESUMO.md` primeiro e depois os arquivos listados em Dependências.

Se não houver `.business-os/` nem contexto fornecido por um plugin da empresa, avisar que o `business-os` monta o contexto e seguir com o que o usuário informar. Campo vazio é lacuna: perguntar, não inventar. Nada marcado `(hipótese)` ou `(a confirmar)` vira afirmação pública.

## Dependências

- **Negócio e oferta:** `.business-os/negocio.md` (pra entender o que os dados representam)
- **Tom de voz e limites:** `.business-os/mensagem.md`

---

## Workflow

### Passo 1 — Entender o contexto

Antes de analisar, perguntar se não estiver claro:
- "O que é esse arquivo? (vendas, anúncios, métricas, respostas de pesquisa...)"
- "Qual é a pergunta principal que você quer responder com esses dados?"

Se o contexto estiver óbvio pelo nome do arquivo ou pelo conteúdo, prossegue sem perguntar.

### Passo 2 — Ler o arquivo

Ler o arquivo fornecido. Se for Excel (.xlsx), ler com as ferramentas disponíveis pra extrair o conteúdo das células.

### Passo 3 — Análise

Preserve o significado de cada indicador também na explicação e nas recomendações. Cliques não são contatos, contatos não são pedidos e pedidos não são clientes únicos sem essa definição na fonte. Não estime o volume de uma etapa a partir de outra sem dados que liguem as duas; uma possível explicação continua como hipótese, sem números ou eventos intermediários inventados.

Identificar e reportar:

**O que está bom:**
- Métricas acima da média ou em crescimento
- Padrões positivos nos dados
- Top performers (produtos, campanhas, períodos, etc)

**O que preocupa:**
- Quedas, anomalias ou tendências negativas
- O que está abaixo do esperado
- Gargalos ou desperdícios visíveis

**Comparações:**
- Contra as metas de `.business-os/momento.md`, quando houver
- Período atual vs período anterior (se houver)
- Top vs bottom performers
- Distribuição entre categorias

**Insights não óbvios:**
- Correlações interessantes
- Padrões que não aparecem na leitura superficial

### Passo 4 — Output

Gerar um resumo executivo em prosa (não só bullet points):

```markdown
# Análise — [Nome do Arquivo/Relatório]
*[Data da análise]*

## O que esses dados mostram
[2-3 parágrafos com o panorama geral]

## O que está funcionando
[lista com contexto]

## O que merece atenção
[lista com contexto]

## 3 recomendações
1. [ação concreta]
2. [ação concreta]
3. [ação concreta]

## Números-chave
| Métrica | Valor | Contexto |
|---------|-------|---------|
| ... | ... | ... |
```

Salvar em `analises/analise-[nome]-[data].md` na pasta do negócio.

Se a análise mudou algo que o contexto afirma (carro-chefe, ticket médio, perfil de quem compra), oferecer atualizar com o `business-os`, com o arquivo analisado como fonte.

Perguntar se quer exportar o resumo em HTML pra compartilhar ou apresentar.

---

## Regras

- Análise em prosa, não só listas — o usuário deve poder ler e entender sem abrir o arquivo original
- Nunca inventar dados que não estão no arquivo
- Se os dados estiverem incompletos ou com problemas, mencionar antes de analisar
- Tom conforme `.business-os/mensagem.md`
