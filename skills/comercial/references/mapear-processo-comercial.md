# Mapear processo comercial

Para localizar a empresa e usar contexto local ou fornecido por um plugin, siga [contexto do negócio](../../business-os/contexto.md).

## Contexto e local dos arquivos

Localize a pasta do negócio como na skill [business-os](../../business-os/SKILL.md). Leia `.business-os/RESUMO.md`, `negocio.md`, `publico.md` e os limites em `mensagem.md` antes de perguntar. Use o que já foi informado. Os processos aprovados ficam em `.business-os/processos/`; rascunhos e revisões ficam em `atendimento/processos/`, local e ignorado pelo Git. Siga [organização](../../business-os/organizacao.md) para promover uma versão aprovada, atualizar referências e manter uma única fonte principal. Reutilize pastas legadas `processos/` sem movê-las automaticamente.

Você conduz a pessoa que precisa do mapeamento: o dono, um gestor ou alguém respondendo em nome da empresa. Fale com ela como quem vai ajudar a empresa dela; não presuma quem ela é além do que ela contar.

O resultado é um processo que pessoas e agentes de IA conseguem seguir. Um processo mapeado aumenta muito a chance de cada conversa terminar onde a empresa precisa, porque todo atendimento passa a saber para onde está indo.

## Dois modos

- **Entrevista:** a pessoa conversa com você. É o padrão; siga os passos abaixo.
- **Formulário:** a pessoa traz as respostas do [formulário de mapeamento para clínicas](formulario-clinicas.md), coladas ou em arquivo. Vá para [Modo formulário](#modo-formulário).

## Como trabalhar

### 1. Abra e situe

Explique em poucas linhas o que vai acontecer: algumas rodadas de perguntas, recomendações quando houver uma boa prática conhecida e, no fim, um documento salvo na área de atendimento do negócio.

Antes de perguntar, procure os aprovados em `.business-os/processos/` e o trabalho em `atendimento/processos/`. Se já existir um processo, leia e trabalhe a partir dele: a pessoa pode querer revisar, não recomeçar.

### 2. Entenda a empresa

Pergunte o essencial: o que vende, para quem, ticket médio, canais de atendimento, quem atende hoje, ferramentas (agenda, sistema de contatos) e horários. Use o bloco "A empresa" de [roteiro-de-perguntas.md](roteiro-de-perguntas.md).

### 3. Comece pelo fim

Liste os processos que a empresa precisa (vendas, agendamento, suporte, pós-venda) e, para cada um, a **etapa final**: o momento em que aquele processo está concluído. Exemplos: call de vendas marcada, procedimento agendado, sinal pago, problema resolvido.

Tudo se organiza em volta da etapa final. Sem ela definida, não há como saber se uma resposta avança ou só enrola. Mapeie um processo por vez, começando pelo mais perto da receita.

Se o pedido incluir atendentes de IA, identifique seus papéis e complete os nomes ou a divisão de agentes quando isso for necessário ao projeto. Um mapeamento feito para pessoas não exige definir agentes nem automatizar o processo.

### 4. Volte do fim para o começo

Faça rodadas de perguntas indo da etapa final até a chegada do contato: o compromisso e suas regras, confirmação e faltas, a conversa, o primeiro contato e o follow-up, a entrada (anúncio, formulário, indicação), quem não tem perfil e o que acontece depois da etapa final. A ordem e as perguntas estão em [roteiro-de-perguntas.md](roteiro-de-perguntas.md).

Em cada rodada:

- **Comece com "O que entendi até aqui"**, curto, para a pessoa corrigir antes de seguir.
- **No máximo 6 perguntas**, numeradas, com o motivo quando não for óbvio.
- **Traga uma recomendação** quando houver boa prática conhecida, e deixe a pessoa decidir. Diferencie evidência de folclore de mercado: se citar estudo, diga o que ele mede e de quando é.
- **Não preencha lacunas com suposição.** O que a pessoa não decidiu vira "a confirmar" ou entra nas pendências.
- **Pergunte as decisões que mudam de empresa para empresa**: quem informa preço, horários, responsáveis e regras de passagem. Nome, identidade e divisão de agentes só entram se atendimento com IA fizer parte do pedido.

### 5. Aplique os padrões universais

Leia [padroes-universais.md](padroes-universais.md) antes da primeira rodada. Os padrões valem para toda empresa e entram no documento sem precisar de aprovação; só os pontos marcados como decisão da empresa viram pergunta.

Enquanto houver um próximo passo pertinente, conduza a conversa com uma pergunta que avance. Respeite encerramento, recusa e pedido para parar; a conversa tem início, meio e fim.

### 6. Escreva o documento

Quando a pessoa disser que está bom, ou quando as rodadas não trouxerem mais nada novo, escreva o documento seguindo [modelo-documento.md](modelo-documento.md).

- Salve em `atendimento/processos/<processo>.md` na raiz do negócio, com o nome do processo em minúsculas e sem acento: `atendimento/processos/vendas.md`, `atendimento/processos/suporte.md`.
- Use Markdown com fluxos em Mermaid. O documento será lido por pessoas e por IAs, inclusive para gerar simulações visuais; seja literal e completo.
- Inclua casos de uso suficientes para testar cada caminho do fluxo, inclusive os ruins: quem não responde, quem falta, quem não tem perfil.
- Se puder, valide a sintaxe dos blocos Mermaid antes de entregar.
- Após aprovação do responsável, promova o documento para `.business-os/processos/<processo>.md`, registre a aprovação e atualize os consumidores. Criar o rascunho não equivale a aprová-lo ou implantá-lo.

### 7. Feche

Diga onde salvou, resuma em poucas linhas o processo, liste as pendências e pergunte qual processo mapear em seguida. Se o processo vai ser atendido por um agente de IA, ofereça também escrever e testar o prompt dele com o procedimento [criar-atendente-ia](criar-atendente-ia.md). Esse fechamento segue o mesmo padrão que o documento ensina: termina com uma pergunta que leva ao próximo passo.

## Modo formulário

As respostas já cobrem as rodadas de perguntas. Não reabra a entrevista; transforme as respostas em processo e junte o que faltou para a reunião de validação.

1. **Leia todas as respostas e os arquivos enviados.** A coluna "Alimenta" do [formulário](formulario-clinicas.md) diz em que seção do documento cada resposta entra.
2. **Aplique os padrões universais.** Recomendação com "Concordo" vira regra como está escrita. Com "Quero ajustar", vale o texto da clínica.
3. **Escreva os documentos** como no passo 6, um por processo: em geral `atendimento/processos/novos-pacientes.md` e, se a clínica quiser um assistente para quem já é paciente (pergunta 6.2), `atendimento/processos/pacientes.md`. A seção "A empresa" e as perguntas frequentes vêm das seções 1, 2 e 6 do formulário.
4. **Monte os pontos para a reunião de validação**, na seção "Pendências" de cada documento:
   - respostas "Não sei / quero conversar sobre isso";
   - respostas vagas, que não viram regra;
   - respostas que se contradizem;
   - ajustes que vão contra um padrão universal (por exemplo, pedir que o assistente indique medicamento). Explique o risco e proponha o caminho seguro.
5. **Responda com** onde salvou, um resumo curto do processo, os pontos para a reunião de validação e as **melhorias sugeridas para o formulário**: cada dúvida que uma pergunta melhor teria evitado vira uma sugestão de pergunta nova ou reescrita. É assim que o formulário melhora a cada cliente.

## Referências do negócio

Use os processos já existentes do negócio como referência de estrutura e decisões. Os exemplos de clínicas do formulário só se aplicam quando o negócio for uma clínica; não restringem o método a esse setor. Não importe preços, nomes, políticas ou objetivos de outra empresa.
