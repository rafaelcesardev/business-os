# Plugin no próprio repositório

O repositório da empresa serve de pasta de trabalho e de origem do plugin que a equipe instala no Codex e no Claude Code. Não há cópia nem ZIP: `cerebro/` é a raiz do plugin. A estrutura completa está em [organização](../organizacao.md).

## Preparar

Rode o [caixa.py](../scripts/caixa.py) com `iniciar <pasta-da-empresa>`. Ele cria o que faltar e preserva o que existe, inclusive entradas de outros plugins nos catálogos:

| Arquivo | Papel |
| --- | --- |
| `cerebro/plugin.json` | Manifesto portátil |
| `cerebro/.codex-plugin/plugin.json` | Manifesto Codex |
| `cerebro/.claude-plugin/plugin.json` | Manifesto Claude Code |
| `cerebro/skills/contexto/SKILL.md` | Entrada do plugin: lê os documentos originais, sem duplicá-los |
| `.agents/plugins/marketplace.json` | Catálogo Codex, na raiz do repositório, apontando para `./cerebro` |
| `.claude-plugin/marketplace.json` | Catálogo Claude Code, na raiz do repositório, apontando para `./cerebro` |

Depois ajuste o que o script não tem como saber:

- **Descrição:** troque a descrição genérica dos manifestos e da skill por uma que diga o que a empresa faz e a que consultas o Cérebro responde. É ela que faz a IA acionar o plugin.
- **Responsável:** `author` e `owner` saem com o nome da empresa; troque por quem mantém o catálogo, quando for outra pessoa.
- **Ícone:** com logo oficial, prepare em `cerebro/assets/` uma versão quadrada em PNG ou JPEG e aponte para ela em `composerIcon` e `logo` (portátil e Codex) e em `icon` (Claude Code).
- **Nome:** mantenha o identificador estável; trocá-lo quebra a atualização de quem já instalou.

O plugin leva só contexto: sem métodos, hooks, servidores ou automações. Tudo que estiver versionado dentro de `cerebro/` acompanha a instalação; revise pensando em quem vai receber.

## README para instalar e usar

Use o [modelo de README](../modelo-readme.md) com os dados reais: nome, finalidade, repositório, plugin, marketplace e a árvore das pastas que existem. O README mostra o estado atual, sem histórico de migração nem nomes anteriores.

- O prompt para leigos traz a origem real e pede que a IA instale sem alterar a empresa. Uma IA sem ferramentas de instalação só consegue orientar os passos.
- Os comandos instalam no Codex e no Claude Code, não no chat comum do Claude. O comando único do Claude Code pede uma CLI recente; em versões sem `--marketplace`, adicione o marketplace e instale em dois comandos.
- Repositório privado pede acesso e autenticação de quem instala. Não cole credenciais no README.
- Sem repositório publicado, indique a publicação como pendente em vez de comandos com placeholders.

Fontes: [Plugins no ChatGPT e Codex](https://learn.chatgpt.com/docs/plugins), [instalação no Claude Code](https://code.claude.com/docs/en/discover-plugins) e [plugins no Claude e Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

## Conferir antes de distribuir

```sh
python3 <pasta-desta-skill>/scripts/caixa.py conferir <pasta-da-empresa>
claude plugin validate <pasta-da-empresa>/cerebro
claude plugin validate <pasta-da-empresa>
```

Sem logo oficial, o validador do Claude Code avisa que falta o ícone; é esperado.

O `conferir` verifica nome e versão iguais nos três manifestos, o destino dos catálogos, os links dentro do Cérebro, o tamanho do resumo e o bloco do `AGENTS.md`. Confira também `git ls-files`: material bruto, credenciais e dados de outras empresas não acompanham a entrega, e quem recebe acesso ao repositório vê também o histórico.

Arquivos válidos não comprovam a instalação nem a qualidade das respostas. Instalar, fazer perguntas de teste e testar com outra conta são verificações à parte; registre as que de fato foram feitas.

## Publicar uma mudança

Aumente a versão nos três manifestos, publique quando autorizado e atualize o marketplace e o plugin em cada cliente.

## Formatos oficiais

- [Empacotamento e catálogos do Codex](https://developers.openai.com/plugins/build/plugins)
- [Catálogo do Claude Code](https://code.claude.com/docs/en/plugin-marketplaces)
- [Manifesto do Claude Code](https://code.claude.com/docs/en/plugins-reference)
