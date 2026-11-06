---
name: comercial
description: "Organiza vendas e atendimento de uma empresa: processo comercial, oportunidades, orçamento, acompanhamento, suporte, pós-venda e atendentes com IA. Use para melhorar a conversão e a operação de atendimento, mapear o processo ou criar, revisar e testar instruções de um atendente na plataforma escolhida pelo cliente."
---

# Comercial

Entenda o que precisa acontecer entre o primeiro contato e o resultado esperado. Escolha o procedimento pelo problema descrito, sem exigir que o usuário conheça etapas, ferramentas ou nomes de skills.

## Contexto e escopo

Localize a empresa pelo [contexto compartilhado](../business-os/contexto.md). Leia `RESUMO.md`, a oferta, o público e os limites necessários. Reaproveite processos em `.business-os/processos/` e instruções em `.business-os/agentes/` antes de entrevistar novamente.

Se o problema é atrair público, produzir divulgação ou analisar anúncios, encaminhe a [Marketing](../marketing/SKILL.md). Se é vender, atender, acompanhar uma oportunidade ou resolver o pós-venda, conduza aqui. Em um pedido misto, encadeie o que for necessário sem pedir ao usuário que escolha a área.

## Procedimentos internos

| Pedido | Carregar quando necessário |
| --- | --- |
| Entender gargalos, etapas, responsáveis ou passagem para uma pessoa | [Mapear processo](references/mapear-processo-comercial.md) |
| Planejar, escrever, revisar ou testar instruções do atendente com IA | [Atendente com IA](references/criar-atendente-ia.md) |
| Escrever proposta, cobrança, resposta ou acompanhamento por e-mail | [E-mail compartilhado](../business-os/references/email-profissional.md) |
| Analisar vendas, atendimento, conversão ou dados da operação | [Análise compartilhada](../business-os/references/analisar-dados.md) |

São procedimentos internos. Leia somente o necessário e os recursos específicos que ele indicar. Para comunicação com clientes, use as regras e a voz da empresa; não transforme toda conversa em anúncio nem imponha um roteiro quando o pedido é apenas um e-mail.

## Decisões da área

- Mapear o processo não exige criar um agente de IA. Um agente pode usar o processo já aprovado; complete somente as lacunas que impedem as instruções ou os testes.
- Revisar um atendente preserva ferramentas, capacidades, regras de preço e passagem para pessoas, salvo mudança solicitada. Use o CRM ou plataforma contratada, sem presumir fornecedor nem inventar integrações.
- Acompanhar uma oportunidade ou cobrar um cliente é relação comercial. E-mail de divulgação para atrair interessados é [Marketing](../marketing/SKILL.md); ambos reutilizam o mesmo procedimento de e-mail.
- Análise identifica fatos, lacunas e hipóteses a partir dos dados disponíveis. Recomendar mudança de processo não equivale a alterar o CRM ou ativar automações.

## Entrega e limites

Rascunhos, revisões e resultados de testes ficam em `atendimento/`. Processos e instruções aprovados pertencem ao contexto conforme a [organização](../business-os/organizacao.md); uma revisão não substitui silenciosamente a versão aprovada.

Planejar, testar e implantar são ações distintas. Não envie mensagens, configure serviços ou publique um atendente apenas por ter preparado as instruções. Quando a implantação estiver autorizada, confira as capacidades reais da plataforma e siga o procedimento correspondente.

Informe o que foi entregue, o que foi executado e o que permanece sem teste. Sem acesso ao motor real, entregue instruções e cenários, sem declarar que o atendimento está validado em produção.
