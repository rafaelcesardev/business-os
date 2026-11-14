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

O Cérebro (`cerebro/`), os documentos de trabalho e o site ficam no Git. Mídia pesada, planilhas e material bruto ficam fora e precisam de backup próprio.

## Gerenciar o negócio

Comece por `cerebro/RESUMO.md`. Qualquer IA aberta nesta pasta encontra o Cérebro pelo `AGENTS.md`.

Para manter o Cérebro e produzir com ele (posicionamento, copy, carrosséis, site, campanhas, prospecção, atendimento), instale o [Cortex](https://github.com/rafaelcesardev/cortex). Os métodos ficam nele; as informações da empresa ficam aqui. Quem só consulta pode usar apenas o plugin da empresa.
