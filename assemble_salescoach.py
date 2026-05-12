import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/sorna/Documents/germinare-supabase/data_chats.json', 'r', encoding='utf-8') as f:
    chats_raw = json.load(f)

chats_index = {c['chat']: c for c in chats_raw}

evals = {
  "Fabricio": {
    "score": 5.5,"scoreLabel": "Proativo porém pouco técnico",
    "summary": "O vendedor demonstra grande volume de contatos e proatividade na região, mas falha em seguir o processo de formalização de BIDs. A negociação está travada devido a uma lacuna de preço entre o alvo do cliente e a oferta disponível.",
    "status": "Em andamento","vendedor": "Fabricio","produto": "DDGs",
    "metrics": {"respostaMed": "6min","objecoes": "2","conversao": "Não","msgs": "61"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Mapeamento de demanda","text": "O vendedor mapeou diversos clientes na mesma região (Patos de Minas/Paracatu), facilitando logística e escala.","tip": "Continue agrupando demandas regionais para barganhar fretes melhores com o fornecedor.","msgRef": "tenho 3 a 4 vendas em negociação"},
      {"type": "warn","label": "⚠️ Atenção","title": "Qualificação do BID","text": "O vendedor tenta obter preços sem passar os parâmetros básicos (volume, prazo, mês).","tip": "Use um checklist (Produto, Volume, Preço Alvo, Prazo, Embarque) antes de acionar o broker.","msgRef": "vou perguntar"},
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Ancoragem de Preço","text": "Fabricio baseou a negociação no preço da cooperativa, perdendo a margem de manobra do broker.","tip": "Não prometa o preço da cooperativa; foque no diferencial de entrega ou disponibilidade que a Germinare oferece.","msgRef": "preco que dei foi o que a cooperativa cobra"}
    ],
    "objecoes": [
      {"objecao": "Diferença de preço (Cliente quer 212, Fornecedor quer 220).","resposta_dada": "Vou tentar convencer o cliente.","resposta_ideal": "Justificar que o DDGs de 42% PB tem maior valor nutricional que o da cooperativa, ou que a disponibilidade para dezembro está escassa, justificando o prêmio de R$ 8,00."},
      {"objecao": "BID incompleto — sem mês de embarque e prazo de pagamento.","resposta_dada": "Entendido, vou perguntar.","resposta_ideal": "Chegar com formulário de BID preenchido para dar agilidade e seriedade à negociação."}
    ],
    "followupMsg": "Fulano, verifiquei aqui e o mercado de DDGs para dezembro apertou bastante. Consegui segurar essa carga de 220 em Paranaguá por pouco tempo. Considerando a proteína de 42%, seu custo por ponto de proteína ainda sai melhor que o da cooperativa. Fechamos as 200 toneladas para garantir seu embarque agora?"
  },
  "Bioma Trading | Germinare": {
    "score": 6.5,"scoreLabel": "Agilidade boa, condução passiva",
    "summary": "A vendedora foi extremamente rápida na resposta e na busca pela cotação. No entanto, faltou qualificar o volume da demanda e ser mais proativa na abordagem direta ao cliente final.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "Casca de Soja",
    "metrics": {"respostaMed": "1min","objecoes": "0","conversao": "Parcial","msgs": "17"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Velocidade de resposta","text": "Vanessa respondeu quase instantaneamente, crucial no mercado de grãos onde os preços oscilam rápido.","tip": "Mantenha esse tempo de resposta, pois transmite confiança ao parceiro que traz o BID.","msgRef": "pesquisei aqui"},
      {"type": "warn","label": "⚠️ Atenção","title": "Falta de Qualificação","text": "A vendedora não perguntou o volume pretendido para agosto, dado essencial para negociar com o fornecedor.","tip": "Antes de consultar o fornecedor, pergunte sempre o volume e a forma de pagamento.","msgRef": "melhor oferta que tenho"},
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Postura Reativa","text": "Vanessa deixou que a Cinthia fizesse a ponte de volta, perdendo o controle da negociação com o Rodrigo.","tip": "Tome a frente: diga que vai ligar para o Rodrigo imediatamente para defender o preço e fechar a ponta.","msgRef": "vou passar para o Rodrigo"}
    ],
    "objecoes": [],
    "followupMsg": "Cinthia, conseguiu falar com o Rodrigo sobre os R$ 185? Se o volume dele for fechado (ex: 30+ ton), consigo tentar um fôlego no prazo com o fornecedor. Quer que eu ligue direto para ele agora para agilizar?"
  },
  "Muriel": {
    "score": 5.5,"scoreLabel": "Atendimento reativo e passivo",
    "summary": "A vendedora agiu como informante de preços, sem contestar a oferta menor do concorrente ou buscar alternativas de fechamento imediato. A negociação estagnou na dependência de cotações futuras.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "DDGs",
    "metrics": {"respostaMed": "2min","objecoes": "1","conversao": "Não","msgs": "16"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Agilidade no retorno","text": "A vendedora manteve um fluxo de resposta rápido, essencial no mercado spot de grãos.","tip": "Continue com esse tempo de resposta, mas adicione perguntas qualificadoras em cada interação.","msgRef": "Pode mandar sim"},
      {"type": "warn","label": "⚠️ Atenção","title": "Aceitação passiva de preço","text": "Ao ouvir que o concorrente estava R$3 abaixo, a vendedora não defendeu sua margem ou questionou a origem/qualidade.","tip": "Questione se o preço do concorrente inclui impostos, qual a proteína e se a retirada é imediata.","msgRef": "trabalhando hoje ta 228"},
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Falta de Fechamento","text": "A conversa terminou com uma promessa de 'vou ver', transferindo o controle da negociação para o comprador.","tip": "Trave o cliente no que você tem agora (Jul/Ago) antes de buscar meses futuros, ou condicione a busca de Outubro ao fechamento imediato.","msgRef": "vou ver e te retorno"}
    ],
    "objecoes": [
      {"objecao": "Preço do concorrente a R$225 contra R$228 da Vanessa.","resposta_dada": "Apenas confirmou o próprio preço e especulou sobre a origem do outro.","resposta_ideal": "Entendo o preço de 225, mas esse volume é garantido? O meu de 228 é de usina com carregamento prioritário. Se eu conseguir 227 fechamos agora?"}
    ],
    "followupMsg": "Muriel, verifiquei aqui: para Out/Nov as usinas estão segurando oferta, mas consegui uma brecha. Sobre os 225 que você viu para Jul/Ago, confirmou se é DDG ou WDG? O meu de 228 é padrão ouro. Consigo tentar 227 se fecharmos a carga agora para garantir o frete. O que acha?"
  },
  "Paulo Consultoria": {
    "score": 5.5,"scoreLabel": "Acompanhamento reativo e passivo",
    "summary": "A vendedora realizou o follow-up de um BID prometido, mas aceitou passivamente o adiamento por motivos de saúde do cliente, perdendo o controle do timing da negociação.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "DDGs",
    "metrics": {"respostaMed": "9min","objecoes": "1","conversao": "Não","msgs": "16"},
    "improvements": [
      {"type": "warn","label": "⚠️ Atenção","title": "Escassez sem justificativa","text": "Vanessa mencionou a necessidade de fechar na semana, mas não deu um motivo comercial (alta de preços ou fim de lote).","tip": "Sempre vincule a urgência a um fator de mercado, como 'a usina vai subir a tabela' ou 'o frete está subindo'.","msgRef": "precisamos fechar essa semana"},
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Encerramento Passivo","text": "Ao dizer 'qualquer coisa pode chamar', a vendedora transfere a responsabilidade do próximo passo para o comprador.","tip": "Mantenha o controle da agenda. Em vez de esperar, defina você o horário do próximo contato.","msgRef": "qualquer coisa pode chamar"}
    ],
    "objecoes": [
      {"objecao": "Crise de sinusite e adiamento do BID para o dia seguinte.","resposta_dada": "Aceitou o prazo e desejou melhoras de forma simples.","resposta_ideal": "Desejar melhoras e perguntar se os parâmetros (volume e preço alvo) já estão definidos para ir consultando o fornecedor informalmente."}
    ],
    "followupMsg": "Bom dia, Paulo! Espero que já esteja se sentindo melhor. Conseguiu levantar os números do BID de DDGs? O volume para dezembro está rodando rápido e quero garantir sua prioridade com a usina antes da virada de preço."
  },
  "g | risk": {
    "score": 9.5,"scoreLabel": "Fechamento rápido e objetivo",
    "summary": "A vendedora Vanessa apresentou uma oferta oportuna de DDGs e conduziu a negociação de forma extremamente ágil. O fechamento de 200 toneladas ocorreu em menos de 30 minutos.",
    "status": "Fechado","vendedor": "Vanessa","produto": "DDGs 42% PB",
    "metrics": {"respostaMed": "3min","objecoes": "0","conversao": "Sim","msgs": "15"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Proatividade Comercial","text": "A vendedora iniciou o contato com uma oportunidade específica (DDGs 42% PB) e preço C/F, acelerando a tomada de decisão.","tip": "Continue utilizando ofertas com 'gancho' de oportunidade/novidade para gerar senso de urgência no comprador.","msgRef": "Trago uma novidade"},
      {"type": "warn","label": "⚠️ Atenção","title": "Alinhamento de Condições","text": "O fechamento foi rápido, mas não houve menção explícita ao prazo de pagamento antes do contrato.","tip": "Sempre confirme o prazo de pagamento no chat antes de gerar o contrato para evitar retrabalho jurídico.","msgRef": "preparar contrato"}
    ],
    "objecoes": [],
    "followupMsg": "Oi g | risk, contrato enviado para o seu e-mail! Consegue me confirmar o recebimento e se a assinatura sai ainda hoje para garantirmos a logística de dezembro?"
  },
  "Turma do DDGs": {
    "score": 7.5,"scoreLabel": "Prospecção ágil e estruturada",
    "summary": "Vanessa apresentou uma oferta completa e técnica de DDGs, gerando interesse imediato. Contudo, ignorou a objeção de preço de um dos participantes, focando apenas no lead mais quente.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "DDGs Inpasa",
    "metrics": {"respostaMed": "1min","objecoes": "1","conversao": "Parcial","msgs": "13"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Oferta Técnica Completa","text": "Vanessa enviou todos os parâmetros necessários (volume, preço, prazo, PB e umidade) de uma só vez, agilizando a decisão.","tip": "Continue padronizando a oferta com o padrão técnico (PB/Umidade), pois isso reduz o tempo de perguntas.","msgRef": "42% PB, 10% umidade"},
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Objeção de Preço Ignorada","text": "O vendedor Fabricio sinalizou que o preço está alto, e a Vanessa não tentou entender o target dele ou contra-argumentar.","tip": "Sempre que houver objeção de preço, pergunte o BID alvo. Como broker, você precisa desse dado para negociar com o fornecedor.","msgRef": "meus clientes precisam de preco menor"}
    ],
    "objecoes": [
      {"objecao": "meus clientes precisam de preco menor","resposta_dada": "Nenhuma. A vendedora ignorou a mensagem e focou no outro parceiro.","resposta_ideal": "Fabricio, entendo. Qual o BID (preço alvo) que eles estão trabalhando hoje? Se tivermos volume, posso tentar brigar por um desconto no lote com a Inpasa."}
    ],
    "followupMsg": "Fabricio, voltando aqui: qual o preço alvo (BID) que seus clientes estão buscando para esse DDGs de dezembro? Me passa o valor e o volume que eu tento buscar uma flexibilidade no fornecedor agora."
  },
  "Wilson Mkt": {
    "score": 6.8,"scoreLabel": "Proativa, mas pouco persuasiva",
    "summary": "Vendedora iniciou oferta ativa de DDGs com clareza técnica, mas a negociação estagnou após o cliente questionar o custo do frete. Falta contorno de objeção comparativo.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "DDGs 42% PB",
    "metrics": {"respostaMed": "10min","objecoes": "1","conversao": "Parcial","msgs": "11"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Qualificação do Produto","text": "A vendedora foi direta informando a proteína (42% PB) e o preço por tonelada.","tip": "Continue especificando o teor de proteína, pois no DDG isso é o principal driver de valor.","msgRef": "DDGs 42% PB a R$ 228"},
      {"type": "warn","label": "⚠️ Atenção","title": "Passividade no Frete","text": "Ao passar um frete alto (R$130/ton), a vendedora apenas entregou o número sem justificar o benefício.","tip": "Antes de passar o preço final, mencione a disponibilidade imediata ou a qualidade superior do lote para amortecer o impacto do frete.","msgRef": "seria em torno de R$ 358"},
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Contorno de Objeção","text": "O cliente deu um sinal claro de interesse ao perguntar sobre o preço no MT, mas a conversa parou na queixa do valor alto.","tip": "Mostre que o custo por ponto de proteína (PB) pode ser mais barato que o farelo local mesmo com o frete.","msgRef": "Nossa.. bem alto"}
    ],
    "objecoes": [
      {"objecao": "Custo de frete elevado para Rondonópolis/MT.","resposta_dada": "A vendedora apenas informou o valor total sem argumentação adicional.","resposta_ideal": "Entendo que o frete assusta, Wilson, mas esse lote de 42% PB tem digestibilidade acima da média. Se compararmos o custo da proteína posta aí com o farelo de soja local, o DDG ainda economiza sua dieta. Qual seria seu preço alvo para fecharmos uma carreta teste?"}
    ],
    "followupMsg": "Wilson, estou consultando agora as usinas do Mato Grosso para comparar. Mas me diga: para o seu formulador, qual o nível máximo de fibra que você aceita? Esse lote de Patos de Minas é padrão exportação. Se eu conseguir baixar R$10,00 na tonelada, a gente fecha?"
  },
  "Leonardo Campos l Bioma Trading": {
    "score": 5.5,"scoreLabel": "Prospecção Ativa, Condução Passiva",
    "summary": "A vendedora iniciou bem com uma oferta ativa, mas perdeu o controle da negociação ao demonstrar passividade frente à demanda do cliente. Faltou qualificação de volume e senso de urgência para buscar o BID de Casca de Soja.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "DDGs 42% PB e Casca de Soja",
    "metrics": {"respostaMed": "1min","objecoes": "1","conversao": "Não","msgs": "10"},
    "improvements": [
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Postura Reativa no Brokerage","text": "Ao dizer 'posso pesquisar se precisar', a vendedora transfere a iniciativa para o comprador, fatal no mercado de grãos.","tip": "Substitua por proatividade: 'Vou pesquisar agora as melhores ofertas de casca para agosto e te retorno em 20 minutos. Qual volume você projeta?'","msgRef": "posso pesquisar se precisar"},
      {"type": "warn","label": "⚠️ Atenção","title": "Falta de Qualificação de BID","text": "O cliente aceitou a janela de agosto para DDGs, mas a vendedora não perguntou o volume nem o destino.","tip": "Sempre que o cliente confirmar interesse, peça imediatamente: Volume, Destino e Prazo de Pagamento.","msgRef": "pode ser pra agosto sim"},
      {"type": "good","label": "✅ Ponto Forte","title": "Agilidade e Oferta Clara","text": "A vendedora foi rápida nas respostas e iniciou o contato com uma oferta muito específica (PB, Preço, Local).","tip": "Mantenha esse padrão de abertura, pois facilita a tomada de decisão do comprador.","msgRef": "DDGs 42% PB a R$ 228,00"}
    ],
    "objecoes": [
      {"objecao": "Necessidade de produto complementar (Casca de Soja) e janela futura (Agosto).","resposta_dada": "Informou que não tinha oferta boa no momento e que poderia pesquisar se ele quisesse.","resposta_ideal": "Informar que buscaria imediatamente no mercado para montar um pacote (DDGs + Casca) visando otimizar o frete para o cliente."}
    ],
    "followupMsg": "Leonardo, já estou consultando meus fornecedores aqui para a Casca de Soja em agosto para te passar a melhor ponta. Para eu fechar o BID completo com os DDGs para você, qual o volume que você está precisando para esse período? Se fecharmos o pacote, consigo apertar a margem com o fornecedor."
  },
  "Central Rede | Germinare": {
    "score": 8.5,"scoreLabel": "Prospecção direta e resolutiva",
    "summary": "O vendedor iniciou o contato com uma oferta técnica completa e específica, gerando interesse imediato. A conversa evoluiu rapidamente para uma chamada telefônica, o que é positivo para o fechamento.",
    "status": "Em andamento","vendedor": "Leandro","produto": "DDGs Inpasa 42% PB",
    "metrics": {"respostaMed": "2min","objecoes": "1","conversao": "Parcial","msgs": "9"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Abordagem Técnica Direta","text": "O vendedor enviou todas as especificações essenciais (origem, volume, preço, prazo e proteína) em uma única sequência.","tip": "Continue fornecendo o 'pacote completo' na primeira oferta para filtrar leads qualificados rapidamente.","msgRef": "200t/mes, R$228 ton"},
      {"type": "warn","label": "⚠️ Atenção","title": "Passagem de Bastão","text": "A intervenção da Vanessa para avisar que o Leandro ligaria pode criar ruído desnecessário se não for ágil.","tip": "Em negociações B2B rápidas, o próprio vendedor deve ligar imediatamente após o 'Pode sim' para manter o timing.","msgRef": "Leandro vai te ligar"}
    ],
    "objecoes": [
      {"objecao": "Preciso verificar com o gerente","resposta_dada": "Aceitou a ligação solicitada pela cliente.","resposta_ideal": "Perfeito. Vou te ligar agora para te passar os argumentos de custo-benefício que você pode apresentar para ele e facilitar a aprovação."}
    ],
    "followupMsg": "Gabi, conforme falamos na ligação, consegui segurar essa cotação da Inpasa até o final do dia. O seu gerente deu o ok para as 200t de dezembro?"
  },
  "Germinare x Cargill Regional MG": {
    "score": 8.5,"scoreLabel": "Abordagem ágil e consultiva",
    "summary": "Vanessa iniciou a oferta com dados comerciais precisos, gerando interesse imediato no comprador da Cargill. O Leandro interveiu rapidamente para converter a conversa de chat em uma call técnica, agilizando o ciclo de venda.",
    "status": "Em andamento","vendedor": "Vanessa e Leandro","produto": "DDGs Inpasa",
    "metrics": {"respostaMed": "1min","objecoes": "0","conversao": "Parcial","msgs": "9"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Dados Comerciais Completos","text": "A Vanessa já iniciou com produto, volume, preço e prazo de pagamento, o que filtra curiosos e atrai compradores sérios.","tip": "Continue fornecendo a tríade (Preço, Volume, Prazo) na primeira mensagem para acelerar o BID.","msgRef": "200t/mes, R$ 228 ton"},
      {"type": "good","label": "✅ Ponto Forte","title": "Transição para Call","text": "O vendedor Leandro percebeu o gatilho de interesse técnico e propôs a ligação para fechar detalhes complexos.","tip": "Em contas grandes como Cargill, a call é essencial para entender se o BID será spot ou contrato recorrente.","msgRef": "Posso te ligar para detalhar?"},
      {"type": "warn","label": "⚠️ Atenção","title": "Troca de Interlocutor","text": "A entrada de um segundo vendedor sem aviso pode confundir o cliente se não for bem coordenada.","tip": "O Leandro poderia ter se apresentado como especialista técnico ou gerente da conta para justificar a entrada.","msgRef": "Cargill aqui o Leandro"}
    ],
    "objecoes": [],
    "followupMsg": "Oi, conforme falamos por telefone, seguem em anexo as especificações do DDGs da Inpasa. Já confirmei a disponibilidade das 200t para dezembro. Podemos avançar com o fechamento desse lote?"
  },
  "Kellen Superv": {
    "score": 8.5,"scoreLabel": "Negociação ágil e objetiva",
    "summary": "Vanessa apresentou uma oferta clara de DDGs e obteve a confirmação de interesse para 100 toneladas. A negociação avançou rapidamente para a fase de formalização do BID.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "DDGs Inpasa",
    "metrics": {"respostaMed": "1min","objecoes": "0","conversao": "Parcial","msgs": "7"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Timing Impecável","text": "A vendedora manteve um tempo de resposta baixíssimo, crítico no mercado de grãos para garantir a oportunidade.","tip": "Continue priorizando o retorno rápido quando o cliente demonstrar interesse em verificar demanda.","msgRef": "vou reservar pra voces"},
      {"type": "good","label": "✅ Ponto Forte","title": "Oferta Estruturada","text": "A mensagem inicial já trouxe os dados essenciais (Produto, Fornecedor, Preço e Prazo), acelerando a tomada de decisão.","tip": "Mantenha o padrão de informar a origem (Inpasa) e o destino (Patos) logo no início.","msgRef": "Inpasa, R$ 228 ton"}
    ],
    "objecoes": [],
    "followupMsg": "Oi Kellen, já estou com o volume de 100t de DDGs pré-reservado aqui na Inpasa. Consegue me enviar o BID formal agora para eu travar esse negócio?"
  },
  "Fazendão x Germinare": {
    "score": 6.5,"scoreLabel": "Agilidade técnica, fechamento passivo",
    "summary": "A vendedora foi ágil ao calcular o frete e sanar a dúvida de composição de preço do cliente. Contudo, a conversa estagnou após a confirmação do valor final, sem uma tentativa clara de fechamento ou coleta de volume.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "DDGs Inpasa",
    "metrics": {"respostaMed": "2min","objecoes": "0","conversao": "Parcial","msgs": "6"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Agilidade no retorno","text": "Vanessa levou apenas 3 minutos para fornecer o cálculo do frete, mantendo o cliente engajado.","tip": "Mantenha esse tempo de resposta, pois no mercado de grãos a volatilidade exige rapidez.","msgRef": "vou calcular"},
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Falta de fechamento (CTA)","text": "A vendedora confirmou o preço mas não solicitou o BID ou o volume para reserva.","tip": "Ao confirmar o preço C/F, emende imediatamente uma pergunta de fechamento: 'Quantas carretas podemos fechar nesse valor?'","msgRef": "isso, C/F Uberaba"}
    ],
    "objecoes": [],
    "followupMsg": "Fazendão, esse preço de R$273 posto Uberaba está muito competitivo para DDG Inpasa em dezembro. Consegue me passar o volume pra eu já travar com a usina?"
  },
  "Milena Consultoria": {
    "score": 4.8,"scoreLabel": "Atendimento reativo e limitado",
    "summary": "A vendedora ofertou DDGs para dezembro, mas interrompeu a fluidez da negociação ao dar uma resposta negativa seca sobre a disponibilidade de novembro. Faltou postura consultiva para converter a necessidade do cliente.",
    "status": "Travado","vendedor": "Vanessa","produto": "DDGs Inpasa",
    "metrics": {"respostaMed": "1min","objecoes": "1","conversao": "Não","msgs": "7"},
    "improvements": [
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Resposta Finalizadora","text": "Ao responder apenas que 'novembro já fechou', você encerra a possibilidade de venda sem resistência.","tip": "Entenda a urgência do cliente. Se ele quer novembro, pergunte se é por estoque baixo ou preço, e tente puxar a venda de dezembro como solução antecipada.","msgRef": "so dezembro no momento"},
      {"type": "good","label": "✅ Ponto Forte","title": "Tempo de Resposta","text": "A vendedora foi extremamente ágil em todas as interações, respondendo em menos de um minuto.","tip": "Mantenha essa agilidade, mas use o tempo para elaborar argumentos melhores.","msgRef": "novembro ja fechamos"}
    ],
    "objecoes": [
      {"objecao": "Cliente quer saber se tem disponibilidade para novembro.","resposta_dada": "novembro ja fechamos, so dezembro no momento","resposta_ideal": "Novembro está com as janelas lotadas devido à alta demanda, mas o lote de dezembro é o que garante o melhor custo-benefício agora. O cliente tem estoque para cobrir essa virada de mês?"}
    ],
    "followupMsg": "Milena, consegui confirmar aqui que a Inpasa deve liberar os carregamentos de dezembro logo no início do mês. Se o cliente tiver flexibilidade de estoque por mais alguns dias, conseguimos travar esse preço de agora antes de uma nova subida. O que acha?"
  },
  "Nutrialfa | Germinare": {
    "score": 5.5,"scoreLabel": "Abordagem reativa, falta urgência",
    "summary": "A vendedora apresentou o produto e respondeu prontamente às dúvidas técnicas. No entanto, a conversa estagnou ao aceitar passivamente o tempo de análise do comprador sem aplicar gatilhos de escassez ou buscar o BID.",
    "status": "Em andamento","vendedor": "Vanessa","produto": "DDGs Inpasa",
    "metrics": {"respostaMed": "1min","objecoes": "0","conversao": "Parcial","msgs": "7"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Agilidade no atendimento","text": "Vanessa foi extremamente rápida em fornecer os dados técnicos, mantendo o timing do comprador.","tip": "Continue com esse tempo de resposta, ele é crucial no mercado Spot de grãos.","msgRef": "42% PB, 10% umidade"},
      {"type": "bad","label": "🚨 Melhora Urgente","title": "Passividade no fechamento","text": "Ao responder apenas 'aguardo', a vendedora perdeu a chance de coletar o BID ou criar urgência sobre o lote.","tip": "Quando o cliente for 'analisar', tente extrair o preço alvo (BID) ou mencione a liquidez do lote.","msgRef": "otimo, aguardo"}
    ],
    "objecoes": [
      {"objecao": "vou analisar e te retorno","resposta_dada": "otimo, aguardo","resposta_ideal": "Perfeito. Como a demanda para dezembro está alta e o volume é limitado, qual seria seu preço alvo para eu já tentar travar com o fornecedor enquanto você valida o técnico?"}
    ],
    "followupMsg": "Oi, tudo bem? Conseguiu validar o DDG com sua equipe? O mercado deu uma movimentada agora à tarde e esse lote para Patos de Minas está com bastante procura. Se tiver um BID, consigo tentar priorizar sua carga aqui."
  },
  "Conrado": {
    "score": 9.0,"scoreLabel": "Fluxo comercial ágil e objetivo",
    "summary": "O vendedor Conrado apresentou uma demanda qualificada com volume, praça e preço alvo definidos. A broker Vanessa agiu rapidamente solicitando a formalização para iniciar a negociação.",
    "status": "Em andamento","vendedor": "Conrado","produto": "DDGs",
    "metrics": {"respostaMed": "1min","objecoes": "0","conversao": "Parcial","msgs": "5"},
    "improvements": [
      {"type": "good","label": "✅ Ponto Forte","title": "Qualificação da Demanda","text": "Conrado forneceu os dados essenciais (volume, período e preço) logo na abertura, evitando idas e vindas desnecessárias.","tip": "Continue enviando o 'pacote completo' de informações para acelerar o trabalho da mesa de negociação.","msgRef": "150 ton dezembro, quer R$ 220"},
      {"type": "good","label": "✅ Ponto Forte","title": "Agilidade de Resposta","text": "A interação entre o vendedor e a broker ocorreu em tempo real, crucial no mercado de commodities.","tip": "Manter padrão de resposta abaixo de 5 minutos é um diferencial competitivo.","msgRef": "manda o BID formal"}
    ],
    "objecoes": [],
    "followupMsg": "Vanessa, acabei de te enviar o BID formal. Consegues priorizar esse com os fornecedores? O cliente tem pressa para carregar em dezembro."
  }
}

AVATAR_GRADS = [
    "linear-gradient(135deg,#3b4a6b,#5b7aaa)",
    "linear-gradient(135deg,#3b6b4a,#5baa7a)",
    "linear-gradient(135deg,#6b3b4a,#aa5b70)",
    "linear-gradient(135deg,#4a3b6b,#7a5baa)",
    "linear-gradient(135deg,#5a3b3b,#aa5b5b)",
    "linear-gradient(135deg,#1a4731,#25d366)",
    "linear-gradient(135deg,#1f3a5f,#3b82f6)",
    "linear-gradient(135deg,#4a4a3b,#8a8a5b)",
]

def initials(name):
    parts = str(name or '?').split()[:2]
    return ''.join(p[0] for p in parts if p).upper() or '?'

def score_color(s):
    if s >= 8: return '#25d366'
    if s >= 6: return '#f59e0b'
    return '#ef4444'

def arc_offset(score):
    return 150.8 - (score / 10) * 150.8

conversations_js = []
for i, (chat_name, ev) in enumerate(evals.items()):
    chat = chats_index.get(chat_name)
    if not chat:
        print(f'  WARNING: chat not found: {chat_name}')
        continue
    msgs_js = []
    for m in chat['mensagens']:
        msgs_js.append({
            'side': 'sent' if m.get('from_me') else 'recv',
            'sender': 'Vanessa' if m.get('from_me') else (m.get('de') or ''),
            'text': (m.get('texto') or '[' + (m.get('tipo') or 'midia') + ']'),
            'time': m.get('hora', ''),
        })
    last_msg = chat['mensagens'][-1] if chat['mensagens'] else {}
    preview = (last_msg.get('texto') or '')[:55] or '[midia]'
    conv = {
        'id': i,
        'chat': chat['chat'],
        'initials': initials(chat['chat']),
        'avatarGrad': AVATAR_GRADS[i % len(AVATAR_GRADS)],
        'time': (chat['mensagens'][-1].get('hora') if chat['mensagens'] else ''),
        'preview': preview,
        'score': ev.get('score', 0),
        'msgs': chat['total'],
        'status': ev.get('status', 'Em andamento'),
        'tags': [t for t in [ev.get('produto'), ev.get('status')] if t],
        'scoreLabel': ev.get('scoreLabel', ''),
        'summary': ev.get('summary', ''),
        'vendedor': ev.get('vendedor', ''),
        'metrics': ev.get('metrics', {}),
        'improvements': ev.get('improvements', []),
        'objecoes': ev.get('objecoes', []),
        'followupMsg': ev.get('followupMsg', ''),
        'messages': msgs_js,
        'arcOffset': arc_offset(ev.get('score', 0)),
        'arcColor': score_color(ev.get('score', 0)),
        'scoreColor': score_color(ev.get('score', 0)),
    }
    conversations_js.append(conv)
    print(f'  [{i+1}] {chat_name}: score={ev["score"]}, status={ev["status"]}')

DATE = "2026-05-12"
TOTAL_ORIGINAL = 33
conv_data = json.dumps(conversations_js, ensure_ascii=False, separators=(',', ':'))

html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SalesCoach AI — Germinare</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');
  :root{--bg:#0d0f12;--surface:#161a1f;--surface2:#1e2329;--border:#2a2f38;--text:#e8ecf0;--muted:#6b7a8d;--accent:#25d366;--accent2:#128c7e;--warn:#f59e0b;--danger:#ef4444;--info:#3b82f6;--highlight:rgba(37,211,102,0.12)}
  *{margin:0;padding:0;box-sizing:border-box}
  body{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--text);height:100vh;overflow:hidden;display:flex;flex-direction:column}
  .topbar{background:var(--surface);border-bottom:1px solid var(--border);padding:0 20px;height:52px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
  .topbar-brand{display:flex;align-items:center;gap:10px}
  .topbar-logo{width:28px;height:28px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px}
  .topbar-title{font-family:'Syne',sans-serif;font-weight:700;font-size:15px;letter-spacing:-.3px}
  .topbar-title span{color:var(--accent)}
  .topbar-meta{display:flex;gap:12px;align-items:center}
  .pill{background:var(--surface2);border:1px solid var(--border);border-radius:20px;padding:4px 14px;font-size:12px;color:var(--muted);font-weight:500}
  .app-layout{display:flex;flex:1;overflow:hidden}
  .conv-list{width:300px;flex-shrink:0;background:var(--surface);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}
  .conv-list-header{padding:14px 16px 10px;border-bottom:1px solid var(--border);flex-shrink:0}
  .conv-list-header h3{font-family:'Syne',sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin-bottom:10px}
  .search-box{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:7px 12px;display:flex;align-items:center;gap:8px}
  .search-box input{background:transparent;border:none;outline:none;color:var(--text);font-size:12px;width:100%;font-family:'DM Sans',sans-serif}
  .search-box input::placeholder{color:var(--muted)}
  .conv-items{flex:1;overflow-y:auto;padding:8px 0}
  .conv-items::-webkit-scrollbar{width:4px}
  .conv-items::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
  .conv-item{padding:12px 16px;cursor:pointer;border-left:3px solid transparent;transition:all .15s}
  .conv-item:hover{background:var(--surface2)}
  .conv-item.active{background:var(--highlight);border-left-color:var(--accent)}
  .conv-item-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px}
  .conv-name{font-weight:600;font-size:13px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:175px}
  .conv-time{font-size:11px;color:var(--muted);flex-shrink:0}
  .conv-preview{font-size:11.5px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:8px}
  .conv-footer{display:flex;justify-content:space-between;align-items:center}
  .score-badge{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:2px 8px;border-radius:20px}
  .score-good{background:rgba(37,211,102,.15);color:var(--accent)}
  .score-mid{background:rgba(245,158,11,.15);color:var(--warn)}
  .score-low{background:rgba(239,68,68,.12);color:var(--danger)}
  .tag-chips{display:flex;gap:4px}
  .tag-chip{font-size:10px;padding:2px 6px;border-radius:4px;background:var(--surface);border:1px solid var(--border);color:var(--muted);max-width:90px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .conv-main{flex:1;display:flex;flex-direction:column;overflow:hidden;border-right:1px solid var(--border)}
  .conv-header{padding:12px 20px;background:var(--surface);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
  .conv-header-left{display:flex;align-items:center;gap:12px}
  .contact-avatar{width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;color:#fff}
  .contact-info h4{font-size:14px;font-weight:600}
  .contact-info p{font-size:11px;color:var(--muted)}
  .status-pill{font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px}
  .sp-Fechado{background:rgba(37,211,102,.15);color:var(--accent)}
  .sp-Emandamento{background:rgba(59,130,246,.15);color:var(--info)}
  .sp-Travado{background:rgba(245,158,11,.15);color:var(--warn)}
  .sp-Perdido{background:rgba(239,68,68,.12);color:var(--danger)}
  .messages-area{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:10px}
  .messages-area::-webkit-scrollbar{width:4px}
  .messages-area::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
  .day-sep{display:flex;align-items:center;gap:10px;margin:4px 0 8px}
  .day-sep-line{flex:1;height:1px;background:var(--border)}
  .day-sep-label{font-size:11px;color:var(--muted);background:var(--surface2);padding:2px 10px;border-radius:10px;border:1px solid var(--border)}
  .msg-row{display:flex;gap:8px;max-width:78%}
  .msg-row.sent{align-self:flex-end;flex-direction:row-reverse}
  .msg-row.received{align-self:flex-start}
  .msg-meta{font-size:10px;color:var(--muted);margin-bottom:3px;padding:0 4px}
  .msg-row.sent .msg-meta{text-align:right}
  .msg-bubble{padding:10px 14px;border-radius:12px;font-size:13px;line-height:1.5;white-space:pre-wrap;word-break:break-word}
  .msg-row.sent .msg-bubble{background:#1d4a2e;border-bottom-right-radius:3px}
  .msg-row.received .msg-bubble{background:var(--surface2);border:1px solid var(--border);border-bottom-left-radius:3px}
  .msg-bubble.hl-good{background:rgba(37,211,102,.18)!important;border:1.5px solid rgba(37,211,102,.45)!important}
  .msg-bubble.hl-warn{background:rgba(245,158,11,.15)!important;border:1.5px solid rgba(245,158,11,.4)!important}
  .msg-bubble.hl-bad{background:rgba(239,68,68,.14)!important;border:1.5px solid rgba(239,68,68,.4)!important}
  .followup-area{border-top:1px solid var(--border);padding:12px 20px;background:var(--surface);flex-shrink:0}
  .followup-label{font-size:10px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.8px;margin-bottom:6px}
  .followup-box{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:10px 14px;font-size:12px;line-height:1.55;color:var(--text);display:flex;align-items:flex-start;justify-content:space-between;gap:10px;transition:border-color .15s}
  .followup-box:hover{border-color:var(--accent)}
  .followup-box span{flex:1}
  .copy-btn{font-size:10px;padding:3px 8px;border-radius:4px;background:rgba(37,211,102,.15);color:var(--accent);border:none;cursor:pointer;font-family:'DM Sans',sans-serif;font-weight:600;white-space:nowrap;flex-shrink:0}
  .copy-btn:hover{background:rgba(37,211,102,.3)}
  .synthesis-panel{width:290px;flex-shrink:0;background:var(--surface);display:flex;flex-direction:column;overflow:hidden}
  .synth-header{padding:14px 16px 12px;border-bottom:1px solid var(--border);flex-shrink:0}
  .synth-header h3{font-family:'Syne',sans-serif;font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:12px}
  .score-ring-wrap{display:flex;align-items:center;gap:14px}
  .score-ring{position:relative;width:58px;height:58px;flex-shrink:0}
  .score-ring svg{transform:rotate(-90deg)}
  .score-ring-label{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-size:17px;font-weight:800}
  .score-meta h4{font-family:'Syne',sans-serif;font-size:14px;font-weight:800}
  .score-meta p{font-size:11px;color:var(--muted);margin-top:2px}
  .synth-body{flex:1;overflow-y:auto;padding:14px 16px;display:flex;flex-direction:column;gap:16px}
  .synth-body::-webkit-scrollbar{width:4px}
  .synth-body::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
  .synth-section h5{font-family:'Syne',sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:8px}
  .summary-text{font-size:12.5px;line-height:1.6;color:#b0bac6}
  .improve-item{border:1px solid var(--border);border-radius:10px;padding:10px 12px;background:var(--surface2);cursor:pointer;transition:all .2s;position:relative;overflow:hidden;margin-bottom:8px}
  .improve-item::before{content:'';position:absolute;left:0;top:0;bottom:0;width:3px}
  .improve-item.good::before{background:var(--accent)}
  .improve-item.warn::before{background:var(--warn)}
  .improve-item.bad::before{background:var(--danger)}
  .improve-item:hover{border-color:var(--accent);transform:translateX(2px)}
  .il-good{color:var(--accent)}
  .il-warn{color:var(--warn)}
  .il-bad{color:var(--danger)}
  .improve-title{font-size:12.5px;font-weight:600;margin-bottom:4px}
  .improve-text{font-size:11.5px;color:var(--muted);line-height:1.5}
  .improve-tip{margin-top:6px;font-size:11px;color:rgba(37,211,102,.75);line-height:1.4}
  .metrics-row{display:grid;grid-template-columns:1fr 1fr;gap:8px}
  .metric-card{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:10px 12px}
  .metric-card-label{font-size:10px;color:var(--muted);font-weight:500}
  .metric-card-value{font-family:'Syne',sans-serif;font-size:17px;font-weight:800;margin-top:2px}
  .mv-good{color:var(--accent)}
  .mv-warn{color:var(--warn)}
  .mv-bad{color:var(--danger)}
  .metric-card-sub{font-size:10px;color:var(--muted);margin-top:1px}
  .obj-card{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:10px;margin-bottom:8px}
  .obj-label{font-size:10px;font-weight:700;padding:2px 6px;border-radius:4px;white-space:nowrap}
  .obj-label.dada{background:var(--surface2);color:var(--muted)}
  .obj-label.ideal{background:rgba(37,211,102,.15);color:var(--accent)}
  .empty-state{flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px;color:var(--muted);font-size:13px}
  @keyframes flash{0%,100%{opacity:1}50%{opacity:.4}}
  .flash{animation:flash .4s 2}
</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-brand">
    <div class="topbar-logo">🌱</div>
    <div class="topbar-title">Sales<span>Coach</span> AI — Germinare</div>
  </div>
  <div class="topbar-meta">
    <div class="pill">📅 """ + DATE + """</div>
    <div class="pill">✦ """ + str(len(conversations_js)) + " negociações de " + str(TOTAL_ORIGINAL) + """ conversas</div>
  </div>
</div>
<div class="app-layout">
  <div class="conv-list">
    <div class="conv-list-header">
      <h3>Negociações do dia</h3>
      <div class="search-box">🔍 <input type="text" id="searchInput" placeholder="Buscar..." oninput="filterList()"/></div>
    </div>
    <div class="conv-items" id="convList"></div>
  </div>
  <div class="conv-main">
    <div class="conv-header" id="convHeader" style="display:none">
      <div class="conv-header-left">
        <div class="contact-avatar" id="convAvatar"></div>
        <div class="contact-info"><h4 id="convContactName"></h4><p id="convContactSub"></p></div>
      </div>
      <div id="convStatusPill"></div>
    </div>
    <div id="emptyState" class="empty-state" style="flex:1">
      <div style="font-size:36px">💬</div><div>Selecione uma negociação</div>
    </div>
    <div class="messages-area" id="messagesArea" style="display:none"></div>
    <div class="followup-area" id="followupArea" style="display:none">
      <div class="followup-label">💬 Follow-up sugerido pela IA</div>
      <div class="followup-box">
        <span id="followupText"></span>
        <button class="copy-btn" onclick="copyFollowup()">Copiar</button>
      </div>
    </div>
  </div>
  <div class="synthesis-panel">
    <div class="synth-header">
      <h3>Análise IA</h3>
      <div class="score-ring-wrap">
        <div class="score-ring">
          <svg viewBox="0 0 58 58" width="58" height="58">
            <circle cx="29" cy="29" r="24" fill="none" stroke="#2a2f38" stroke-width="5"/>
            <circle id="scoreArc" cx="29" cy="29" r="24" fill="none" stroke="#6b7a8d" stroke-width="5"
              stroke-dasharray="150.8" stroke-dashoffset="75.4" stroke-linecap="round"/>
          </svg>
          <div class="score-ring-label" id="scoreLabel" style="color:var(--muted)">—</div>
        </div>
        <div class="score-meta">
          <h4 id="scoreTitle" style="color:var(--muted)">Selecione</h4>
          <p id="scoreSubtitle"></p>
        </div>
      </div>
    </div>
    <div class="synth-body" id="synthBody">
      <div style="color:var(--muted);font-size:12px;text-align:center;margin-top:20px">Selecione uma conversa para ver a análise</div>
    </div>
  </div>
</div>
<script>
var CONVS=""" + conv_data + """;
var display=CONVS.slice();
var activeId=-1;
function sc(s){return s>=8?'score-good':s>=6?'score-mid':'score-low'}
function esc(t){return String(t||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function renderList(){
  document.getElementById('convList').innerHTML=display.map(function(c){
    return '<div class="conv-item '+(c.id===activeId?'active':'')+'" onclick="selConv('+c.id+')">'
      +'<div class="conv-item-top"><div class="conv-name">'+esc(c.chat)+'</div><div class="conv-time">'+esc(c.time)+'</div></div>'
      +'<div class="conv-preview">'+esc(c.preview)+'</div>'
      +'<div class="conv-footer">'
        +'<div class="score-badge '+sc(c.score)+'">⭐ '+c.score+'</div>'
        +'<div class="tag-chips">'+c.tags.slice(0,2).map(function(t){return '<div class="tag-chip">'+esc(t)+'</div>'}).join('')+'</div>'
      +'</div></div>';
  }).join('');
}
function filterList(){
  var q=document.getElementById('searchInput').value.toLowerCase();
  display=CONVS.filter(function(c){return c.chat.toLowerCase().includes(q)||c.tags.join(' ').toLowerCase().includes(q)||c.vendedor.toLowerCase().includes(q)});
  renderList();
}
function selConv(id){
  activeId=id;
  var c=CONVS.find(function(x){return x.id===id});
  if(!c) return;
  document.getElementById('convHeader').style.display='flex';
  document.getElementById('convAvatar').textContent=c.initials;
  document.getElementById('convAvatar').style.background=c.avatarGrad;
  document.getElementById('convContactName').textContent=c.chat;
  document.getElementById('convContactSub').textContent=c.msgs+' mensagens · '+c.vendedor;
  var sp=c.status.replace(/ /g,'');
  document.getElementById('convStatusPill').innerHTML='<div class="status-pill sp-'+sp+'">'+esc(c.status)+'</div>';
  document.getElementById('emptyState').style.display='none';
  var area=document.getElementById('messagesArea');
  area.style.display='flex';
  area.innerHTML='<div class="day-sep"><div class="day-sep-line"></div><div class="day-sep-label">'+esc(c.chat)+' · """ + DATE + """</div><div class="day-sep-line"></div></div>'
    +c.messages.map(function(m,i){
      var impIdx=c.improvements.findIndex(function(imp){return imp.msgRef&&m.text.toLowerCase().includes(imp.msgRef.toLowerCase().substring(0,25))});
      var hl=impIdx>=0?(' hl-'+c.improvements[impIdx].type):'';
      return '<div class="msg-row '+m.side+'" id="msg-'+id+'-'+i+'">'
        +'<div style="display:flex;flex-direction:column;'+(m.side==='sent'?'align-items:flex-end':'')+'">'
        +'<div class="msg-meta">'+esc(m.sender)+' · '+esc(m.time)+'</div>'
        +'<div class="msg-bubble'+hl+'"'+(impIdx>=0?' onclick="fromMsg('+impIdx+','+id+','+i+')" style="cursor:pointer"':'')+'>'+esc(m.text)
        +(impIdx>=0?'<div style="margin-top:6px"><span style="font-size:10px;font-weight:700;padding:2px 7px;border-radius:4px;cursor:pointer;background:rgba(37,211,102,.15);color:var(--accent)">'+esc(c.improvements[impIdx].label)+' →</span></div>':'')
        +'</div></div></div>';
    }).join('');
  area.scrollTop=area.scrollHeight;
  document.getElementById('followupArea').style.display='block';
  document.getElementById('followupText').textContent=c.followupMsg;
  document.getElementById('scoreArc').style.stroke=c.arcColor;
  document.getElementById('scoreArc').setAttribute('stroke-dashoffset',c.arcOffset);
  document.getElementById('scoreLabel').textContent=c.score;
  document.getElementById('scoreLabel').style.color=c.scoreColor;
  document.getElementById('scoreTitle').textContent=c.scoreLabel;
  document.getElementById('scoreTitle').style.color=c.scoreColor;
  document.getElementById('scoreSubtitle').textContent=c.status+' · '+c.msgs+' msgs';
  var m=c.metrics||{};
  document.getElementById('synthBody').innerHTML=
    '<div class="synth-section"><h5>📋 Síntese</h5><p class="summary-text">'+esc(c.summary)+'</p></div>'
    +'<div class="synth-section"><h5>📊 Métricas</h5><div class="metrics-row">'
      +'<div class="metric-card"><div class="metric-card-label">Resp. Média</div><div class="metric-card-value '+(parseInt(m.respostaMed)<5?'mv-good':'mv-warn')+'">'+esc(m.respostaMed||'—')+'</div></div>'
      +'<div class="metric-card"><div class="metric-card-label">Objeções</div><div class="metric-card-value '+(parseInt(m.objecoes)===0?'mv-good':parseInt(m.objecoes)>1?'mv-bad':'mv-warn')+'">'+esc(m.objecoes||'0')+'</div></div>'
      +'<div class="metric-card"><div class="metric-card-label">Mensagens</div><div class="metric-card-value">'+esc(m.msgs||String(c.msgs))+'</div></div>'
      +'<div class="metric-card"><div class="metric-card-label">Conversão</div><div class="metric-card-value '+(m.conversao==='Sim'?'mv-good':m.conversao==='Parcial'?'mv-warn':'mv-bad')+'">'+esc(m.conversao||'—')+'</div></div>'
    +'</div></div>'
    +'<div class="synth-section"><h5>💡 Análise</h5>'
      +c.improvements.map(function(imp,idx){
        return '<div class="improve-item '+imp.type+'" id="imp-'+id+'-'+idx+'" onclick="fromImp('+idx+','+id+')">'
          +'<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px">'
          +'<span style="font-size:11px;font-weight:700" class="il-'+imp.type+'">'+esc(imp.label)+'</span>'
          +'<span style="font-size:12px;color:var(--muted)">↗</span></div>'
          +'<div class="improve-title">'+esc(imp.title)+'</div>'
          +'<div class="improve-text">'+esc(imp.text)+'</div>'
          +'<div class="improve-tip">💡 '+esc(imp.tip)+'</div>'
          +'</div>';
      }).join('')
    +'</div>'
    +(c.objecoes&&c.objecoes.length?
      '<div class="synth-section"><h5>🛡 Objeções</h5>'
      +c.objecoes.map(function(o){
        return '<div class="obj-card">'
          +'<div style="font-size:12px;font-weight:600;margin-bottom:6px">'+esc(o.objecao)+'</div>'
          +(o.resposta_dada?'<div style="display:flex;gap:6px;margin-bottom:4px;align-items:flex-start"><span class="obj-label dada">Como reagiu</span><span style="font-size:11px;color:#b0bac6;line-height:1.4;flex:1">'+esc(o.resposta_dada)+'</span></div>':'')
          +(o.resposta_ideal?'<div style="display:flex;gap:6px;align-items:flex-start"><span class="obj-label ideal">Ideal</span><span style="font-size:11px;color:#b0bac6;line-height:1.4;flex:1">'+esc(o.resposta_ideal)+'</span></div>':'')
          +'</div>';
      }).join('')+'</div>'
    :'');
  renderList();
}
function fromImp(impIdx,convId){
  document.querySelectorAll('.improve-item').forEach(function(e){e.style.boxShadow=''});
  var ie=document.getElementById('imp-'+convId+'-'+impIdx);
  if(ie) ie.style.boxShadow='0 0 0 2px rgba(37,211,102,.3)';
  var c=CONVS.find(function(x){return x.id===convId});
  if(!c) return;
  var imp=c.improvements[impIdx];
  var mIdx=c.messages.findIndex(function(m){return imp.msgRef&&m.text.toLowerCase().includes(imp.msgRef.toLowerCase().substring(0,25))});
  if(mIdx>=0){
    var me=document.getElementById('msg-'+convId+'-'+mIdx);
    if(me){me.scrollIntoView({behavior:'smooth',block:'center'});me.classList.add('flash');setTimeout(function(){me.classList.remove('flash')},900)}
  }
}
function fromMsg(impIdx,convId,msgIdx){fromImp(impIdx,convId)}
function copyFollowup(){
  var text=document.getElementById('followupText').textContent;
  navigator.clipboard.writeText(text).then(function(){
    var btn=document.querySelector('.copy-btn');
    btn.textContent='Copiado ✓';
    setTimeout(function(){btn.textContent='Copiar'},1500);
  });
}
renderList();
if(CONVS.length>0) selConv(CONVS[0].id);
</script>
</body>
</html>"""

with open('C:/Users/sorna/Documents/germinare-supabase/salescoach.html', 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('=== CONCLUIDO ===')
print(f'{TOTAL_ORIGINAL} conversas originais -> {len(conversations_js)} negociações avaliadas')
print(f'Arquivo: C:/Users/sorna/Documents/germinare-supabase/salescoach.html')
print(f'Tamanho: {len(html)} chars')
