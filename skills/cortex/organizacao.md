# Organização da empresa

## Um repositório por empresa

Cada empresa tem um repositório privado com raiz em kebab-case, por exemplo `churrascaria-do-jonas/`. Dentro dele, nomes curtos, sem repetir o nome da empresa.

```text
churrascaria-do-jonas/
  AGENTS.md                              mapa para qualquer IA aberta na pasta
  CLAUDE.md                              aponta para o AGENTS.md
  README.md                              como instalar e usar o plugin da empresa
  .gitignore
  .agents/plugins/marketplace.json       catálogo Codex
  .claude-plugin/marketplace.json        catálogo Claude Code
  cerebro/                               o Cérebro: o que a equipe consulta; raiz do plugin
    RESUMO.md                            lido primeiro em toda tarefa
    negocio.md  publico.md  mensagem.md  marca.md  momento.md  historico.md
    processos/                           como a empresa trabalha: venda, atendimento, entrega
    modelos/                             documentos reusáveis: proposta, roteiro de call
    conhecimento/                        aprendizados e referências de negócio
    referencias/                         repertório de marketing, leve e com origem
    agentes/                             instruções aprovadas de atendentes com IA
    assets/                              logo e arquivos oficiais da marca
    fontes/                              material bruto, fora do Git
    skills/contexto/SKILL.md             entrada do plugin da empresa
    plugin.json  .codex-plugin/  .claude-plugin/
  site/                                  código do site
  marketing/  comercial/  atendimento/   trabalho de cada área
  planejamento/  analises/               andamento, planos e revisões
  entregas/  tmp/                        pacotes gerados e temporários, fora do Git
```

O [caixa.py](scripts/caixa.py) monta essa estrutura (`iniciar`) e aponta o que foge dela (`conferir`). Crie as pastas de trabalho só quando forem usadas.

## Cérebro ou pasta de trabalho

No Cérebro entra o que está valendo e que a equipe precisa consultar. Quem instala o plugin da empresa recebe exatamente essa pasta.

Rascunhos, versões em teste, produção e andamento ficam nas pastas de trabalho da raiz. Quando o responsável aprova um processo, um modelo ou uma instrução de atendente, mova o documento para o Cérebro, registre a decisão em `historico.md` e atualize quem apontava para o caminho antigo. O documento aprovado passa a ser a fonte; uma revisão só o substitui depois de aprovada.

- **Marca e referências:** as escolhas da marca ficam em `marca.md`. Em `referencias/` vai o repertório durável: URL, autor, o que aproveitar e os limites de uso. Acervos completos, downloads e vídeos ficam em `marketing/referencias/`.
- **Andamento:** para [continuar um trabalho](references/continuar-trabalho.md), use o controle que a empresa já tem (CRM, quadro). Sem um, use `planejamento/andamento.md`. [Revisões](references/revisar-negocio.md) e [conferências de resultado](references/conferir-resultados.md) ficam em `analises/`. Em `momento.md` vai só o apontador.

## O que vai para o Git

Documentos de texto são versionados, inclusive os de trabalho. Fica fora o que é pesado, bruto ou sigiloso:

| Fica fora | Motivo |
| --- | --- |
| `cerebro/fontes/` | Bruto: transcrições e prints podem trazer dados pessoais |
| Vídeo, áudio e ZIP | Pesados; guarde em drive ou backup |
| Planilhas e CSV | Costumam trazer listas de clientes e contatos |
| `entregas/`, `tmp/`, dependências e builds | Regeneráveis |
| `.env` e credenciais | Segredos |

O `caixa.py iniciar` acrescenta essas regras à `.gitignore` e mantém as que já existem. A `.gitignore` não retira arquivos já rastreados nem apaga nada do disco, e o que fica fora do Git precisa de backup próprio. Num projeto antigo, confira com `git status` o que vai entrar antes de versionar; não use `git add .` às cegas.

## Plugin da empresa

`cerebro/` é ao mesmo tempo a fonte editável e a raiz do plugin: os catálogos na raiz do repositório apontam para ela, sem cópia. O passo a passo está em [plugin no próprio repositório](references/repositorio-plugin.md).

- Quem instala recebe uma versão. Para distribuir uma mudança, aumente a versão nos três manifestos e publique.
- Quem tem acesso ao repositório vê tudo que está nele, inclusive o site e o histórico. Para entregar só uma seleção, use o [exportador](references/gerar-plugin-negocio.md).
- Para a equipe só consultar, dê permissão de leitura no GitHub. Em repositório privado de conta pessoal, todo colaborador pode escrever; leitura apenas exige uma organização.
- Com logo oficial, use-a como ícone do plugin: uma versão quadrada e legível, em PNG ou JPEG, dentro de `cerebro/assets/`. Sem logo, fica o ícone padrão.

## Projetos que já existem

Leia o que existe antes de criar. Preserve caminhos, repositórios e políticas de Git que já funcionam. Para reorganizar, mostre o destino e os arquivos afetados e execute só a etapa autorizada.

- **Nome antigo:** uma pasta `.business-os/` é o Cérebro com o nome anterior e continua sendo lida. Para migrar, renomeie para `cerebro/` e rode `caixa.py iniciar`.
- **Site em subpasta:** no serviço de deploy, a raiz do projeto e os caminhos que disparam o build são configurações separadas; aponte as duas para `site/`.
