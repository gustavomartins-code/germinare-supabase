import json

with open("C:/Users/sorna/Documents/germinare-supabase/data_chats.json", "r", encoding="utf-8") as f:
    chats = json.load(f)

date = "2026-05-12"
total_msgs = sum(c["total"] for c in chats)
chats_js = json.dumps(chats, ensure_ascii=False, separators=(",", ":"))

# URL da edge function de avaliação
AVALIAR_URL = "https://pgmtlxgihzongbuncnpm.supabase.co/functions/v1/avaliar-conversa"

html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Germinare WhatsApp</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0d1117;color:#e6edf3;height:100vh;display:flex;flex-direction:column;overflow:hidden}
.topbar{background:#161b22;border-bottom:1px solid #30363d;padding:10px 16px;display:flex;align-items:center;gap:12px;flex-shrink:0}
.app{display:flex;flex:1;overflow:hidden}

/* SIDEBAR */
.sidebar{width:300px;min-width:300px;background:#161b22;border-right:1px solid #30363d;display:flex;flex-direction:column;overflow:hidden}
.sidebar-tools{padding:10px;border-bottom:1px solid #30363d}
.sidebar-tools input{width:100%;padding:7px 10px;background:#0d1117;border:1px solid #30363d;border-radius:6px;color:#e6edf3;font-size:12px}
.sidebar-tools input:focus{outline:none;border-color:#58a6ff}
.contact-list{flex:1;overflow-y:auto}
.contact{padding:10px 12px;cursor:pointer;border-bottom:1px solid #21262d;display:flex;align-items:center;gap:9px;transition:background .1s}
.contact:hover{background:#1c2128}
.contact.active{background:#1f3a5f;border-left:3px solid #58a6ff}
.avatar{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#fff;flex-shrink:0}
.cinfo{flex:1;min-width:0}
.cname{font-size:12px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cparts{font-size:10px;color:#8b949e;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:1px}
.cbadge{background:#238636;color:#fff;font-size:10px;font-weight:700;padding:2px 6px;border-radius:10px;flex-shrink:0}

/* MAIN */
.main{flex:1;display:flex;flex-direction:column;overflow:hidden;position:relative}
.chat-header{padding:10px 16px;background:#161b22;border-bottom:1px solid #30363d;flex-shrink:0;display:flex;align-items:center;justify-content:space-between;gap:12px}
.chat-header-left{flex:1;min-width:0}
.chat-header .name{font-size:14px;font-weight:600}
.chat-header .parts{font-size:11px;color:#8b949e;margin-top:3px}
.chat-header .parts span{display:inline-block;background:#21262d;border-radius:4px;padding:1px 6px;margin:2px 2px 0 0;font-size:10px}
.chat-header .parts span.eu{background:#1a4731;color:#3fb950}

/* BOTÃO AVALIAR */
.btn-avaliar{background:#8957e5;color:#fff;border:none;border-radius:6px;padding:7px 14px;font-size:12px;font-weight:600;cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:background .15s;flex-shrink:0}
.btn-avaliar:hover{background:#a371f7}
.btn-avaliar:disabled{background:#30363d;color:#6e7681;cursor:not-allowed}
.btn-avaliar .spinner{width:12px;height:12px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}

/* MENSAGENS */
.messages{flex:1;overflow-y:auto;padding:16px 20px;display:flex;flex-direction:column;gap:2px;background:#0d1117}
.msg-wrap{display:flex;flex-direction:column;margin-bottom:4px}
.msg-wrap.sent{align-items:flex-end}
.msg-wrap.recv{align-items:flex-start}
.sender-name{font-size:10px;font-weight:700;margin-bottom:2px;padding:0 2px}
.msg-wrap.sent .sender-name{color:#3fb950}
.msg-wrap.recv .sender-name{color:#58a6ff}
.bubble{max-width:68%;padding:8px 12px;border-radius:12px;font-size:12.5px;line-height:1.55;word-break:break-word;white-space:pre-wrap;position:relative}
.bubble.recv{background:#21262d;border-top-left-radius:3px}
.bubble.sent{background:#1a4731;border-top-right-radius:3px}
.bubble .hora{font-size:10px;color:#8b949e;text-align:right;margin-top:4px}
.empty{flex:1;display:flex;align-items:center;justify-content:center;color:#484f58;font-size:13px;flex-direction:column;gap:10px}

/* PAINEL DE AVALIAÇÃO */
.eval-panel{position:absolute;top:0;right:0;width:400px;height:100%;background:#161b22;border-left:1px solid #30363d;display:flex;flex-direction:column;transform:translateX(100%);transition:transform .25s ease;z-index:10;overflow:hidden}
.eval-panel.open{transform:translateX(0)}
.eval-header{padding:12px 16px;border-bottom:1px solid #30363d;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
.eval-header span{font-size:13px;font-weight:600;color:#a371f7}
.eval-close{background:none;border:none;color:#8b949e;cursor:pointer;font-size:18px;line-height:1;padding:2px 6px}
.eval-close:hover{color:#e6edf3}
.eval-body{flex:1;overflow-y:auto;padding:16px}

/* SCORE GERAL */
.score-circle{width:72px;height:72px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;margin:0 auto 16px;border:3px solid}
.score-circle .sn{font-size:22px;font-weight:700}
.score-circle .sl{font-size:10px;color:#8b949e}

/* CRITÉRIOS */
.crit-list{margin-bottom:16px}
.crit-item{margin-bottom:10px}
.crit-label{display:flex;align-items:center;justify-content:space-between;font-size:11px;margin-bottom:4px}
.crit-name{color:#8b949e;text-transform:uppercase;letter-spacing:.4px}
.crit-note{font-weight:700;font-size:12px}
.crit-bar{height:4px;background:#21262d;border-radius:2px;overflow:hidden}
.crit-fill{height:100%;border-radius:2px;transition:width .4s ease}
.crit-obs{font-size:11px;color:#8b949e;margin-top:3px;line-height:1.4}

/* SEÇÕES */
.eval-section{margin-bottom:16px}
.eval-section h4{font-size:11px;text-transform:uppercase;letter-spacing:.6px;color:#8b949e;margin-bottom:8px;border-bottom:1px solid #21262d;padding-bottom:4px}
.eval-section ul{list-style:none}
.eval-section ul li{font-size:12px;line-height:1.5;padding:3px 0 3px 14px;position:relative;color:#e6edf3}
.eval-section ul li:before{content:'•';position:absolute;left:2px;color:#58a6ff}
.eval-section ul li.pos:before{color:#3fb950}
.eval-section ul li.opp:before{color:#f0883e}

/* OBJEÇÕES */
.obj-card{background:#0d1117;border:1px solid #30363d;border-radius:6px;padding:10px;margin-bottom:8px}
.obj-text{font-size:12px;font-weight:600;color:#e6edf3;margin-bottom:6px}
.obj-row{display:flex;gap:6px;margin-bottom:4px}
.obj-label{font-size:10px;font-weight:700;padding:2px 6px;border-radius:4px;white-space:nowrap}
.obj-label.dada{background:#21262d;color:#8b949e}
.obj-label.ideal{background:#1a4731;color:#3fb950}
.obj-val{font-size:11px;color:#c9d1d9;line-height:1.4}

/* FOLLOW-UP */
.followup-box{background:#0d1117;border:1px solid #30363d;border-radius:6px;padding:12px;font-size:12px;line-height:1.6;color:#e6edf3;white-space:pre-wrap;cursor:pointer;transition:border-color .15s}
.followup-box:hover{border-color:#58a6ff}
.followup-hint{font-size:10px;color:#484f58;margin-top:6px}

/* PLANO */
.plano-item{display:flex;align-items:flex-start;gap:8px;margin-bottom:8px}
.plano-num{width:20px;height:20px;border-radius:50%;background:#8957e5;color:#fff;font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.plano-txt{font-size:12px;color:#e6edf3;line-height:1.4}

::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-thumb{background:#30363d;border-radius:3px}
</style>
</head>
<body>
<div class="topbar">
  <span style="font-size:20px">💬</span>
  <div>
    <div style="font-size:15px;font-weight:600;color:#58a6ff">Germinare — WhatsApp</div>
    <div style="font-size:12px;color:#8b949e">""" + date + " &middot; " + str(len(chats)) + " conversas &middot; " + str(total_msgs) + """ mensagens</div>
  </div>
</div>
<div class="app">
  <div class="sidebar">
    <div class="sidebar-tools">
      <input type="text" id="search" placeholder="Buscar conversa..." oninput="filterChats()" />
    </div>
    <div class="contact-list" id="chatList"></div>
  </div>
  <div class="main">
    <div id="chatHeader" class="chat-header" style="display:none">
      <div class="chat-header-left">
        <div class="name" id="chatName"></div>
        <div class="parts" id="chatParts"></div>
      </div>
      <button class="btn-avaliar" id="btnAvaliar" onclick="avaliarConversa()">
        <span>✦</span> Avaliar conversa
      </button>
    </div>
    <div id="chatArea" class="empty">
      <div style="font-size:36px">💬</div>
      <div>Selecione uma conversa</div>
    </div>

    <!-- Painel de avaliação -->
    <div class="eval-panel" id="evalPanel">
      <div class="eval-header">
        <span>✦ Avaliação de Vendas</span>
        <button class="eval-close" onclick="fecharPainel()">✕</button>
      </div>
      <div class="eval-body" id="evalBody">
        <div style="color:#484f58;text-align:center;margin-top:40px;font-size:13px">Carregando análise...</div>
      </div>
    </div>
  </div>
</div>

<script>
var AVALIAR_URL='""" + AVALIAR_URL + """';
var COLORS=['#238636','#1f6feb','#d29922','#8957e5','#0a7e6b','#c9510c','#6e7681','#1a7f64'];
var DATA=""" + chats_js + """;
var filtered=DATA.slice();
var currentChat=null;

function initials(name){
  return String(name||'?').split(' ').slice(0,2).map(function(w){return w[0]||''}).join('').toUpperCase()||'?';
}
function esc(t){
  return String(t||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\\n/g,'<br>');
}

function renderList(list){
  var el=document.getElementById('chatList');
  el.innerHTML=list.map(function(c,i){
    var col=COLORS[i%COLORS.length];
    var parts=c.participantes.filter(function(p){return p!=='EU'}).slice(0,3).join(', ');
    var lastMsg=c.mensagens[c.mensagens.length-1];
    var prev=lastMsg&&lastMsg.texto?lastMsg.texto.substring(0,45):'[midia]';
    return '<div class="contact" onclick="openChat('+i+')" id="ci'+i+'">'
      +'<div class="avatar" style="background:'+col+'">'+initials(c.chat)+'</div>'
      +'<div class="cinfo">'
        +'<div class="cname">'+esc(c.chat)+'</div>'
        +'<div class="cparts">'+esc(parts||prev)+'</div>'
      +'</div>'
      +'<div class="cbadge">'+c.total+'</div>'
      +'</div>';
  }).join('');
}

function filterChats(){
  var q=document.getElementById('search').value.toLowerCase();
  filtered=DATA.filter(function(c){
    return c.chat.toLowerCase().indexOf(q)>=0
      || c.participantes.some(function(p){return p.toLowerCase().indexOf(q)>=0});
  });
  renderList(filtered);
}

function openChat(idx){
  document.querySelectorAll('.contact').forEach(function(el){el.classList.remove('active')});
  var el=document.getElementById('ci'+idx);
  if(el) el.classList.add('active');
  currentChat=filtered[idx];
  fecharPainel();

  document.getElementById('chatHeader').style.display='flex';
  document.getElementById('chatName').textContent=currentChat.chat;
  var partsHtml=currentChat.participantes.map(function(p){
    return '<span class="'+(p==='EU'?'eu':'')+'">'+(p==='EU'?'Vanessa':esc(p))+'</span>';
  }).join('');
  document.getElementById('chatParts').innerHTML=partsHtml;

  var area=document.getElementById('chatArea');
  area.className='messages';
  var html='';
  var prevSender='__init__';

  currentChat.mensagens.forEach(function(m){
    var isSent=m.from_me===true;
    var side=isSent?'sent':'recv';
    var nome=isSent?'Vanessa':esc(m.de);
    var txt=m.texto?esc(m.texto):'<em style="color:#6e7681">['+esc(m.tipo||'midia')+']</em>';
    var showLabel=(m.de!==prevSender);
    prevSender=m.de;
    html+='<div class="msg-wrap '+side+'">'
      +(showLabel?'<div class="sender-name">'+nome+'</div>':'')
      +'<div class="bubble '+side+'">'+txt
      +'<div class="hora">'+m.hora+'</div>'
      +'</div></div>';
  });

  area.innerHTML=html;
  area.scrollTop=area.scrollHeight;
}

function fecharPainel(){
  document.getElementById('evalPanel').classList.remove('open');
}

function scoreColor(n){
  if(n>=8) return '#3fb950';
  if(n>=6) return '#d29922';
  return '#f85149';
}

function barColor(n){
  if(n>=8) return '#238636';
  if(n>=6) return '#9e6a03';
  return '#da3633';
}

function critLabel(key){
  var m={
    abertura_rapport:'Abertura / Rapport',
    identificacao_necessidade:'Identificação de Necessidade',
    apresentacao_solucao:'Apresentação da Solução',
    contorno_objecao:'Contorno de Objeção',
    fechamento:'Fechamento',
    follow_up:'Follow-up'
  };
  return m[key]||key;
}

function renderEval(data){
  var nota=data.nota_geral||0;
  var cor=scoreColor(nota);

  var html='';

  // Score geral
  html+='<div class="score-circle" style="border-color:'+cor+';color:'+cor+'">'
    +'<div class="sn">'+nota.toFixed(1)+'</div>'
    +'<div class="sl">nota geral</div>'
    +'</div>';

  // Meta
  if(data.vendedor||data.produto_foco){
    html+='<div style="text-align:center;margin-bottom:16px">';
    if(data.vendedor) html+='<div style="font-size:12px;font-weight:600">'+esc(data.vendedor)+'</div>';
    if(data.contato) html+='<div style="font-size:11px;color:#8b949e">▸ '+esc(data.contato)+'</div>';
    if(data.produto_foco) html+='<div style="font-size:11px;color:#8b949e">'+esc(data.produto_foco)+'</div>';
    html+='</div>';
  }

  // Critérios
  if(data.criterios){
    html+='<div class="eval-section"><h4>Critérios</h4><div class="crit-list">';
    Object.keys(data.criterios).forEach(function(k){
      var c=data.criterios[k];
      var n=c.nota||0;
      var pct=(n/10*100)+'%';
      html+='<div class="crit-item">'
        +'<div class="crit-label"><span class="crit-name">'+critLabel(k)+'</span><span class="crit-note" style="color:'+scoreColor(n)+'">'+n+'</span></div>'
        +'<div class="crit-bar"><div class="crit-fill" style="width:'+pct+';background:'+barColor(n)+'"></div></div>'
        +(c.obs?'<div class="crit-obs">'+esc(c.obs)+'</div>':'')
        +'</div>';
    });
    html+='</div></div>';
  }

  // Positivos e oportunidades
  if(data.pontos_positivos&&data.pontos_positivos.length){
    html+='<div class="eval-section"><h4>✓ Pontos Positivos</h4><ul>';
    data.pontos_positivos.forEach(function(p){html+='<li class="pos">'+esc(p)+'</li>';});
    html+='</ul></div>';
  }
  if(data.oportunidades_perdidas&&data.oportunidades_perdidas.length){
    html+='<div class="eval-section"><h4>⚡ Oportunidades Perdidas</h4><ul>';
    data.oportunidades_perdidas.forEach(function(p){html+='<li class="opp">'+esc(p)+'</li>';});
    html+='</ul></div>';
  }

  // Objeções
  if(data.objecoes_identificadas&&data.objecoes_identificadas.length){
    html+='<div class="eval-section"><h4>🛡 Objeções</h4>';
    data.objecoes_identificadas.forEach(function(o){
      html+='<div class="obj-card">'
        +'<div class="obj-text">'+esc(o.objecao)+'</div>';
      if(o.resposta_dada){
        html+='<div class="obj-row"><span class="obj-label dada">Como reagiu</span><span class="obj-val">'+esc(o.resposta_dada)+'</span></div>';
      }
      if(o.resposta_ideal){
        html+='<div class="obj-row"><span class="obj-label ideal">Ideal</span><span class="obj-val">'+esc(o.resposta_ideal)+'</span></div>';
      }
      html+='</div>';
    });
    html+='</div>';
  }

  // Plano de ação
  if(data.plano_acao&&data.plano_acao.length){
    html+='<div class="eval-section"><h4>🎯 Plano de Ação</h4>';
    data.plano_acao.forEach(function(p,i){
      html+='<div class="plano-item">'
        +'<div class="plano-num">'+(i+1)+'</div>'
        +'<div class="plano-txt">'+esc(p)+'</div>'
        +'</div>';
    });
    html+='</div>';
  }

  // Follow-up sugerido
  if(data.mensagem_followup_sugerida){
    html+='<div class="eval-section"><h4>💬 Follow-up Sugerido</h4>'
      +'<div class="followup-box" onclick="copiarFollowup(this)" title="Clique para copiar">'+esc(data.mensagem_followup_sugerida)+'</div>'
      +'<div class="followup-hint">Clique para copiar a mensagem</div>'
      +'</div>';
  }

  return html;
}

function copiarFollowup(el){
  var text=el.innerText;
  navigator.clipboard.writeText(text).then(function(){
    var orig=el.style.borderColor;
    el.style.borderColor='#3fb950';
    setTimeout(function(){el.style.borderColor=orig;},1200);
  });
}

function avaliarConversa(){
  if(!currentChat) return;
  var btn=document.getElementById('btnAvaliar');
  btn.disabled=true;
  btn.innerHTML='<div class="spinner"></div> Analisando...';

  document.getElementById('evalBody').innerHTML='<div style="color:#484f58;text-align:center;margin-top:40px;font-size:13px">⏳ Processando com IA...</div>';
  document.getElementById('evalPanel').classList.add('open');

  var payload={chat:currentChat.chat, mensagens:currentChat.mensagens};

  fetch(AVALIAR_URL, {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify(payload)
  })
  .then(function(r){
    if(!r.ok) return r.json().then(function(e){throw new Error(e.error||'Erro '+r.status)});
    return r.json();
  })
  .then(function(data){
    document.getElementById('evalBody').innerHTML=renderEval(data);
  })
  .catch(function(err){
    document.getElementById('evalBody').innerHTML='<div style="color:#f85149;text-align:center;margin-top:40px;font-size:13px">❌ '+err.message+'</div>';
  })
  .finally(function(){
    btn.disabled=false;
    btn.innerHTML='<span>✦</span> Avaliar conversa';
  });
}

renderList(DATA);
</script>
</body>
</html>"""

with open("C:/Users/sorna/Documents/germinare-supabase/whatsapp-viewer.html", "w", encoding="utf-8") as f:
    f.write(html)

print("OK - " + str(len(html)) + " chars, " + str(len(chats)) + " conversas")
