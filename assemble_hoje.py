import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/sorna/Documents/germinare-supabase/data_hoje.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

after_f1 = d['after_f1']
chats_index = {c['chat']: c for c in after_f1}

evals = {
  "Vanessa Germinare 🌱": {
    "score": 6.8, "scoreLabel": "Operacional pesado, comercial pendente",
    "summary": "Vanessa foca na organização de eventos e logística, enquanto cobra agilidade em negociações críticas de caroço de algodão. Há gargalos claros em termos contratuais e atualização de CRM pelo vendedor.",
    "status": "Em andamento", "vendedor": "Conrado", "produto": "Caroço de algodão, Farelo",
    "metrics": {"respostaMed": "15min", "objecoes": "3", "conversao": "Parcial", "msgs": "110"},
    "improvements": [
      {"type": "good", "label": "✅ Ponto Forte", "title": "Visão Estratégica",
       "text": "Identificação precisa de clientes âncoras como a Danone para ganho de mercado.",
       "tip": "Use o histórico da Danone para criar autoridade com outros compradores da mesma região.",
       "msgRef": "seria bom entrarmos lá"},
      {"type": "warn", "label": "⚠️ Atenção", "title": "Gestão de CRM",
       "text": "O vendedor parece negligenciar o registro de dados, o que prejudica a inteligência comercial.",
       "tip": "Condicione o repasse de novos BIDs à atualização prévia do status no RD Station.",
       "msgRef": "atualizar o Rd"},
      {"type": "bad", "label": "🚨 Melhora Urgente", "title": "Postura Proativa",
       "text": "Necessidade de cobrança constante por informações básicas (BIDs e prazos).",
       "tip": "Implemente um checklist de envio de BID: Volume, Preço, Prazo e Fornecedor antes de acionar o broker.",
       "msgRef": "como que vou flar com ele"}
    ],
    "objecoes": [
      {"objecao": "Fornecedor (Yukaer) não aceita alongamento de contrato.",
       "resposta_dada": "Identificou como entrave crítico e questionou viabilidade do preço.",
       "resposta_ideal": "Negociar cláusula de reajuste programado ou bonificação por volume para viabilizar o contrato curto."},
      {"objecao": "Preço fora do mercado (Danone).",
       "resposta_dada": "Acionou Leonardo para reprecificação imediata do caroço.",
       "resposta_ideal": "Apresentar comparativo de frete e qualidade (proteína/energia) para justificar o prêmio."}
    ],
    "followupMsg": "Leonardo, conseguiu o retorno da reprecificação do caroço para a Danone? O cliente está aguardando e precisamos entrar lá com esse BID agressivo hoje."
  },
  "Thais Camila": {
    "score": 6.8, "scoreLabel": "Proativa com Dependência Logística",
    "summary": "Thais demonstra agilidade no atendimento de múltiplas demandas simultâneas para casca e DDGS. Contudo, a negociação está travada pela falta de retornos da Inpasa e pela ausência de um colega, gerando vácuo nas cotações.",
    "status": "Em andamento", "vendedor": "Thais Camila", "produto": "DDGS e Casca de Soja",
    "metrics": {"respostaMed": "5min", "objecoes": "1", "conversao": "Não", "msgs": "32"},
    "improvements": [
      {"type": "good", "label": "✅ Ponto Forte", "title": "Multitarefa e Agilidade",
       "text": "Thais consegue gerenciar três frentes de clientes diferentes de forma organizada.",
       "tip": "Continue usando as marcações (@) para garantir que os stakeholders vejam os pedidos urgentes.",
       "msgRef": "dps cobra ele as cotações"},
      {"type": "warn", "label": "⚠️ Atenção", "title": "Dependência de Terceiros",
       "text": "A venda está parada aguardando a Inpasa e o retorno de um colega de férias, sem um plano B imediato.",
       "tip": "Sempre tenha um fornecedor secundário quando o principal estiver offline.",
       "msgRef": "sem nossos retornos da inpasa"},
      {"type": "bad", "label": "🚨 Melhora Urgente", "title": "Contorno de Preço",
       "text": "Ao receber que o cliente comprou a 63,00 (abaixo do ofertado), ela não questionou origem ou frete.",
       "tip": "Pergunte as especificações do lote concorrente para defender sua spread ou negociar melhor.",
       "msgRef": "Muito fora Thais, eu consegui"}
    ],
    "objecoes": [
      {"objecao": "Preço ('Muito fora... consegui comprar um lote a 63,00')",
       "resposta_dada": "Estou vendo com ela, volto contigo qualquer coisa.",
       "resposta_ideal": "Entendi, Henrique. Esse lote de 63,00 é para carregamento imediato também? Meu produto é padrão Cargill, com melhor fluidez."}
    ],
    "followupMsg": "Henrique, consegui alinhar com a usina aqui. Se fecharmos as cargas de casca agora para Indianópolis, consigo priorizar seu carregamento antes da virada de lote. O preço de 63,00 que você viu era FOB ou CIF?"
  },
  "Fabricio": {
    "score": 6.5, "scoreLabel": "Proativo com entrave técnico",
    "summary": "O vendedor demonstra excelente visão de relacionamento ao sugerir presença em evento estratégico de pecuária. No entanto, está focado apenas em preço e aceitando passivamente a comparação desvantajosa com o farelo de soja.",
    "status": "Em andamento", "vendedor": "Fabricio", "produto": "DDGs e Farelo de Soja",
    "metrics": {"respostaMed": "22min", "objecoes": "3", "conversao": "Parcial", "msgs": "30"},
    "improvements": [
      {"type": "good", "label": "✅ Ponto Forte", "title": "Visão Relacional",
       "text": "O vendedor identificou um influenciador (Jaime) e sugeriu uma ação de marketing de baixo custo.",
       "tip": "Use o evento para coletar dados de consumo e leads qualificados, não apenas presença física.",
       "msgRef": "a jogada acho que é muito mais"},
      {"type": "warn", "label": "⚠️ Atenção", "title": "Comparativo Nutricional",
       "text": "Fabricio compara quilo por quilo do DDG com o Farelo, sem defender o valor da proteína bruta e gordura.",
       "tip": "Apresente o custo por ponto de proteína (PB) para mostrar que o DDG é mais barato mesmo com preço nominal próximo.",
       "msgRef": "DDGs teria que estar 1180"},
      {"type": "bad", "label": "🚨 Melhora Urgente", "title": "Postura de Tomador de Pedido",
       "text": "O vendedor está repassando as dores do cliente sem tentar contornar as dificuldades.",
       "tip": "Argumente sobre o ganho de estoque e proteção contra oscilação de mercado ao comprar volume fechado.",
       "msgRef": "nao precisa pagar antecipado"}
    ],
    "objecoes": [
      {"objecao": "Preço do DDG não compensa frente ao farelo de soja.",
       "resposta_dada": "Aceitou que o preço deveria ser 1180 para empatar.",
       "resposta_ideal": "O DDG não substitui apenas o farelo, ele entra como fonte de energia e proteína. No custo por kg de MS ou PB, o DDG ainda é mais eficiente."},
      {"objecao": "Dificuldade de pagamento antecipado e volume de carga.",
       "resposta_dada": "Repassou que o farelo não exige isso.",
       "resposta_ideal": "Mostrar o ROI: o desconto obtido na Germinare pelo volume/pagamento supera o custo financeiro do prazo curto."}
    ],
    "followupMsg": "Fabricio, recebi o BID do Hudson. Vou brigar pelo preço na usina. Sobre o evento no Jaime — excelente sacada! Me confirma a previsão de público. Para os clientes de Patos, foque no custo por ponto de proteína."
  },
  "Leandro": {
    "score": 7.5, "scoreLabel": "Operacional e Assertivo",
    "summary": "O vendedor iniciou com um pedido estruturado de DDGs, demonstrando bom fluxo operacional. Contudo, a conversa seguiu para um formato de balcão de cotações, perdendo o foco no fechamento dos novos produtos.",
    "status": "Fechado", "vendedor": "Leandro", "produto": "DDGs, Farelo de Soja, Casca de Soja",
    "metrics": {"respostaMed": "32min", "objecoes": "1", "conversao": "Sim", "msgs": "22"},
    "improvements": [
      {"type": "good", "label": "✅ Ponto Forte", "title": "Gestão de Risco",
       "text": "Excelente postura ao identificar a restrição de crédito do cliente e adaptar a modalidade de venda.",
       "tip": "Mantenha essa clareza sobre o perfil do cliente para evitar problemas na originação.",
       "msgRef": "apenas venda carga a carga"},
      {"type": "warn", "label": "⚠️ Atenção", "title": "Passividade na Cotação",
       "text": "Após o envio das tabelas de farelo, o vendedor não provocou o bid, deixando a decisão no cliente.",
       "tip": "Após enviar o preço, pergunte: 'Qual desses volumes melhor atende sua janela de maio?'",
       "msgRef": "seguem preços de hoje:"},
      {"type": "bad", "label": "🚨 Melhora Urgente", "title": "Transição de Assuntos",
       "text": "A troca constante entre DDG, Casca e Farelo sem fechar os tópicos anteriores dispersa a atenção do comprador.",
       "tip": "Tente organizar a demanda por janela de embarque em vez de listar produtos soltos.",
       "msgRef": "Tem preços de farelo hoje?"}
    ],
    "objecoes": [
      {"objecao": "Restrição de contrato (Risco de crédito/Operacional)",
       "resposta_dada": "Determinou venda apenas carga a carga.",
       "resposta_ideal": "Além de limitar carga a carga, oferecer pagamento antecipado para garantir originação de volumes maiores sem risco."}
    ],
    "followupMsg": "Leandro, sobre o farelo JTI (R$ 1.550) que te passei para maio: temos uma janela curta de carregamento. Consegue confirmar se o cliente roda esse volume hoje?"
  },
  "Daiane Lemes": {
    "score": 7.5, "scoreLabel": "Proativa com foco operacional",
    "summary": "A vendedora demonstrou agilidade no envio de cotações e tabelas atualizadas para múltiplos produtos. No entanto, houve repetição excessiva de informações e falta de condução incisiva para o fechamento da demanda de 200t.",
    "status": "Em andamento", "vendedor": "Daiane Lemes", "produto": "DDGS, Caroço de Algodão e Casca de Soja",
    "metrics": {"respostaMed": "54min", "objecoes": "0", "conversao": "Não", "msgs": "20"},
    "improvements": [
      {"type": "good", "label": "✅ Ponto Forte", "title": "Agilidade e Variedade",
       "text": "A vendedora forneceu opções CIF e FOB rapidamente, cobrindo diferentes necessidades do cliente.",
       "tip": "Continue utilizando o gatilho de validade (até às 15:00h) para criar senso de urgência.",
       "msgRef": "Preço válido até às 15:00h"},
      {"type": "warn", "label": "⚠️ Atenção", "title": "Repetição de Conteúdo",
       "text": "O envio múltiplo da mesma tabela polui a conversa e pode parecer erro técnico.",
       "tip": "Revise a mensagem antes de enviar ou evite o copia e cola excessivo em intervalos curtos.",
       "msgRef": "preços se mantiveram"},
      {"type": "bad", "label": "🚨 Melhora Urgente", "title": "Falta de Call to Action",
       "text": "Após confirmar que os preços se mantiveram, não houve uma pergunta de fechamento sobre as 200 toneladas.",
       "tip": "Sempre termine uma atualização de preço com pergunta indutiva: 'Podemos rodar o BID dessas 200t com esses valores?'",
       "msgRef": "preços se mantiveram"}
    ],
    "objecoes": [],
    "followupMsg": "Oi! Como os preços da Yukaer se mantiveram e o mercado está com forte tendência de alta, conseguimos confirmar aquelas 200t de casca para Santa Vitória agora para garantir o volume de maio?"
  },
  "Giulliana Diniz": {
    "score": 9.5, "scoreLabel": "Alta eficiência operacional",
    "summary": "A vendedora enviou dados estruturados e completos para a formalização de três contratos. O detalhamento do pedido inclui todas as variáveis críticas para o fechamento imediato.",
    "status": "Fechado", "vendedor": "Giulliana Diniz", "produto": "LEM (Farelo)",
    "metrics": {"respostaMed": "55min", "objecoes": "0", "conversao": "Sim", "msgs": "4"},
    "improvements": [
      {"type": "good", "label": "✅ Ponto Forte", "title": "Precisão de Dados",
       "text": "A vendedora entregou o BID com todas as informações necessárias: CNPJ, IE, frete e modalidade de pagamento.",
       "tip": "Mantenha este padrão de envio em bloco para reduzir o tempo de digitação e erro humano no sistema do broker.",
       "msgRef": "Pedido LEM 50 toneladas"},
      {"type": "warn", "label": "⚠️ Atenção", "title": "Fluxo de Confirmação",
       "text": "Embora os dados estejam completos, não há registro de confirmação de recebimento por parte do broker.",
       "tip": "Sempre solicite um 'ok' ou 'recebido' após enviar dados de contrato para garantir que o processamento começou.",
       "msgRef": "contrato 19239"}
    ],
    "objecoes": [],
    "followupMsg": "Heber, recebi as informações dos contratos 19237, 19238 e os detalhes do pedido da Cristiana (19239). Já estou espelhando com o fornecedor para rodar as assinaturas. Te confirmo assim que estiverem prontos!"
  }
}

AVATAR_GRADS = [
    "linear-gradient(135deg,#3b4a6b,#5b7aaa)",
    "linear-gradient(135deg,#3b6b4a,#5baa7a)",
    "linear-gradient(135deg,#6b3b4a,#aa5b70)",
    "linear-gradient(135deg,#4a3b6b,#7a5baa)",
    "linear-gradient(135deg,#5a3b3b,#aa5b5b)",
    "linear-gradient(135deg,#1a4731,#25d366)",
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
        print('  WARNING: chat not found:', chat_name)
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
    print('  [' + str(i+1) + '] ' + chat_name + ': score=' + str(ev['score']) + ', status=' + ev['status'])

DATE = "2026-05-12"
TOTAL_ORIGINAL = 55
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
    <div class="pill">✦ """ + str(len(conversations_js)) + " negociações de " + str(TOTAL_ORIGINAL) + """ contatos</div>
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
var CONVS="""  + conv_data + """;
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
    btn.textContent='Copiado \u2713';
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
print(str(TOTAL_ORIGINAL) + ' contatos originais -> ' + str(len(conversations_js)) + ' negociacoes avaliadas')
print('Arquivo: C:/Users/sorna/Documents/germinare-supabase/salescoach.html')
print('Tamanho: ' + str(len(html)) + ' chars')
