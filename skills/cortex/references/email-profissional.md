# Rascunho de Email

Localize a empresa e siga as regras gerais do [Cérebro da empresa](../contexto.md). Leia `RESUMO.md` primeiro e depois os arquivos listados em Dependências; os caminhos de saída partem da pasta da empresa.

## Dependências

- **Negócio e oferta:** `cerebro/negocio.md`
- **Tom de voz e limites:** `cerebro/mensagem.md`

---

## Workflow

### Passo 1 — Coletar o contexto

Se o usuário não forneceu as informações necessárias, perguntar:
1. "Pra quem é o email? (nome, cargo, relação com você)"
2. "Qual é o objetivo? (cobrar, propor, responder, agradecer, seguir up...)"
3. "Tem algo específico que precisa constar ou que precisa evitar dizer?"

Se o usuário deu o contexto de forma livre (mesmo que bagunçado), extrai o que der e prossegue.

**Em nome de quem?** Definir antes de escrever:
- **O usuário falando com o cliente dele** (proposta, cobrança, relatório): usar **Quem cuida** do `RESUMO.md` pra contexto e o tom do próprio usuário.
- **O negócio falando com o público dele** (cliente final, fornecedor): usar Voz e Limites de `mensagem.md` e contato de `negocio.md`.

Se não der pra saber pelo pedido, perguntar.

### Passo 2 — Escrever o email

**Considerar:**
- Tom proporcional à relação (cliente novo = mais cuidado, parceiro antigo = mais direto)
- Objetivo claro na abertura (não enterrar o pedido no final)
- Uma ação pedida por vez
- Encerramento sem redundância ("Qualquer dúvida, fico à disposição" é padrão — só usar se fizer sentido)

**Estrutura:**
```
Assunto: [linha de assunto direta, sem clicbait]

[Nome],

[Parágrafo 1 — contexto ou referência ao último contato]

[Parágrafo 2 — o ponto principal ou o pedido]

[Parágrafo 3 — próximo passo, se houver]

[Assinatura]
[Nome de quem assina — perguntar se não estiver claro]
```

### Passo 3 — Apresentar opções de tom (quando fizer sentido)

Se o assunto for delicado (cobrança, feedback negativo, recusa), oferecer 2 versões:
- Versão A: mais direta
- Versão B: mais suave

Deixar o usuário escolher.

---

## Regras

- Tom segue `cerebro/mensagem.md` quando o email é em nome do negócio
- Nunca usar linguagem corporativa genérica sem necessidade
- Assunto do email deve ser específico e descritivo, não vago ("Seguimento", "Proposta")
- Se for um email de cobrança, ser direto mas sem agressividade
- Se for resposta a algo, citar o contexto na primeira linha
