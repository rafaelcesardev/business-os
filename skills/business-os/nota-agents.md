<!-- business-os:inicio -->
## Contexto do negócio

O contexto deste negócio está em `.business-os/`. Antes de criar, planejar ou decidir
qualquer coisa pra ele, leia @.business-os/RESUMO.md e, conforme a tarefa:

| Arquivo | O que tem |
| --- | --- |
| `.business-os/negocio.md` | Oferta e preços, como o cliente chega e compra, operação, contato |
| `.business-os/publico.md` | Quem compra, dores, objeções, frases reais dos clientes |
| `.business-os/mensagem.md` | Concorrência, posicionamento, provas, voz, limites do que pode ser dito |
| `.business-os/marca.md` | Cores, fontes, logo (arquivos em `.business-os/assets/`), estilo visual |
| `.business-os/momento.md` | Objetivo atual, prioridades, fonte de andamento, orçamento, datas importantes |
| `.business-os/historico.md` | O que já foi feito e o que se aprendeu |
| `.business-os/referencias/` | Repertório revisado e leve, com origem e leitura do estilo |
| `.business-os/processos/` e `.business-os/agentes/` | Processos e instruções aprovados |
| `.business-os/fontes/` | Material bruto local; pode não acompanhar o clone nem o plugin |

Regras:
- Campo vazio é lacuna: perguntar, não inventar.
- `(hipótese)` e `(a confirmar)` não viram afirmação pública.
- Promessa só com prova registrada em `mensagem.md`; nada que cruze os limites de lá.
- A raiz usa o nome da empresa em kebab-case; as subpastas usam nomes curtos, sem repetir esse nome. Um repositório guarda o contexto revisado e o código em `site/`.
- `marketing/`, `atendimento/`, `entregas/`, `tmp/` e as fontes brutas são locais e ignorados pelo Git; precisam de backup separado. Recrie as áreas locais necessárias ao retomar um clone. Promova processos e instruções ao contexto somente após aprovação.
- Para continuar um trabalho, leia a fonte de andamento apontada em `momento.md` e confira o estado atual. Sem controle existente, use `planejamento/andamento.md`; revisões e análises ficam em `analises/`. Essas áreas também são locais, com backup separado. Entrega concluída não comprova resultado do negócio.
- A própria base pode ser instalável como plugin. Atualize a fonte principal e versione os manifestos quando necessário; não edite uma cópia instalada como segunda base.
- Informação nova sobre o negócio vai pro arquivo certo, com a fonte em `fontes/`
  (com o plugin business-os instalado, chamando o `business-os`).
<!-- business-os:fim -->
