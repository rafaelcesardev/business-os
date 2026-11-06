# Registrar e retomar trabalho

Use quando houver trabalho continuado, uma interrupção ou um pedido para continuar de onde parou. Não crie um registro de projeto para uma resposta simples já concluída. A referência de passagem entre sessões está em [fontes da gestão](fundamentos-gestao.md).

## Uma fonte de andamento

Encontre o negócio pelo [contexto compartilhado](../contexto.md). Leia `RESUMO.md`, `momento.md` e o caminho de acompanhamento registrado. Se o trabalho já estiver num CRM, quadro, documento ou sistema, use essa fonte. Sem acesso de escrita, entregue a atualização proposta; não inaugure um controle concorrente. Sem fonte existente, use `planejamento/andamento.md` na pasta do negócio, somente quando precisar salvar continuidade.

Registre em `momento.md` o apontador para o acompanhamento quando a atualização do contexto estiver autorizada, seguindo [alimentar contexto](../alimentar.md). Não copie todo o quadro para a base. Um plugin instalado pode conter somente o apontador de sua versão, não o estado atual.

## Ao registrar

Leia o registro existente e atualize o trabalho correspondente, preservando os demais. Use o identificador da ferramenta ou o título e escopo já adotados; não duplique uma iniciativa a cada conversa. Se não conseguir distinguir dois trabalhos, pergunte qual antes de alterar qualquer um.

Guarde apenas o necessário para outra sessão continuar:

```markdown
## Trabalho: <título existente>
Observado em: <data e fuso quando necessário>
Objetivo e escopo combinado: <resultado esperado e limites>
Fonte principal e arquivos: <registros e caminhos reais>
Concluído e verificado: <etapa, evidência e data; lacunas explícitas>
Estado atual: <situação observada e decisões com sua origem>
Próxima ação: <ação concreta, responsável e prazo conhecidos>
Pendências: <bloqueios, de quem depende e condição de retomada>
Resultado a conferir: <medida e momento combinado, quando pertinente>
```

Não preencha campos desconhecidos com nomes, datas ou aprovações plausíveis. Distinga combinado de proposto. Registre ações externas realizadas, ainda não executadas e de resultado incerto para evitar repetição. Não inclua credenciais ou conversas brutas; mantenha os materiais nas áreas próprias e cite sua origem. A [organização](../organizacao.md) define versionamento e backup.

Só afirme que uma ação anterior não foi executada quando a fonte confirmar isso. Sem registro, use “não comprovado”: uma próxima ação como obter um material não prova que ninguém já o solicitou. Você pode informar as ações que não realizou nesta sessão, sem estender essa afirmação ao histórico de outras pessoas.

## Ao retomar

1. Leia o registro mais recente do trabalho e as decisões que ele referencia, dentro da empresa correta.
2. Confira os arquivos e o estado real que podem ter mudado: tarefa, serviço, campanha, versão ou bloqueio. Um registro antigo orienta a consulta, não prova o estado atual nem concede uma autorização nova.
3. Identifique o que continua válido e o que divergiu. Preserve alterações de outras pessoas; resolva somente a ambiguidade que impedir a ação. Se faltar o material local ou acesso à fonte, informe a lacuna e recupere o necessário antes da ação dependente.
4. Continue pela próxima ação ainda necessária, dentro do pedido e da autorização existentes. Não repita entrega, envio ou publicação sem verificar o resultado anterior; diante de uma execução incerta, procure o registro no destino antes de tentar novamente.
5. Ao concluir uma etapa ou interromper o trabalho, atualize o mesmo registro. Separe conclusão da entrega de acompanhamento de resultado ainda pendente, usando [conferir resultados](conferir-resultados.md) quando pertinente.

Resuma o ponto de retomada, o avanço comprovado e a pendência restante. Não declare continuidade validada em outra máquina apenas porque o apontador está no Git: o conteúdo local depende de backup ou acesso à fonte.
