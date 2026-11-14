![Cortex](assets/readme.svg)

# Cortex

Cortex é um plugin para Codex e Claude Code que ajuda a organizar e usar o contexto de uma empresa no trabalho de marketing, vendas e atendimento. Serve para quem cuida do próprio negócio e para quem presta serviços a clientes.

Você descreve o que precisa em linguagem natural. O Cortex consulta as informações da empresa, aproveita os materiais existentes e escolhe os métodos adequados ao objetivo. Pergunta pelo que falta e mantém oferta, público, voz e limites como referência do trabalho.

## O que você pode fazer

O plugin tem quatro entradas. Você pode começar sempre pelo Cortex; Iniciar, Marketing e Comercial são atalhos opcionais.

| Entrada | O que faz | Exemplo de pedido |
| --- | --- | --- |
| [Iniciar](skills/iniciar/SKILL.md) | Cria o Cérebro de uma empresa na pasta atual e conduz a entrevista inicial | “Inicie o Cérebro desta empresa.” |
| [Cortex](skills/cortex/SKILL.md) | Mantém o Cérebro, revisa prioridades, retoma trabalhos e acompanha resultados | “Revise a semana da empresa e me ajude a escolher o próximo passo.” |
| [Marketing](skills/marketing/SKILL.md) | Ajuda a atrair clientes e apresentar a empresa com posicionamento, conteúdo, presença digital e anúncios | “Crie um carrossel com esta ideia e a nossa identidade.” |
| [Comercial](skills/comercial/SKILL.md) | Organiza a prospecção, o processo de venda, atendimento e trabalho dos atendentes com IA | “Analise estas conversas e encontre os problemas no atendimento.” |

**Marketing** reúne o [posicionamento](skills/marketing/references/posicionamento.md), criação e revisão do [manual da marca](skills/marketing/references/manual-da-marca.md), textos, legendas, roteiros, posts, carrosséis e artes; planejamento de sites e landing pages; SEO, Google Business Profile e respostas a avaliações; campanhas para Google, Instagram e Facebook; análise de anúncios e relatórios.

**Comercial** ajuda a montar a [prospecção](skills/comercial/references/prospeccao.md), mapear etapas, responsáveis e gargalos, preparar propostas e acompanhamentos, analisar vendas e atendimento e criar, revisar ou testar instruções de atendentes com IA na plataforma escolhida pela empresa.

E-mails e análise de dados são recursos compartilhados. O objetivo do pedido determina como usá-los, sem exigir que você conheça os procedimentos internos.

Para trabalho continuado, o Cortex consulta o andamento existente, registra o próximo passo e confere o que mudou antes de retomar. As revisões comparam compromissos e resultados com as evidências disponíveis. Uma entrega pode estar pronta enquanto seu efeito no negócio ainda aguarda dados. Veja as [fontes e escolhas desses procedimentos](skills/cortex/references/fundamentos-gestao.md).

## Para quem serve

- **Donos de negócio:** reunir o que a empresa sabe e usar essa base nas tarefas do dia a dia.
- **Profissionais e equipes:** trabalhar com oferta, público, identidade e processos aprovados em uma referência comum.
- **Prestadores de serviço e agências:** manter o contexto de cada cliente separado e reutilizar os mesmos métodos de trabalho.

## Como funciona

O Cortex é a caixa de ferramentas. O que ele cria e mantém para cada empresa é o **Cérebro**: uma pasta `cerebro/` com o contexto, as decisões, a marca, os processos e o conhecimento dela.

1. **Inicia o Cérebro.** Monta a estrutura padrão na pasta da empresa, aproveita documentos, site e conversas que já existem e completa as lacunas com uma entrevista guiada.
2. **Mantém o Cérebro.** Registra oferta, dados práticos, público, mensagem, marca, momento e histórico, com a origem de cada informação.
3. **Conduz o pedido.** Consulta só o contexto e os procedimentos necessários para a entrega, respeitando textos e decisões já aprovados.
4. **Entrega com verificação.** Informa o que foi produzido, o que foi testado e o que ainda falta.

O Cérebro não depende do Cortex para ser consultado: qualquer IA aberta na pasta da empresa o encontra pelo `AGENTS.md`, e a equipe pode instalá-lo como plugin. Os métodos ficam aqui; os dados ficam no repositório de cada empresa, sem se misturar.

## Instalar

### Pedir à sua IA

Copie para o Codex ou Claude Code com acesso ao computador:

```text
Instale neste ambiente o plugin Cortex a partir do repositório rafaelcesardev/cortex. O plugin e o marketplace se chamam cortex. Use as ferramentas disponíveis. Se alguma etapa depender de mim, me oriente. Confirme a instalação e explique como começar a usar.
```

Uma IA sem ferramentas de instalação poderá apenas orientar os passos.

### Usar o terminal

**Codex:**

```sh
codex plugin marketplace add rafaelcesardev/cortex
codex plugin add cortex@cortex
```

**Claude Code:**

```sh
claude plugin install cortex --marketplace rafaelcesardev/cortex
```

Requer a CLI atualizada. Abra uma conversa nova no Codex ou reinicie a sessão do Claude Code depois da instalação.

## Começar a usar

Abra a pasta da empresa no Codex ou Claude Code e chame `iniciar` (no Claude Code, `/cortex:iniciar`). Ou copie:

```text
Use o Cortex para iniciar o Cérebro desta empresa. Aproveite os materiais que já existem nesta pasta, pergunte o que faltar e me ajude a escolher o próximo passo conforme meu objetivo.
```

Com o Cérebro pronto, peça o trabalho diretamente: “Defina o nosso posicionamento”, “Crie o manual completo da nossa marca”, “Revise este texto com a nossa voz”, “Monte a prospecção para este serviço” ou “Organize o processo entre o primeiro contato e o fechamento”.

## Onde fica o trabalho

Cada empresa tem seu próprio repositório:

- **`cerebro/`:** o que está valendo e a equipe consulta: resumo, negócio, público, mensagem, marca, momento, histórico, processos, modelos e conhecimento. É também o plugin da empresa.
- **`site/`:** código do site.
- **`marketing/`, `comercial/`, `atendimento/`, `planejamento/`, `analises/`:** trabalho de cada área. Documentos de texto são versionados.
- **Fora do Git:** material bruto, vídeo, áudio, planilhas, pacotes gerados e segredos; precisam de backup próprio.

A equipe instala `cerebro/` como plugin de consulta, sem os métodos. Para só consultar, basta permissão de leitura no repositório. Veja os detalhes em [organização](skills/cortex/organizacao.md).

## O que uma entrega inclui

O trabalho segue os dados e as provas disponíveis. Informações desconhecidas são tratadas como lacunas; hipóteses ficam identificadas. Resultados, depoimentos e capacidades de ferramentas precisam de evidência.

A entrega depende do pedido e das ferramentas disponíveis: planejamento de site entrega o plano; roteiro entrega as cenas e as falas. Produção de mídia, publicação, configuração de serviços e implantação de atendentes exigem os recursos e a autorização correspondentes. Preparar um material não comprova sua publicação nem seu funcionamento em produção.

## Verificar o projeto

Os scripts que montam e conferem o Cérebro usam a biblioteca padrão do Python. Para rodar os testes:

```sh
python3 -m unittest discover -s tests -v
```

Os [15 cenários de gestão](tests/cenarios-gestao.md) também têm um [executor para as CLIs reais](tests/avaliar_gestao.py), com empresas e serviços fictícios. Veja os [resultados, correções e limites da validação](tests/validacao-gestao.md).

## Licença

[MIT](LICENSE).
