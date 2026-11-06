# Alimentar o contexto com material novo

Transforma material bruto em contexto. O bruto fica guardado como chegou em `fontes/`; os arquivos da `.business-os/` recebem só a síntese, com cada prova e cada frase real apontando de volta pra fonte.

## Workflow

### Passo 1 — Achar o contexto

Procurar `.business-os/` na pasta atual e nas pastas acima. Se não existir, seguir [criar.md](criar.md), que processa o material ao montar o contexto. Se o usuário citar outro negócio, perguntar o caminho da pasta dele.

### Passo 2 — Guardar a fonte

Salvar o material em `.business-os/fontes/AAAA-MM-DD-descricao.ext`, com a data em que o material foi produzido (a da call, a do print) e não a de hoje, quando der pra saber.

| Material | Como guardar |
| --- | --- |
| Arquivo (PDF, imagem, áudio, planilha) | Copiar o arquivo |
| Texto colado | `.md` com o texto exatamente como veio |
| Link (site, Instagram, Google) | `.md` com a URL na primeira linha e o conteúdo extraído abaixo |

Depois de salva, a fonte não se edita. Correção vira fonte nova. `fontes/` é bruto local ignorado pelo Git; o contexto versionado deve registrar a origem necessária para entender cada fato, mesmo se a fonte bruta não acompanhar o clone. Para referências de marketing, preserve o acervo em `marketing/referencias/` ou no caminho existente e registre a análise durável e os links em `.business-os/referencias/`, evitando duplicar as mídias. Arquivos oficiais leves da marca ficam em `assets/`. Siga [organização](organizacao.md) para distinguir repertório aprovado de produção.

### Passo 3 — Ler antes de extrair

Ler o material inteiro e os arquivos da `.business-os/` que ele pode tocar. Sem saber o que já está escrito, não dá pra distinguir informação nova, repetida ou contraditória.

### Passo 4 — Distribuir

| O material traz | Vai pra |
| --- | --- |
| Produto, serviço, preço, como entrega, como vende, equipe, ferramentas, contato | `negocio.md` |
| Quem compra, quanto já sabe, dores, desejos, objeções, gatilhos, onde pesquisa | `publico.md` |
| Frase de cliente final mostrando como ele fala | `publico.md` → Frases reais, literal, com a fonte |
| Concorrente e o que ele promete, diferencial, promessa | `mensagem.md` |
| Número, case, depoimento, certificação | `mensagem.md` → Provas, com a fonte |
| Jeito de falar, palavras usadas ou evitadas, o que não pode ser dito | `mensagem.md` → Voz ou Limites |
| Cor, fonte, logo, referência visual | `marca.md`; arquivos em `assets/` |
| Meta, prazo, prioridade, orçamento, data importante | `momento.md` |
| Decisão tomada, resultado de ação, aprendizado | `historico.md` |

Fato dito pelo negócio ou visto no material entra como fato. Conclusão tirada por dedução entra com `(hipótese)`.

**Transcrição de entrevista com o dono ou a equipe:** separar quem fala.
- O jeito como o dono fala do negócio é material de **Voz** (`mensagem.md`).
- Quando ele cita o cliente final ("eles sempre chegam perguntando se dói"), a frase vai pra **Frases reais** marcada `(relato do dono)`: vale como pista, mas é menos forte que a fala do próprio cliente.
- Quando o usuário entrevista outra pessoa, o que ele mesmo disse na call (sugestões, ideias, promessas) não é informação do negócio: só entra o que o dono disse. Quando o próprio usuário é o dono, o que ele diz é a fonte.

### Passo 5 — Mostrar antes de salvar

Apresentar as mudanças agrupadas por arquivo:

```
negocio.md
  + Oferta: Limpeza de pele — R$ 180
  ~ Carro-chefe: "botox" → "harmonização facial" (fonte diz que mudou em outubro)
publico.md
  + Frase real: "tenho vergonha de sorrir em foto" (fontes/2026-11-01-call.md)
Conflito: negocio.md diz atendimento só presencial; a call fala em consulta online. Qual vale?
```

Conflito nunca se resolve sozinho: mostre as versões e peça a decisão necessária. Se o usuário já pediu para incorporar informações confirmadas e não há conflito, aplique a atualização local e apresente o que mudou; não repita uma aprovação por arquivo.

### Passo 6 — Aplicar

- Campo preenchido perde o comentário-guia.
- Atualizar `atualizado:` em cada arquivo alterado.
- Tirar de **O que falta saber**, no `RESUMO.md`, o que foi respondido, e incluir lacunas novas que o material revelou.
- Se mudou algo que está no `RESUMO.md` (oferta principal, público, objetivo), atualizar o resumo também.
- Registrar em `historico.md` só decisões e resultados, não a entrada de cada fonte.

Fechar com uma linha por arquivo alterado e as lacunas que continuam abertas. Se vier outra entrevista (call com o dono ou o próprio usuário respondendo sobre o negócio dele), oferecer essas lacunas em forma de perguntas pra ela, no estilo de [roteiro-entrevista.md](roteiro-entrevista.md).

## Regras

- Frases reais e depoimentos entram literais. Corrigir o português de um cliente apaga exatamente o que torna a frase útil.
- Nada entra sem fonte em `fontes/`, mesmo que o usuário só tenha falado na conversa: nesse caso, a fonte é um `.md` com o que ele disse e a data.
- Evite guardar dados pessoais desnecessários nas fontes; quando forem necessários à tarefa, preserve o acesso adequado. CPF, telefone de cliente final, dados de saúde e credenciais não entram automaticamente na síntese nem no plugin entregue ao dono.
- Atualizar o contexto principal não altera um plugin instalado. Para distribuir uma atualização, revise o conteúdo versionado, atualize a versão dos manifestos e siga [gerar-plugin-negocio](references/gerar-plugin-negocio.md). O ZIP separado é opcional.
