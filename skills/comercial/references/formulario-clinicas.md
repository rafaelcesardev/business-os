# Formulário de mapeamento para clínicas

Especificação do formulário que a clínica preenche depois de contratar. As respostas alimentam a skill, que gera os documentos de processo sem precisar de entrevista. Feito para clínicas médicas, odontológicas e de estética.

O objetivo é que a IA não tenha dúvidas ao montar o processo. Toda dúvida que se repetir entre clientes vira uma pergunta nova ou uma pergunta melhor aqui.

## Convenções

### Tipos de pergunta

| Tipo | Como aparece |
| --- | --- |
| `texto curto` | Uma linha |
| `texto longo` | Caixa de texto com **botão de voz**; a fala é transcrita |
| `número` | Campo numérico |
| `sim/não` | Dois botões |
| `única` | Escolha uma opção |
| `múltipla` | Escolha várias opções |
| `faixa` | Escolha uma faixa de valores |
| `horários` | Grade por dia da semana, com abertura e fechamento |
| `lista` | Grupo de campos que a pessoa repete quantas vezes precisar (um item por serviço, por exemplo) |
| `recomendação` | Mostra a recomendação e as opções "Concordo" e "Quero ajustar". "Quero ajustar" abre um `texto longo` |
| `arquivo` | Envio de arquivo |

### Regras para todas as perguntas

- Toda pergunta, menos 1.1 e 1.2, tem a opção **"Não sei / quero conversar sobre isso"**. Ela evita resposta inventada e entra na lista da reunião de validação.
- Perguntas abertas trazem um exemplo. Com exemplo, a resposta vem completa.
- "Mostrar se" usa o número da pergunta: `2.5 = Sim` quer dizer "só aparece se a resposta da 2.5 for Sim".
- "Alimenta" diz em que seção do documento de processo a resposta entra (veja [modelo-documento.md](modelo-documento.md)).
- O formulário é dividido nas seções abaixo, salva o progresso e mostra "Seção X de 9". A pessoa pode parar e voltar.
- Arquivos e prints não devem conter dados de pacientes. Avise isso no campo de envio.
- Recomendações são pontos de partida. Revise-as com os números reais de cada clínica.

## 1. A clínica

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Nome da clínica | `texto curto` | | | A empresa |
| 1.2 | Seu nome e sua função | `texto curto` + `única` | Dono ou sócio · Gestor · Recepção · Outro | | Papéis |
| 1.3 | Tipo de clínica | `múltipla` | Médica · Odontológica · Estética · Outra | | A empresa |
| 1.4 | Em que a clínica é especializada? | `texto longo` | Ex.: "Harmonização facial, depilação a laser e tratamentos corporais." | | A empresa |
| 1.5 | Unidades | `lista` | Por unidade: nome, endereço, ponto de referência, tem estacionamento (sim/não) | | A empresa; Perguntas frequentes |
| 1.6 | Dias e horários de funcionamento | `horários` | Um quadro por unidade | | A empresa; Agendamento |
| 1.7 | Quantos profissionais atendem pacientes? | `número` | | | A empresa |
| 1.8 | Como é o seu paciente típico? | `texto longo` | Ex.: "Mulheres de 30 a 55 anos que querem rejuvenescer sem cirurgia." | | Princípios do atendimento; Conversa |
| 1.9 | Por que os pacientes escolhem vocês e não outra clínica? | `texto longo` | Ex.: "Atendimento com hora marcada, sem espera, e a mesma profissional do início ao fim." | | Conversa |
| 1.10 | Vocês atendem convênio? | `única` | Só particular · Particular e convênio · Só convênio | | A empresa |
| 1.11 | Quais convênios? | `texto longo` | | 1.10 ≠ Só particular | A empresa; Perguntas frequentes |

## 2. Serviços e preços

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 2.1 | Serviços e procedimentos | `lista` | Por serviço: nome; para que serve, em uma frase; duração do atendimento; número de sessões normal; preço (valor fixo · a partir de · depende de avaliação); precisa de avaliação antes (sim/não); quem realiza. Ex.: "Limpeza de pele · remove cravos e impurezas · 1h · 1 sessão · R$ 180 · não · Ana" | | A empresa |
| 2.2 | Quais serviços vocês mais querem vender? | `múltipla` | Os itens da 2.1, até 3 | | Visão geral; Conversa |
| 2.3 | A primeira consulta ou avaliação é: | `única` | Gratuita · Paga (qual valor) · Não há avaliação | | A empresa; Etapa final |
| 2.4 | Formas de pagamento | `múltipla` | Pix · Dinheiro · Débito · Crédito à vista · Crédito parcelado (até quantas vezes) · Boleto · Financiamento | | A empresa; Perguntas frequentes |
| 2.5 | Vocês cobram sinal para reservar o horário? | `sim/não` | | | Etapa final; Agendamento |
| 2.6 | Como funciona o sinal? | `lista` | Por serviço: valor ou porcentagem; é devolvido se desmarcar com antecedência (sim, até quantas horas antes / não) | 2.5 = Sim | Etapa final; Agendamento |
| 2.7 | Política de cancelamento e remarcação | `recomendação` | "Remarcação sem custo até 24 horas antes. Depois disso, o sinal não é devolvido." | 2.5 = Sim | Agendamento |
| 2.8 | Política de cancelamento e remarcação | `texto longo` | Ex.: "Pode remarcar até 12 horas antes, sem custo." | 2.5 = Não | Agendamento |
| 2.9 | Pacotes, planos ou promoções em vigor | `texto longo` | Ex.: "Pacote de 10 sessões de laser com 15% de desconto, válido até dezembro." | | A empresa |

## 3. Como vocês atendem hoje

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 3.1 | De onde vêm os pacientes novos? | `múltipla` | Instagram · Anúncios · Google · Indicação · Convênio · Passam na frente · Outro | | Entrada |
| 3.2 | Por onde os pacientes falam com vocês? | `múltipla` | WhatsApp · Instagram Direct · Telefone · Site · Presencial | | Entrada |
| 3.3 | Quantos contatos novos chegam por mês, mais ou menos? | `faixa` | Até 50 · 51 a 150 · 151 a 300 · Mais de 300 | | Registro |
| 3.4 | Quem responde o WhatsApp hoje? | `texto curto` | Ex.: "A recepcionista, das 8h às 18h." | | Papéis |
| 3.5 | Quanto tempo leva a primeira resposta? | `faixa` | Poucos minutos · Até 1 hora · Algumas horas · No dia seguinte ou mais | | Registro |
| 3.6 | Onde vocês mais perdem pacientes? | `múltipla` | Demora para responder · Ninguém responde fora do horário · Some depois de saber o preço · Agenda e não comparece · Ninguém retoma quem não agendou · Outro | | Visão geral |
| 3.7 | De cada 10 contatos, quantos agendam? E quantos comparecem? | `número` + `número` | | | Registro |
| 3.8 | Onde fica a agenda? | `única` | Google Agenda · Sistema de clínica (qual) · Papel ou planilha · Outro | | Agendamento |
| 3.9 | Onde ficam os contatos dos pacientes? | `única` | No sistema da clínica · Só no WhatsApp · Planilha · Outro | | Registro |
| 3.10 | Materiais que ajudam a entender o atendimento | `arquivo` | Tabela de preços, roteiro da recepção, prints de conversas boas e ruins, sem dados de pacientes | | Todas |

## 4. Onde o atendimento precisa chegar

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 4.1 | Para um paciente novo, o atendimento está concluído quando: | `única` | Avaliação ou consulta agendada · Procedimento agendado · Sinal pago e horário reservado · Outro. Nota na tela: "Se o serviço precisa de avaliação, recomendamos que o fim seja a avaliação agendada." | | Etapa final |
| 4.2 | Quem marca o horário? | `recomendação` | "O assistente marca direto na agenda, oferecendo dois horários para o paciente escolher." Alternativas no ajuste: a recepção confirma · o assistente envia um link de agendamento | | Agendamento |
| 4.3 | O que o paciente precisa fazer antes de ter o horário garantido? | `múltipla` | Pagar sinal · Enviar fotos · Preencher cadastro · Trazer pedido médico · Nada | | Etapa final |

## 5. Agenda, confirmação e faltas

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 5.1 | Antecedência mínima para agendar | `recomendação` | "Aceitar agendamento até 2 horas antes, se houver horário livre." | | Agendamento |
| 5.2 | Até quantos dias à frente oferecer horários | `recomendação` | "Oferecer horários nos próximos 7 dias. Quanto mais longe o horário, maior a chance de falta." | | Agendamento |
| 5.3 | Confirmação | `recomendação` | "Pedir confirmação na véspera, tentar de novo no fim do dia e, sem resposta, manter o horário e avisar a recepção." | | Confirmação e lembretes |
| 5.4 | Lembrete | `recomendação` | "Lembrete 2 horas antes, com endereço e orientações de preparo." | | Confirmação e lembretes |
| 5.5 | Orientações de preparo por serviço | `lista` | Por serviço: orientação. Ex.: "Laser: não tomar sol 7 dias antes." Nota na tela: "O assistente só repassa as orientações escritas aqui; ele não cria orientações." | | Confirmação e lembretes |
| 5.6 | Tolerância de atraso, em minutos | `número` | | | Confirmação e lembretes; Perguntas frequentes |
| 5.7 | Faltas | `recomendação` | "Depois da 1ª falta, até 3 tentativas de remarcar. Depois da 2ª, uma mensagem deixando a porta aberta; o paciente volta quando quiser." | | Faltas |
| 5.8 | Lista de espera para encaixe | `recomendação` | "Quando alguém desmarca, oferecer o horário a quem pediu um horário mais cedo." | | Agendamento |

## 6. O assistente virtual

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 6.1 | Nome do assistente | `texto curto` | Ex.: "Lia". Nota na tela: "Ele sempre se apresenta como assistente virtual." | | Papéis; Princípios do atendimento |
| 6.2 | Quantos assistentes | `recomendação` | "Um assistente para pacientes novos e outro para quem já é paciente (reagendar, dúvidas depois do atendimento), porque têm objetivos diferentes." Alternativa no ajuste: um só para tudo | | Papéis |
| 6.3 | Tom das mensagens | `única` | Mais formal · Próximo e cordial · Descontraído | | Princípios do atendimento |
| 6.4 | Emojis | `única` | Não usar · Com moderação · À vontade | | Princípios do atendimento |
| 6.5 | Como chamar o paciente | `única` | Pelo primeiro nome · Senhor ou senhora · Depende da idade | | Princípios do atendimento |
| 6.6 | O assistente pode falar preço? | `recomendação` | "Informar o preço dos serviços com valor fixo. Nos que dependem de avaliação, explicar do que o valor depende e convidar para a avaliação." Alternativas no ajuste: nunca falar preço · falar só "a partir de" | | Princípios do atendimento; Conversa |
| 6.7 | Perguntas que os pacientes mais fazem, e a resposta de cada uma | `lista` | Pergunta e resposta. Já vem com sugestões para responder ou apagar: Onde fica? Tem estacionamento? Atende convênio? Parcela? Quanto tempo dura? Quantas sessões? Dói? Quando vejo resultado? Nota na tela: "Respostas sobre dor, resultado e cuidados devem ser aprovadas pelo profissional responsável." | | Perguntas frequentes |
| 6.8 | O que o assistente nunca deve dizer ou prometer | `múltipla` + `texto longo` | Já marcadas: prometer resultado de tratamento · dar diagnóstico · indicar medicamento · falar mal de outra clínica. Espaço para acrescentar | | Princípios do atendimento |
| 6.9 | Palavras que a clínica prefere ou evita | `texto longo` | Ex.: "Dizemos 'procedimento', nunca 'cirurgia'. Dizemos 'investimento', não 'preço'." | | Princípios do atendimento |
| 6.10 | Assuntos que sempre vão para uma pessoa | `múltipla` + `texto longo` | Já marcadas: avaliação de fotos · dúvida sobre medicação ou contraindicação · orçamento personalizado · reclamação · pedido para falar com alguém. Espaço para acrescentar | | Conversa |
| 6.11 | Quem assume quando o assistente passa a conversa | `lista` | Por pessoa: nome, função, WhatsApp, dias e horários | | Papéis |
| 6.12 | Em quanto tempo uma pessoa assume | `recomendação` | "Em até 1 hora no horário comercial. O assistente avisa o paciente desse prazo." | | Conversa |
| 6.13 | Urgências: dor forte, sangramento, reação depois de um procedimento | `recomendação` + `texto curto` | "O assistente orienta procurar atendimento de emergência ou ligar para o telefone de plantão e avisa a equipe na hora." Campo: telefone de plantão, se houver | | Conversa |
| 6.14 | Horário do assistente | `recomendação` | "Responde 24 horas. Mensagens que ele inicia (retomadas, lembretes) só saem em horário comercial." | | Princípios do atendimento |

## 7. Quem não responde ou não agenda

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 7.1 | Paciente pede informação e some | `recomendação` | "Retomar em até 5 tentativas: algumas horas depois e nos dias 1, 3, 6 e 10, a última como despedida. Cada mensagem traz algo novo." | | Primeiro contato |
| 7.2 | Paciente recebe o orçamento e não fecha | `recomendação` | "Retomar em 2, 7 e 30 dias, perguntando se ficou alguma dúvida." | | Quem não avança |
| 7.3 | Lista de retomada | `recomendação` | "Quem não agendou recebe um novo contato em 3 meses, a menos que tenha dito que não tem interesse." | | Quem não avança |
| 7.4 | Pacientes que a clínica não atende | `texto longo` | Ex.: "Menores de 18 anos sem responsável; procedimentos cirúrgicos." Nota na tela: "O assistente explica com educação e, se houver, indica outro serviço da clínica." | | Quem não avança |

## 8. Depois do atendimento

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 8.1 | Depois do procedimento | `recomendação` | "Uma mensagem no dia seguinte perguntando como o paciente está e, alguns dias depois, um pedido de avaliação no Google." | | Depois da etapa final |
| 8.2 | Serviços que o paciente repete de tempos em tempos | `lista` | Por serviço: a cada quanto tempo. Ex.: "Toxina botulínica, a cada 5 meses." | | Depois da etapa final |
| 8.3 | Pacientes que não voltam | `recomendação` | "Mandar uma mensagem para quem não volta há 6 meses." | | Depois da etapa final |
| 8.4 | Quem já é paciente quer reagendar, cancelar ou tirar dúvida | `única` | O assistente resolve · Passa para a recepção · O assistente resolve reagendamento e passa as dúvidas | | Depois da etapa final |

## 9. Números e fechamento

| # | Pergunta | Tipo | Opções, exemplo ou recomendação | Mostrar se | Alimenta |
| --- | --- | --- | --- | --- | --- |
| 9.1 | O que vocês querem acompanhar | `múltipla` | Já marcadas: contatos novos · tempo de resposta · agendamentos · comparecimentos · procedimentos realizados. Opcional: faturamento por origem do paciente | | Registro |
| 9.2 | Algo mais que devemos saber? | `texto longo` | | | Todas |
