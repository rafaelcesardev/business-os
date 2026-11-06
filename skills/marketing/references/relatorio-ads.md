# Relatório semanal de Google Ads + Meta Ads

Para localizar a empresa e usar contexto local ou fornecido por um plugin, siga [contexto do negócio](../../business-os/contexto.md).

Procedimento que transforma exports brutos das plataformas em relatório executivo que o dono entende sem precisar abrir a interface do Google ou da Meta.

## Contexto do negócio

Procurar a pasta `.business-os/` na pasta atual e, se não estiver ali, nas pastas acima. A pasta que contém `.business-os/` é a **pasta do negócio**: caminhos de saída como `marketing/...` são relativos a ela (sem `.business-os/`, à pasta atual). Ler `.business-os/RESUMO.md` primeiro e depois os arquivos listados em Dependências.

Se não houver `.business-os/` nem contexto fornecido por um plugin da empresa, avisar que o `business-os` monta o contexto e seguir com o que o usuário informar. Campo vazio é lacuna: perguntar, não inventar. Nada marcado `(hipótese)` ou `(a confirmar)` vira afirmação pública.

## Dependências

- **Contexto:** `.business-os/negocio.md`, `.business-os/historico.md` (campanhas lançadas e aprendizados)
- **Metas:** `.business-os/momento.md` (orçamento, CPA ou custo por contato alvo). Sem meta registrada, perguntar uma vez na resposta ao usuário e oferecer guardar com o `business-os`; no relatório, registrar a meta como lacuna, sem afirmar que a pergunta foi feita
- **Tom de voz e limites:** `.business-os/mensagem.md`
- **Inputs:** CSVs do Google Ads e/ou Meta Ads Manager. Print também aceito (transcrever)
- **Histórico:** `marketing/campanhas/relatorios/` (criar se não existir)

---

## Como rodar

O usuário pede a análise e fornece ou indica os arquivos, por exemplo:

```
Analise os resultados destes arquivos do Google e da Meta.
```

Se não houver arquivos ou dados disponíveis, pergunte onde estão os exports. Não exija um comando específico nem um CSV quando os números já tiverem sido fornecidos no pedido.

## Workflow

Adapte a profundidade ao pedido. Os passos abaixo orientam um relatório completo; uma análise breve de números fornecidos pode voltar no chat, sem inventar período, campanhas ou dados para preencher o modelo nem exigir salvar um relatório semanal.

### Passo 1 — Ler os exports

**Google Ads:** colunas mínimas esperadas — Campanha, Grupo, Impressões, Cliques, CTR, CPC médio, Custo, Conversões, CPA, Conv. rate.

**Meta Ads:** colunas mínimas esperadas — Campanha, Conjunto, Impressões, Alcance, Cliques no link, CTR, CPM, Frequência, Custo, Resultados, Custo por resultado.

**Meta Ads, por anúncio, se tiver vídeo:** Reproduções de vídeo de 3 segundos, ThruPlays e Reproduções do vídeo até 50%. Sem essas colunas, o diagnóstico de criativo do Passo 4 fica só com CTR e custo por resultado: pedir pra incluir no próximo export.

Use os campos disponíveis, mesmo quando o usuário fornecer um resumo em vez das colunas da plataforma. Identifique o evento medido: lead, mensagem, agendamento ou venda. Calcule custo por lead quando houver leads; CPA de cliente e retorno sobre vendas exigem dados de aquisição ou receita. Vendas não informadas são desconhecidas, não zero. Não some eventos diferentes nem trate a soma dos canais como clientes únicos sem deduplicação. Sem dados de resultado, avise e analise somente o tráfego.

Preserve as definições na interpretação e nas recomendações conforme a [análise compartilhada](../../business-os/references/analisar-dados.md): cliques não comprovam contatos recebidos, e a queda depois do clique não identifica sozinha qual parte causou o problema.

### Passo 2 — Comparar com a semana anterior

Buscar em `marketing/campanhas/relatorios/` o relatório anterior. Se existir, calcular variação semana vs semana:

- Investimento total
- Cliques / Impressões
- CTR (clique / impressão)
- CPC / CPM
- Conversões totais (Google + Meta)
- CPA (custo / conversão)
- Custo por canal

Se não existir, é a primeira leitura — sinalizar como baseline.

### Passo 3 — Resumo executivo (topo do relatório)

Uma página, leitura de 2 minutos. Estrutura:

```markdown
# Relatório de Ads — semana <DD/MM> a <DD/MM>

## Resumo executivo

**Investimento:** R$ X.XXX (▼/▲ Y% vs semana anterior)
**Conversões:** N (▼/▲ Y%)
**CPA médio:** R$ X.XX (▼/▲ Y%)

**Canais:**
- Google Ads: R$ X.XXX → N conversões (CPA R$ X.XX)
- Meta Ads:   R$ X.XXX → N conversões (CPA R$ X.XX)

**Headline da semana:** 1 frase do que mais importa (campanha que estourou, criativo que matou,
alerta de orçamento, queda inesperada).
```

### Passo 4 — Detalhamento por canal

Pra cada canal, listar:

**Top 3 campanhas/grupos por performance** (menor CPA, maior conv. rate)
**Bottom 3** (maior CPA, menor conv. rate) — sinalizar pra pausar ou ajustar
**Top criativos** (Meta): impressões + CTR + custo por resultado
**Bottom criativos** (Meta): pra trocar ou pausar
**Palavras-chave com mais custo e zero conversão** (Google) — virar negativas

**Diagnóstico de criativo pelo funil** (Meta). Antes de mandar trocar um criativo, investigar a etapa que mudou. A tabela orienta hipóteses, sem identificar a causa por uma métrica isolada:

| Etapa | Métrica | O que investigar (hipótese) | Ajuste a testar após confirmar |
| --- | --- | --- | --- |
| Parar | Reproduções de 3s ÷ impressões | O visual dos primeiros 3 segundos não para o dedo | Só a abertura: novo visual e texto na tela, o resto igual ([roteiro-reels](roteiro-reels.md)) |
| Ficar | ThruPlays (ou até 50%) ÷ reproduções de 3s | A ponte, dos 3 aos 15 segundos, não continua o gancho | Os segundos 3 a 15, não o gancho |
| Clicar | CTR (cliques no link) | A promessa, a prova ou o CTA no meio do anúncio | Texto principal, título e CTA ([revisar-copy](revisar-copy.md)) |
| Converter | Custo por resultado, conversão depois do clique | Desalinhamento entre promessa, público, destino ou atendimento | A parte sustentada pelo diagnóstico: anúncio, público, página ([planejar-site](planejar-site.md)) ou atendimento |

Imagem não tem as duas primeiras etapas: começar pelo CTR.

Comparar cada criativo com a média da própria conta e com as semanas anteriores (`historico.md`), não com média de mercado. Duas leituras que esta tabela evita:

- **Para muita gente e não converte não é vencedor.** Gancho que atrai o público errado aparece como taxa de 3s alta e conversão no chão. Ler o funil inteiro antes de escalar.
- **Uma peça por vez.** A recomendação troca o visual da abertura, ou a ponte, ou o texto, nunca tudo junto, senão a próxima semana não diz o que funcionou.

### Passo 5 — Alertas automáticos

Varrer os dados e gerar alertas em vermelho/amarelo:

| Alerta | Critério |
|---|---|
| 🔴 Queima de orçamento | Campanha gastou >R$X com 0 conversões |
| 🔴 CTR despencou | CTR caiu >30% vs semana anterior |
| 🟡 Frequência alta (Meta) | Conjunto com freq > 3.0 — público saturado |
| 🟡 Conv. rate baixa | <1% em campanha Search |
| 🟡 CPC subindo | CPC médio +20% vs semana anterior |
| 🟡 Clica e não converte | CTR acima da média da conta e custo por resultado acima da meta → investigar promessa, público, destino e atendimento, sem causa definida por essas taxas |
| 🟢 Oportunidade | Campanha com CTR/conv acima da média + orçamento limitado → considerar aumentar |

### Passo 6 — Recomendações pra semana

Lista curta (3-5 itens) de ações concretas:

```markdown
## Pra fazer na próxima semana

1. **Pausar** Grupo "X" — gastou R$ 230 sem conversão em 7 dias
2. **Adicionar negativas:** [lista de termos que apareceram nos search terms e não convertem]
3. **Trocar a abertura** do criativo B do conjunto "Y" — taxa de 3s metade da média da conta; ponte e texto seguem iguais
4. **Aumentar orçamento** da campanha "Z" — CPA R$ 12, abaixo do alvo
5. **Testar** novo RSA com headline "<sugestão baseada em concorrência atual>"
```

### Passo 7 — Salvar

```
marketing/campanhas/relatorios/<YYYY-MM-DD>-relatorio.md
```

Frontmatter com:
```yaml
---
periodo_inicio: YYYY-MM-DD
periodo_fim: YYYY-MM-DD
investimento_total: 0000.00
conversoes_total: 0
cpa_medio: 00.00
canais: [google-ads, meta-ads]
---
```

Esse frontmatter facilita comparações futuras com scripts e a leitura de longo prazo.

### Passo 8 — Entrega

Mostrar o resumo executivo direto no chat (Passos 3 + 5 + 6) e apontar pro arquivo completo:

> "Relatório completo em `marketing/campanhas/relatorios/<data>-relatorio.md`. Quer um email com o resumo (pro cliente ou pra equipe)?"

Se sim, chamar `email-profissional` com o resumo executivo + link/anexo.

Se o relatório confirmou um aprendizado que se repete (criativo, público ou palavra-chave que funciona ou não funciona pra esse negócio), oferecer registrar em **O que já sabemos** de `.business-os/historico.md`.

---

## Regras

- **Nunca inventar números.** Se o export tá truncado ou ilegível, dizer "dados incompletos" e seguir só com o que dá.
- **Comparação é o que importa.** Número solto ("R$ 1.200 essa semana") não significa nada sem o comparativo.
- **Alertas em ordem.** Vermelho primeiro, amarelo depois, verde por último.
- **Recomendações concretas.** "Pausar Grupo X" > "Otimizar campanhas". Nome da campanha, valor, motivo.
- **Linguagem do dono.** Seguir `.business-os/mensagem.md`. CPM, CTR, CPA são OK se o dono já entende; se não, traduzir pelo evento medido ("custo por mil exibições", "% das exibições que viraram clique", "quanto custou cada contato"). Só usar "cliente" quando houver aquisição medida.
- **Alertas são hipóteses de diagnóstico.** Frequência e taxas isoladas não provam saturação nem a causa da queda. Interprete os limiares da tabela com o objetivo, período, tamanho do público, volume e histórico disponíveis; sem contexto suficiente, registre a limitação.
- **Quando reportar perda:** descreva o dado observado sem inventar a conclusão. "A campanha X gastou R$ 200 e não registrou leads" só cabe se houver medição de leads; ausência de dados de vendas não prova que não houve venda.
