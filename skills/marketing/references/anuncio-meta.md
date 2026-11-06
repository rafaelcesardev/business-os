# Campanha de Meta Ads

Para localizar a empresa e usar contexto local ou fornecido por um plugin, siga [contexto do negócio](../../business-os/contexto.md).

Entrega a campanha pronta pra subir no Gerenciador de Anúncios: estrutura, públicos, criativos com texto completo e checklist de medição. Cada criativo testa um ângulo diferente tirado do contexto do negócio.

## Contexto do negócio

Procurar a pasta `.business-os/` na pasta atual e, se não estiver ali, nas pastas acima. A pasta que contém `.business-os/` é a **pasta do negócio**: caminhos de saída como `marketing/...` são relativos a ela (sem `.business-os/`, à pasta atual). Ler `.business-os/RESUMO.md` primeiro e depois os arquivos listados em Dependências.

Se não houver `.business-os/` nem contexto fornecido por um plugin da empresa, avisar que o `business-os` monta o contexto e seguir com o que o usuário informar. Campo vazio é lacuna: perguntar, não inventar. Nada marcado `(hipótese)` ou `(a confirmar)` vira afirmação pública.

## Dependências

- **Público:** `.business-os/publico.md` (dores, objeções, frases reais, onde está)
- **Negócio e oferta:** `.business-os/negocio.md`
- **Tom de voz, provas e limites:** `.business-os/mensagem.md`
- **Orçamento e objetivo:** `.business-os/momento.md`
- **Visual:** `.business-os/marca.md`
- **Modelos de imagem:** [imagem-estatica.md](imagem-estatica.md)
- **Aprendizados anteriores:** `.business-os/historico.md`
- **Outputs vão em:** `marketing/campanhas/meta-ads-<YYYY-MM-DD>/`

---

## Workflow

### Passo 1 — Briefing

Montar com o contexto e perguntar só o que faltar:

1. **Oferta anunciada:** qual produto ou serviço, e por quanto
2. **Destino:** WhatsApp, site, formulário instantâneo da Meta, perfil
3. **Objetivo da campanha**, pelo que o negócio quer que aconteça:

| Quer | Objetivo na Meta |
| --- | --- |
| Conversas no WhatsApp | Engajamento → mensagens |
| Contatos por formulário | Cadastros |
| Vendas no site | Vendas (exige pixel com evento de compra) |
| Gente nova conhecendo | Reconhecimento ou Tráfego |

4. **Orçamento diário e região**
5. **Medição:** pixel e API de conversões configurados? Sem medição, a Meta otimiza às cegas: avisar antes de seguir.

### Passo 2 — Estrutura

Orçamento pequeno (até uns R$ 100/dia) pede estrutura simples:

```
Campanha: <Negócio> — <Objetivo> — <AAAA-MM>
└── Conjunto 1: público principal
    ├── Criativo A — ângulo dor
    ├── Criativo B — ângulo objeção
    └── Criativo C — ângulo prova
```

Mais orçamento: um segundo conjunto (remarketing ou público alternativo). Muitos conjuntos com pouco dinheiro cada um não saem da fase de aprendizado.

### Passo 3 — Públicos

- **Localização:** cidade ou raio a partir do endereço (`negocio.md`).
- **Público principal:** amplo, deixando a Meta encontrar quem converte, com sugestões de interesses tiradas de **Onde ela está** em `publico.md`.
- **Remarketing:** quem interagiu com o perfil, visitou o site ou chamou no WhatsApp.
- **Exclusões:** clientes atuais, se houver lista.
- Idade e gênero só restringem quando a oferta realmente é restrita.

### Passo 4 — Criativos

De 3 a 5 criativos, cada um com um ângulo diferente: uma dor, uma objeção, uma prova, um bastidor, uma frase real do cliente. Pra cada um:

```markdown
## Criativo <letra> — <ângulo>

**Formato:** vídeo 9:16 | imagem 4:5 | carrossel
**Gancho:** <vídeo: visual · fala · texto na tela, que se completam sem repetir (ver [roteiro-reels](roteiro-reels.md)); imagem: a frase que aparece primeiro, sem descrever a foto>
**Texto principal:** <aparecem ~125 caracteres antes do "mais"; o essencial vem primeiro>
**Título:** <até 40 caracteres>
**Botão:** Enviar mensagem | Saiba mais | Cadastre-se | Comprar agora
**Peça:** <roteiro ou brief da imagem>
```

- **Vídeo:** roteiro no formato do procedimento [roteiro-reels](roteiro-reels.md) (cenas, fala, texto na tela).
- **Imagem:** escolher um modelo de [imagem-estatica.md](imagem-estatica.md), um diferente por criativo, e entregar no formato de lá. Produzir com [carrossel](carrossel.md) (post único).
- **Carrossel:** brief da peça, ou produzir com [carrossel](carrossel.md).
- **Gerar a imagem ou o vídeo:** procedimento [gerar-midia](gerar-midia.md), que usa a ferramenta disponível no ambiente.
- O anúncio que parece post nativo costuma bater o que parece propaganda.
- **Antes de fechar:** revisar gancho, texto principal e título de cada criativo seguindo o procedimento [revisar-copy](revisar-copy.md) (modo rápido), sem estourar os limites de caracteres.

### Passo 5 — Configuração e medição

- Orçamento no conjunto ou na campanha, e duração do teste: 7 dias sem mexer, salvo queima evidente.
- Evento de conversão certo pro objetivo, pixel e API de conversões ativos.
- UTMs nos links pro site (`utm_source=meta&utm_medium=paid&utm_campaign=<nome>`).
- Posicionamentos automáticos, a menos que um formato não tenha peça adequada.

### Passo 6 — Entrega

```
marketing/campanhas/meta-ads-<YYYY-MM-DD>/
  plano.md       ← briefing, estrutura, públicos, configuração, checklist de subida
  criativos.md   ← todos os criativos com texto completo
```

Mostrar no chat a estrutura e os ângulos. Subir tudo pausado; o usuário ativa depois de revisar. Quando for ao ar, oferecer registrar em `.business-os/historico.md` pra comparar com o [relatorio-ads](relatorio-ads.md).

---

## Regras

- **Políticas da Meta:** texto não pode afirmar nem insinuar atributo pessoal de quem lê ("Você está acima do peso?"). Saúde, estética, finanças e emagrecimento têm restrições extras. Crédito, emprego, moradia e temas sociais exigem categoria especial declarada.
- Nada que cruze os **Limites** de `mensagem.md`, mesmo que a Meta aprove.
- Prova e número só de **Provas** em `mensagem.md`. Nunca prometer resultado.
- Se `historico.md` registra o que já funcionou ou não com esse público, partir disso.
