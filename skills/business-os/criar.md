# Criar o contexto de um negócio

Cria a `.business-os/` a partir do modelo e conduz a entrevista que preenche os arquivos. O objetivo da primeira sessão é o `RESUMO.md` completo: com ele, as skills de criação já funcionam. O resto se aprofunda com o tempo, pela própria entrevista ou com material novo ([alimentar.md](alimentar.md)).

## Workflow

### Passo 1 — Onde criar

1. Procurar `.business-os/` na pasta atual e nas pastas acima. Se existir, não criar outra: avisar onde está e seguir [alimentar.md](alimentar.md) pra completar.
2. Use a pasta indicada pelo usuário; quando ele pedir para começar nesta pasta, use a atual. Pergunte o destino somente se estiver ambíguo. Essa vira a **pasta do negócio**. Siga [organizacao.md](organizacao.md) para separar contexto, marketing, site, atendimento e entregas; crie só o que a tarefa usa.
3. Copiar o modelo, que fica na pasta `modelo/` desta skill:

```bash
cp -R "${CLAUDE_SKILL_DIR}/modelo" "<pasta-do-negocio>/.business-os"
```

   Onde `${CLAUDE_SKILL_DIR}` não for substituído (Codex), usar o caminho real da pasta desta skill.

4. Aplique o padrão de [organização](organizacao.md): um repositório por empresa, contexto revisado e site versionados, produção local ignorada. Preserve as regras atuais da `.gitignore` e acrescente as exclusões do modelo. Não ignore a base `.business-os/` inteira. Se o repositório existente já adotar outra política, identifique o conflito antes de alterar o rastreamento. Um pedido de preparação local não autoriza criar repositório remoto, publicar ou conceder acesso.
5. Deixar a pasta do negócio se apresentando sozinha: qualquer agente aberto nela (Claude Code, Codex, outro) precisa achar o contexto sem ninguém chamar skill.
   - Inserir o conteúdo de [nota-agents.md](nota-agents.md) no `AGENTS.md` da pasta do negócio. Sem `AGENTS.md`, criar. Com `AGENTS.md`, acrescentar no fim. Se o bloco entre `<!-- business-os:inicio -->` e `<!-- business-os:fim -->` já estiver lá, substituir em vez de duplicar.
   - Se a pasta tiver `CLAUDE.md`, acrescentar nele a linha `@AGENTS.md`, se ainda não houver: com `CLAUDE.md` presente, o Claude Code não lê o `AGENTS.md`.
   - Projeto com repositório git próprio dentro da pasta (ex.: `site/`): o Codex só lê `AGENTS.md` a partir da raiz do repo. Oferecer o mesmo bloco no `AGENTS.md` do projeto, com os caminhos trocados de `.business-os/` pra `../.business-os/`.

   Avisar o usuário de cada arquivo criado ou alterado.

### Passo 2 — Material que já existe

Perguntar:
> "Tem algum material desse negócio? Transcrição de call, site, Instagram, formulário respondido, proposta, avaliações do Google."

O caso mais comum é a **transcrição de uma entrevista gravada**: a call com o dono do negócio, ou o próprio usuário respondendo o roteiro sobre o negócio dele. Processar todo material seguindo [alimentar.md](alimentar.md) antes da entrevista: cada resposta que o material já der é uma pergunta a menos, e depois de uma boa entrevista gravada o Passo 3 vira só a lista do que ficou faltando.

Sem transcrição ou material suficiente, conduza a entrevista agora com [roteiro-entrevista.md](roteiro-entrevista.md). Não exija que o usuário agende uma call: ele pode responder diretamente. Se preferir entrevistar alguém depois, entregue o roteiro com as lacunas relevantes.

### Passo 3 — Entrevista

Seguir os blocos de [roteiro-entrevista.md](roteiro-entrevista.md). Primeiro perguntar o básico que vai pro `RESUMO.md` e não está no roteiro: nome, links, e se é negócio do usuário ou cliente dele (e o que ele faz pra esse cliente).

Rodadas curtas, no máximo 5 perguntas por vez, começando pelos itens ★. Pular o que o material já respondeu. Cada pergunta traz um exemplo de resposta, pra pessoa entender o nível de detalhe.

Com os itens essenciais cobertos, registre o contexto e apresente o próximo passo conforme a meta. Aprofunde só o necessário à tarefa, sem transformar toda sessão em uma entrevista completa.

Quem responde pode ser o próprio usuário ou o cliente dele. Se o usuário preferir mandar as perguntas pro dono do negócio, gerar a partir do roteiro um questionário com os blocos pendentes, pronto pra enviar, e encerrar. As respostas voltam como material novo ([alimentar.md](alimentar.md)).

"Não sei" e "pula" são respostas válidas: o campo fica vazio e vira lacuna.

### Passo 4 — Escrever os arquivos

- Escrever com as palavras de quem respondeu. Frases que mostram como o cliente final fala vão literais pra **Frases reais** em `publico.md`.
- Campo preenchido perde o comentário-guia. Campo sem resposta mantém o comentário: é assim que a lacuna aparece.
- O que veio de dedução, não de resposta, leva `(hipótese)`.
- Atualizar `atualizado:` no frontmatter de cada arquivo alterado.
- Por último, o `RESUMO.md`: síntese dos outros arquivos, e em **O que falta saber** as lacunas que mais limitam a criação (preço, público, provas costumam ser as primeiras).
- Registrar em `historico.md`: `## AAAA-MM-DD — Contexto criado`.

### Passo 5 — Fechamento

Mostrar:

```
✓ Contexto criado em <pasta-do-negocio>/.business-os/
Preenchido: <arquivos com conteúdo>
Lacunas principais: <itens de O que falta saber>
```

Ao criar um negócio novo, prepare por padrão a própria base como plugin instalável seguindo [gerar-plugin-negocio](references/gerar-plugin-negocio.md), com manifestos locais e README de instalação para a equipe. Respeite um pedido explícito de criar somente o contexto. Preparar esses arquivos não publica o repositório, não instala o plugin nas contas e não concede acesso a ninguém. Para um projeto existente, preserve a estrutura e a etapa autorizada.

Escreva o README da raiz a partir de [modelo-readme.md](modelo-readme.md), preenchendo nome, finalidade, origem real, plugin, marketplace e pastas existentes. Ele deve conter um prompt curto para pedir a instalação à IA, os comandos para quem usa terminal, a estrutura atual e a referência ao repositório do Business OS como ferramenta de gerenciamento. Não apresente o Business OS como dependência obrigatória para apenas consultar o plugin da empresa. Mantenha o README objetivo, sem histórico de migração, nomes anteriores, notas de bastidores, botões ou links de instalação. Se ainda não houver origem utilizável para instalar, indique a publicação pendente em vez de deixar placeholders ou inventar comandos.

Informe os arquivos alterados, o que será versionado e o que precisa de backup local. A leitura automática depende do ambiente e da raiz aberta; confira a descoberta a partir do projeto usado. Depois, recomende o próximo passo e aponte o método adequado no [business-os](SKILL.md). O padrão do plugin é usar a própria base no repositório, com exportação separada somente quando necessária.

## Regras

- Nunca sobrescrever uma `.business-os/` que já existe, nem o resto de um `AGENTS.md` ou `CLAUDE.md`: a nota só entra entre os marcadores dela.
- Nunca inventar resposta pra fechar um campo. Lacuna declarada vale mais que conteúdo plausível.
- Uma rodada por mensagem. Despejar as 30 perguntas de uma vez faz a pessoa responder tudo pela metade.
- As perguntas moram só em `roteiro-entrevista.md`. Melhorou uma pergunta, é lá que muda.
- Saídas de trabalho (carrossel, proposta, campanha) não entram na `.business-os/`. Ela guarda só contexto.
