# {{empresa}}

{{descricao}}

## Instalar o plugin

### Pedir à sua IA

Copie o texto abaixo para o Codex ou Claude Code com acesso ao seu computador:

```text
Instale neste ambiente o plugin de contexto da {{empresa}} a partir do repositório privado {{repositorio}}. O plugin se chama {{plugin}} e o marketplace se chama {{marketplace}}. Use as ferramentas disponíveis, sem modificar os arquivos ou serviços da empresa. Se faltar acesso ao GitHub ou alguma etapa depender de mim, me oriente. Confirme a instalação e explique como começar a usar.
```

Uma IA sem ferramentas de instalação ou acesso ao computador poderá apenas orientar os passos.

### Usar o terminal

Requer a CLI do aplicativo atualizada e acesso autenticado ao repositório privado no GitHub.

**Codex:**

```sh
codex plugin marketplace add {{repositorio}}
codex plugin add {{plugin}}@{{marketplace}}
```

**Claude Code:**

```sh
claude plugin install {{plugin}} --marketplace {{repositorio}}
```

Depois da instalação, abra uma conversa nova no Codex ou reinicie a sessão do Claude Code. Use o plugin {{empresa}} para consultar o contexto da empresa.

## Estrutura

```text
{{estrutura}}
```

O contexto revisado e o site ficam no Git. Produção, rascunhos e pacotes locais precisam de backup separado.

## Gerenciar o negócio

Comece por `.business-os/RESUMO.md`. Recomendamos instalar o [Business OS](https://github.com/rafaelcesardev/business-os) para organizar o contexto, criar copy e carrosséis e planejar sites, campanhas e atendimento. Os métodos ficam no Business OS; as informações da empresa ficam neste repositório.

O Business OS é a ferramenta de gerenciamento. Quem precisa apenas consultar o contexto pode usar somente o plugin da empresa.
