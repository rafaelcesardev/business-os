# Criar o Cérebro de uma empresa

Monta a estrutura padrão e conduz a entrevista que preenche os arquivos. O objetivo da primeira sessão é o `RESUMO.md` completo: com ele, os métodos de criação já funcionam. O resto se aprofunda com o tempo, pela própria entrevista ou com material novo ([alimentar](alimentar.md)).

## Workflow

### Passo 1 — Montar a estrutura

1. Use a pasta indicada pelo usuário; quando ele pedir para começar aqui, a atual. Pergunte só se estiver ambíguo. Se já existir `cerebro/` nela ou acima, não crie outro: avise onde está e siga [alimentar](alimentar.md).
2. Rode o [caixa.py](scripts/caixa.py), que fica em `scripts/` ao lado deste arquivo, com o identificador em kebab-case e o nome real da empresa:

```bash
python3 <pasta-desta-skill>/scripts/caixa.py iniciar <pasta-da-empresa> --nome empresa-exemplo --titulo "Empresa Exemplo"
```

   Ele cria `cerebro/` a partir do modelo, os manifestos e catálogos do plugin da empresa, a skill `contexto`, o bloco do `AGENTS.md`, o `CLAUDE.md` e as regras da `.gitignore`. Não sobrescreve conteúdo: rodar de novo só completa o que falta e atualiza o bloco. Mostre ao usuário os arquivos criados ou alterados.
3. Projeto com repositório Git próprio dentro da pasta (ex.: `site/`): o Codex só lê o `AGENTS.md` da raiz daquele repositório. Ofereça o mesmo bloco lá, com os caminhos trocados para `../cerebro/`.

A estrutura e o que vai para o Git estão em [organização](organizacao.md). Montar a pasta não cria repositório remoto nem dá acesso a ninguém.

### Passo 2 — Material que já existe

Perguntar:
> "Tem algum material dessa empresa? Transcrição de call, site, Instagram, formulário respondido, proposta, avaliações do Google."

O caso mais comum é a **transcrição de uma entrevista gravada**: a call com o dono, ou o próprio usuário respondendo o roteiro sobre a empresa dele. Processar todo material seguindo [alimentar](alimentar.md) antes da entrevista: cada resposta que o material já der é uma pergunta a menos.

Sem material suficiente, conduza a entrevista agora com o [roteiro](roteiro-entrevista.md). Não exija que o usuário agende uma call: ele pode responder direto. Se preferir entrevistar alguém depois, entregue o roteiro com as lacunas relevantes.

### Passo 3 — Entrevista

Seguir os blocos do [roteiro](roteiro-entrevista.md). Primeiro o básico que vai pro `RESUMO.md` e não está no roteiro: nome, links, quem é o dono e quem cuida do Cérebro.

Rodadas curtas, no máximo 5 perguntas por vez, começando pelos itens ★. Pular o que o material já respondeu. Cada pergunta traz um exemplo de resposta, pra pessoa entender o nível de detalhe.

Com os itens essenciais cobertos, registre e apresente o próximo passo conforme a meta. Aprofunde só o necessário à tarefa, sem transformar toda sessão em entrevista completa.

Se o usuário preferir mandar as perguntas pro dono, gere a partir do roteiro um questionário com os blocos pendentes, pronto pra enviar, e encerre. As respostas voltam como material novo.

"Não sei" e "pula" são respostas válidas: o campo fica vazio e vira lacuna.

### Passo 4 — Escrever os arquivos

- Escrever com as palavras de quem respondeu. Frases que mostram como o cliente final fala vão literais pra **Frases reais** em `publico.md`.
- Campo preenchido perde o comentário-guia. Campo sem resposta mantém o comentário: é assim que a lacuna aparece.
- O que veio de dedução, não de resposta, leva `(hipótese)`.
- Atualizar `atualizado:` no frontmatter de cada arquivo alterado.
- Por último, o `RESUMO.md`: a síntese dos outros arquivos em cerca de 300 palavras, só com o que vale hoje. Histórico, fontes, versão do plugin e organização de pastas ficam fora dele. Em **O que falta saber**, até cinco lacunas que mais limitam o trabalho (preço, público e provas costumam ser as primeiras).
- Registrar em `historico.md`: `## AAAA-MM-DD — Cérebro criado`.

### Passo 5 — Fechamento

Rode `caixa.py conferir <pasta-da-empresa>` e corrija o que ele apontar. Depois mostre:

```
✓ Cérebro criado em <pasta-da-empresa>/cerebro/
Preenchido: <arquivos com conteúdo>
Lacunas principais: <itens de O que falta saber>
```

Escreva o README da raiz a partir do [modelo](modelo-readme.md), com nome, finalidade, repositório, plugin e pastas reais. Sem repositório publicado, indique a publicação como pendente em vez de deixar comandos com placeholders.

Recomende o próximo passo pelo objetivo do usuário. Publicar o repositório e instalar o plugin na equipe seguem [plugin no próprio repositório](references/repositorio-plugin.md), quando ele pedir.

## Regras

- Nunca sobrescrever um Cérebro que já existe, nem o resto de um `AGENTS.md` ou `CLAUDE.md`: a nota só entra entre os marcadores dela.
- Uma rodada por mensagem. Despejar as 30 perguntas de uma vez faz a pessoa responder tudo pela metade.
- As perguntas moram só no roteiro. Melhorou uma pergunta, é lá que muda.
