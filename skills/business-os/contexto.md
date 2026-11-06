# Localizar e usar o contexto do negócio

Este protocolo serve aos métodos chamados diretamente e ao ponto de entrada do Business OS.

## Fonte do contexto

1. Procure `.business-os/` na pasta atual e nos pais. A pasta que a contém é a raiz do negócio; leia `RESUMO.md` e depois os arquivos pertinentes à tarefa. Liste também a pasta do negócio fora de `.business-os/` para achar dados, notas e registros da tarefa; não afirme que um registro falta sem procurá-lo.
2. Um plugin da empresa, selecionado ou fornecido pelo usuário, também pode fornecer o contexto. Leia seu resumo e referências e identifique a empresa e a versão. Não exija criar outra pasta só para voltar a obter os mesmos fatos.
3. Havendo base principal e pacote do mesmo negócio, use a base principal para manutenção. Se houver informação conflitante ou não estiver claro qual vale para a tarefa, mostre o conflito e peça a decisão necessária.
4. Sem nenhuma fonte de contexto, aproveite o que o usuário informou e pergunte apenas o que afeta a entrega. Para um levantamento completo, use [criar contexto](criar.md). Não preencha lacunas com dados de outra empresa.

As instruções dos métodos sobre arquivos de `.business-os/` se referem à base principal. Quando a fonte for um plugin da empresa, consulte os arquivos equivalentes disponíveis nele, sem presumir que ele tenha o mesmo caminho físico no disco.

## Saídas e atualização

Use a pasta do negócio e os caminhos registrados no resumo. Se só houver um plugin de contexto e o destino dos arquivos ainda estiver ambíguo, defina a pasta de trabalho com o usuário. Nunca grave uma entrega no cache do plugin ou dentro de seus arquivos de referência.

No negócio novo, as áreas são `marketing/`, `site/`, `atendimento/`, `entregas/` e `tmp/`; veja [organização](organizacao.md). Recrie as áreas locais necessárias ao retomar um clone. O Git guarda a base revisada e o site; produção e rascunhos ficam locais. Processos e instruções aprovados têm sua fonte principal na base de contexto. Preserve caminhos existentes quando forem adequados à tarefa.

Para atualizar fatos, trabalhe na fonte principal e registre a origem. A entrega instalada é uma versão; editar a cópia do cache cria uma base paralela e não atualiza automaticamente os outros destinatários. Gere uma versão nova quando uma nova entrega for solicitada.
