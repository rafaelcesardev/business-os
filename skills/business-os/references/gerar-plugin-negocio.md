# Gerar plugin do negócio

Para localizar a empresa e usar contexto local ou fornecido por um plugin, siga [contexto do negócio](../contexto.md).

Entregue uma versão consultável do contexto da empresa. O plugin contém uma skill de contexto e as informações do negócio; os métodos continuam no Business OS.

## 1. Escolha a forma de entrega

O padrão é o **próprio repositório**: `.business-os/` continua sendo a única base editável e também é a raiz do plugin. Os catálogos Codex e Claude Code, na raiz do repositório, apontam para ela. Prepare os manifestos e a skill seguindo [plugin no próprio repositório](repositorio-plugin.md); não copie os documentos para outra pasta.

Prepare também o README da empresa a partir do [modelo padrão](../modelo-readme.md): finalidade, prompt copiável de instalação para leigos, comandos, estrutura atual e referência ao Business OS para gerenciamento. Use a origem real do repositório; não inclua links de instalação nem histórico de migração. O fluxo de criação de um negócio novo chama esta preparação por padrão; publicação, instalação e concessão de acesso continuam sendo ações separadas.

O repositório privado exige acesso de leitura de quem instala. Compartilhar o repositório dá acesso a seus arquivos e histórico, inclusive ao site; não é uma permissão limitada à pasta de contexto. Não crie acesso, publique nem altere a visibilidade sem instrução do usuário.

Use o exportador abaixo somente quando pedirem um ZIP ou quando o destinatário deva receber apenas uma seleção. Esse pacote é uma saída regenerável, não outra base editada em paralelo. `compartilhar.json` filtra o exportador; não filtra a instalação pelo repositório.

## 2. Exportação opcional: contexto e seleção

Localize a pasta do negócio e leia `.business-os/RESUMO.md`. Reaproveite o contexto já existente. Se estiver incompleto, identifique as lacunas; não invente informações para preencher o pacote.

Revise quais arquivos são destinados ao dono ou à equipe. Registre a seleção em `.business-os/compartilhar.json`, seguindo o [modelo](compartilhar.exemplo.json). Os caminhos são relativos à base de contexto. `RESUMO.md` é obrigatório; outros arquivos e recursos entram apenas quando declarados.

Não copie a pasta inteira. Fontes brutas, credenciais, arquivos ocultos e dados de outros negócios não pertencem à entrega. O exportador bloqueia caminhos fora da base, links simbólicos, fontes brutas e tipos executáveis; ele não substitui a revisão do conteúdo de cada arquivo selecionado.

Quando houver logo oficial, inclua o arquivo apropriado na seleção e informe seu caminho no campo opcional `logo` de `compartilhar.json`. O gerador usa esse mesmo recurso no ícone do Codex e do Claude Code. Para compatibilidade, prepare PNG ou JPEG legível em formato quadrado, preservando o desenho da marca. Sem logo, mantenha o ícone padrão; não invente uma marca nem use a de outra empresa.

Links locais de Markdown precisam apontar para arquivos também selecionados. Quando a prova só puder ficar numa fonte privada, use no contexto uma referência textual à fonte e explicite que ela não acompanha o pacote; não apresente um link quebrado como arquivo disponível ao dono.

## 3. Gerar o pacote separado

Execute o [exportador](../scripts/gerar_plugin.py), dentro da skill Business OS, com a pasta do negócio:

```sh
python3 <pasta-business-os>/scripts/gerar_plugin.py <pasta-do-negocio>
```

Use o caminho real da pasta da skill Business OS no ambiente atual, não a pasta `references/`. O script usa apenas a biblioteca padrão do Python.

A saída fica em `entregas/plugins/<nome>/<versao>/`, com um ZIP ao lado. O pacote usa `plugin.json` na raiz, componentes em `skills/` e manifestos de compatibilidade para Codex e Claude Code. Confira o [formato portátil oficial](https://developers.openai.com/plugins/build/plugins) quando mudar o empacotamento.

A mesma entrada pode ser executada de novo. Se o conteúdo mudou, use uma nova versão; o script não sobrescreve uma versão diferente que já exista. Uma falha não deve apagar o contexto ou as versões anteriores.

## 4. Verificar e entregar

Confira os fatos e faça perguntas de teste sobre oferta, público, voz e lacunas usando somente os arquivos do pacote. Verifique também uma pergunta que o contexto não responde: a resposta deve reconhecer a lacuna.

Informe origem, versão e arquivos incluídos. A pasta principal é a fonte editável; uma cópia instalada não é atualizada automaticamente quando a base muda. No modo repositório, revise a base e incremente a versão coerentemente nos manifestos; no modo exportação, gere outro pacote. Atualizar o marketplace e o plugin instalado é uma etapa separada, a conferir em cada cliente.

O pacote local não equivale a publicação ou instalação. Para ChatGPT, Codex ou outro ambiente, confira o mecanismo de importação e compartilhamento disponível à conta e teste com o destinatário antes de afirmar compatibilidade de ponta a ponta. Não publique nem compartilhe dados com terceiros apenas porque o ZIP foi criado.
