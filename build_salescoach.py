"""
Pipeline SalesCoach Germinare
F1 — Filtro estrutural (sem IA): elimina < 4 msgs
F2 — Filtro semântico batch (1 chamada Gemini): tem_vendedor_germinare + tem_negociacao
F3 — Avaliação completa (1 chamada por conversa que passou F2)
"""

import json
import urllib.request
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
DATA_FILE   = "C:/Users/sorna/Documents/germinare-supabase/data_chats.json"
OUTPUT_FILE = "C:/Users/sorna/Documents/germinare-supabase/salescoach.html"
DATE        = "2026-05-12"

# ─── helpers ──────────────────────────────────────────────────────────────────

def gemini(prompt, system=None):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"},
    }
    if system:
        body["system_instruction"] = {"parts": [{"text": system}]}
    req = urllib.request.Request(
        GEMINI_URL,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        resp = json.loads(r.read())
    raw = resp["candidates"][0]["content"]["parts"][0]["text"]
    return json.loads(raw)


def initials(name):
    parts = str(name or "?").split()[:2]
    return "".join(p[0] for p in parts if p).upper() or "?"


# ─── F1: filtro estrutural ─────────────────────────────────────────────────────

def f1_estrutural(chats, min_msgs=4):
    passed = [c for c in chats if c["total"] >= min_msgs]
    print(f"F1 estrutural: {len(chats)} → {len(passed)} (removidos {len(chats)-len(passed)} com <{min_msgs} msgs)")
    return passed


# ─── F2: filtro semântico batch ────────────────────────────────────────────────

F2_SYSTEM = """Você analisa conversas de WhatsApp da empresa Germinare (broker de grãos/rações).
Retorne JSON puro, sem markdown.

Para cada conversa avalie:
- tem_vendedor_germinare: true se alguém da Germinare (Vanessa, Leandro, Thais, Daiane, Fabricio, Andrêssa, Larissa, Giulliana, Andres, Conrado) está presente e fala ativamente
- tem_negociacao: true se há intenção comercial real — menção a preço, volume, produto, BID, contrato, proposta, objeção, fechamento ou follow-up de venda

Retorne array: [{"chat": "<nome>", "tem_vendedor_germinare": bool, "tem_negociacao": bool}]"""

def f2_semantico(chats):
    # Monta resumo compacto de cada conversa para o batch
    resumos = []
    for c in chats:
        msgs_sample = c["mensagens"][:8]  # primeiras 8 msgs bastam para classificar
        linhas = [f"[{m['hora']}] {m['de']}: {(m['texto'] or '[midia]')[:80]}" for m in msgs_sample]
        resumos.append({
            "chat": c["chat"],
            "participantes": c["participantes"],
            "amostra": "\n".join(linhas),
        })

    prompt = "Classifique cada conversa abaixo:\n\n" + "\n\n---\n\n".join(
        f"CHAT: {r['chat']}\nParticipantes: {', '.join(r['participantes'])}\n{r['amostra']}"
        for r in resumos
    )

    resultado = gemini(prompt, system=F2_SYSTEM)

    # Indexa por nome do chat
    idx = {item["chat"]: item for item in resultado}
    passed = [c for c in chats if idx.get(c["chat"], {}).get("tem_vendedor_germinare") and idx.get(c["chat"], {}).get("tem_negociacao")]
    removidos = [c["chat"] for c in chats if c["chat"] not in [p["chat"] for p in passed]]
    print(f"F2 semântico:  {len(chats)} → {len(passed)} (removidos: {', '.join(removidos)})")
    return passed


# ─── F3: avaliação completa ────────────────────────────────────────────────────

F3_SYSTEM = """Você é especialista em vendas B2B no mercado de grãos e rações (DDGs, farelo, milho, casca de soja, caroço de algodão).
A Germinare é um broker: vendedor identifica demanda → repassa BID → broker negocia com fornecedor → fecha.
Foco principal: contorno de objeções e conversão.
Retorne JSON puro, sem markdown."""

F3_SCHEMA = """{
  "score": <0-10 com 1 decimal>,
  "scoreLabel": "<3-4 palavras>",
  "summary": "<2 frases objetivas>",
  "status": "<Fechado|Em andamento|Travado|Perdido>",
  "vendedor": "<nome identificado>",
  "produto": "<produto(s)>",
  "metrics": {
    "respostaMed": "<ex: 4min>",
    "objecoes": "<número>",
    "conversao": "<Sim|Não|Parcial>",
    "msgs": "<número>"
  },
  "improvements": [
    {
      "type": "<good|warn|bad>",
      "label": "<✅ Ponto Forte|⚠️ Atenção|🚨 Melhora Urgente>",
      "title": "<título curto>",
      "text": "<1-2 frases>",
      "tip": "<dica prática e específica>",
      "msgRef": "<trecho exato de uma mensagem da conversa>"
    }
  ],
  "objecoes": [
    {"objecao": "<texto>", "resposta_dada": "<como reagiu>", "resposta_ideal": "<como deveria>"}
  ],
  "followupMsg": "<mensagem pronta para enviar agora>"
}"""

def f3_avaliar(chat):
    transcricao = "\n".join(
        f"[{m['hora']}] {m['de']}: {m['texto'] or '[' + (m['tipo'] or 'midia') + ']'}"
        for m in chat["mensagens"]
    )
    prompt = (
        f"Avalie esta conversa de WhatsApp da Germinare com '{chat['chat']}'.\n\n"
        f"TRANSCRIÇÃO:\n{transcricao}\n\n"
        f"Retorne este JSON exato:\n{F3_SCHEMA}"
    )
    return gemini(prompt, system=F3_SYSTEM)


# ─── Build HTML ────────────────────────────────────────────────────────────────

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

def score_color(s):
    if s >= 8: return "#25d366"
    if s >= 6: return "#f59e0b"
    return "#ef4444"

def score_class(s):
    if s >= 8: return "score-good"
    if s >= 6: return "score-mid"
    return "score-low"

def arc_offset(score):
    return 150.8 - (score / 10) * 150.8

def build_conv_js(chat, eval_data, idx):
    msgs_js = []
    for m in chat["mensagens"]:
        msgs_js.append({
            "side": "sent" if m.get("from_me") else "recv",
            "sender": "Vanessa" if m.get("from_me") else (m.get("de") or ""),
            "text": (m.get("texto") or f"[{m.get('tipo') or 'midia'}]"),
            "time": m.get("hora", ""),
        })

    last_msg = chat["mensagens"][-1] if chat["mensagens"] else {}
    preview = (last_msg.get("texto") or "")[:55] or "[mídia]"

    conv = {
        "id": idx,
        "chat": chat["chat"],
        "initials": initials(chat["chat"]),
        "avatarGrad": AVATAR_GRADS[idx % len(AVATAR_GRADS)],
        "time": (chat["mensagens"][-1].get("hora") if chat["mensagens"] else ""),
        "preview": preview,
        "score": eval_data.get("score", 0),
        "msgs": chat["total"],
        "status": eval_data.get("status", "Em andamento"),
        "tags": [p for p in [eval_data.get("produto"), eval_data.get("status")] if p],
        "scoreLabel": eval_data.get("scoreLabel", ""),
        "summary": eval_data.get("summary", ""),
        "vendedor": eval_data.get("vendedor", ""),
        "metrics": eval_data.get("metrics", {}),
        "improvements": eval_data.get("improvements", []),
        "objecoes": eval_data.get("objecoes", []),
        "followupMsg": eval_data.get("followupMsg", ""),
        "messages": msgs_js,
        "arcOffset": arc_offset(eval_data.get("score", 0)),
        "arcColor": score_color(eval_data.get("score", 0)),
        "scoreColor": score_color(eval_data.get("score", 0)),
    }
    return conv


def build_html(conversations_js, date, total_original, total_avaliados):
    conv_data = json.dumps(conversations_js, ensure_ascii=False, separators=(",", ":"))

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SalesCoach AI — Germinare</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');
  :root{{--bg:#0d0f12;--surface:#161a1f;--surface2:#1e2329;--border:#2a2f38;--text:#e8ecf0;--muted:#6b7a8d;--accent:#25d366;--accent2:#128c7e;--warn:#f59e0b;--danger:#ef4444;--info:#3b82f6;--highlight:rgba(37,211,102,0.12)}}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--text);height:100vh;overflow:hidden;display:flex;flex-direction:column}}
  .topbar{{background:var(--surface);border-bottom:1px solid var(--border);padding:0 20px;height:52px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}}
  .topbar-brand{{display:flex;align-items:center;gap:10px}}
  .topbar-logo{{width:28px;height:28px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px}}
  .topbar-title{{font-family:'Syne',sans-serif;font-weight:700;font-size:15px;letter-spacing:-.3px}}
  .topbar-title span{{color:var(--accent)}}
  .topbar-meta{{display:flex;gap:12px;align-items:center}}
  .pill{{background:var(--surface2);border:1px solid var(--border);border-radius:20px;padding:4px 14px;font-size:12px;color:var(--muted);font-weight:500}}
  .app-layout{{display:flex;flex:1;overflow:hidden}}
  /* LISTA */
  .conv-list{{width:300px;flex-shrink:0;background:var(--surface);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}}
  .conv-list-header{{padding:14px 16px 10px;border-bottom:1px solid var(--border);flex-shrink:0}}
  .conv-list-header h3{{font-family:'Syne',sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin-bottom:10px}}
  .search-box{{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:7px 12px;display:flex;align-items:center;gap:8px}}
  .search-box input{{background:transparent;border:none;outline:none;color:var(--text);font-size:12px;width:100%;font-family:'DM Sans',sans-serif}}
  .search-box input::placeholder{{color:var(--muted)}}
  .conv-items{{flex:1;overflow-y:auto;padding:8px 0}}
  .conv-items::-webkit-scrollbar{{width:4px}}
  .conv-items::-webkit-scrollbar-thumb{{background:var(--border);border-radius:4px}}
  .conv-item{{padding:12px 16px;cursor:pointer;border-left:3px solid transparent;transition:all .15s}}
  .conv-item:hover{{background:var(--surface2)}}
  .conv-item.active{{background:var(--highlight);border-left-color:var(--accent)}}
  .conv-item-top{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px}}
  .conv-name{{font-weight:600;font-size:13px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:175px}}
  .conv-time{{font-size:11px;color:var(--muted);flex-shrink:0}}
  .conv-preview{{font-size:11.5px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:8px}}
  .conv-footer{{display:flex;justify-content:space-between;align-items:center}}
  .score-badge{{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:2px 8px;border-radius:20px}}
  .score-good{{background:rgba(37,211,102,.15);color:var(--accent)}}
  .score-mid{{background:rgba(245,158,11,.15);color:var(--warn)}}
  .score-low{{background:rgba(239,68,68,.12);color:var(--danger)}}
  .tag-chips{{display:flex;gap:4px}}
  .tag-chip{{font-size:10px;padding:2px 6px;border-radius:4px;background:var(--surface);border:1px solid var(--border);color:var(--muted)}}
  /* MAIN */
  .conv-main{{flex:1;display:flex;flex-direction:column;overflow:hidden;border-right:1px solid var(--border)}}
  .conv-header{{padding:12px 20px;background:var(--surface);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-shrink:0}}
  .conv-header-left{{display:flex;align-items:center;gap:12px}}
  .contact-avatar{{width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px}}
  .contact-info h4{{font-size:14px;font-weight:600}}
  .contact-info p{{font-size:11px;color:var(--muted)}}
  .status-pill{{font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px}}
  .sp-Fechado{{background:rgba(37,211,102,.15);color:var(--accent)}}
  .sp-Emandamento{{background:rgba(59,130,246,.15);color:var(--info)}}
  .sp-Travado{{background:rgba(245,158,11,.15);color:var(--warn)}}
  .sp-Perdido{{background:rgba(239,68,68,.12);color:var(--danger)}}
  .messages-area{{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:10px}}
  .messages-area::-webkit-scrollbar{{width:4px}}
  .messages-area::-webkit-scrollbar-thumb{{background:var(--border);border-radius:4px}}
  .day-sep{{display:flex;align-items:center;gap:10px;margin:4px 0 8px}}
  .day-sep-line{{flex:1;height:1px;background:var(--border)}}
  .day-sep-label{{font-size:11px;color:var(--muted);background:var(--surface2);padding:2px 10px;border-radius:10px;border:1px solid var(--border)}}
  .msg-row{{display:flex;gap:8px;max-width:78%}}
  .msg-row.sent{{align-self:flex-end;flex-direction:row-reverse}}
  .msg-row.received{{align-self:flex-start}}
  .msg-meta{{font-size:10px;color:var(--muted);margin-bottom:3px;padding:0 4px}}
  .msg-row.sent .msg-meta{{text-align:right}}
  .msg-bubble{{padding:10px 14px;border-radius:12px;font-size:13px;line-height:1.5;white-space:pre-wrap;word-break:break-word}}
  .msg-row.sent .msg-bubble{{background:#1d4a2e;border-bottom-right-radius:3px}}
  .msg-row.received .msg-bubble{{background:var(--surface2);border:1px solid var(--border);border-bottom-left-radius:3px}}
  .msg-bubble.hl-good{{background:rgba(37,211,102,.18)!important;border:1.5px solid rgba(37,211,102,.45)!important}}
  .msg-bubble.hl-warn{{background:rgba(245,158,11,.15)!important;border:1.5px solid rgba(245,158,11,.4)!important}}
  .msg-bubble.hl-bad{{background:rgba(239,68,68,.14)!important;border:1.5px solid rgba(239,68,68,.4)!important}}
  /* FOLLOWUP */
  .followup-area{{border-top:1px solid var(--border);padding:12px 20px;background:var(--surface);flex-shrink:0}}
  .followup-label{{font-size:10px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.8px;margin-bottom:6px}}
  .followup-box{{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:10px 14px;font-size:12px;line-height:1.55;color:var(--text);display:flex;align-items:flex-start;justify-content:space-between;gap:10px;transition:border-color .15s}}
  .followup-box:hover{{border-color:var(--accent)}}
  .followup-box span{{flex:1}}
  .copy-btn{{font-size:10px;padding:3px 8px;border-radius:4px;background:rgba(37,211,102,.15);color:var(--accent);border:none;cursor:pointer;font-family:'DM Sans',sans-serif;font-weight:600;white-space:nowrap;flex-shrink:0}}
  .copy-btn:hover{{background:rgba(37,211,102,.3)}}
  /* PAINEL */
  .synthesis-panel{{width:290px;flex-shrink:0;background:var(--surface);display:flex;flex-direction:column;overflow:hidden}}
  .synth-header{{padding:14px 16px 12px;border-bottom:1px solid var(--border);flex-shrink:0}}
  .synth-header h3{{font-family:'Syne',sans-serif;font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:12px}}
  .score-ring-wrap{{display:flex;align-items:center;gap:14px}}
  .score-ring{{position:relative;width:58px;height:58px;flex-shrink:0}}
  .score-ring svg{{transform:rotate(-90deg)}}
  .score-ring-label{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-size:17px;font-weight:800}}
  .score-meta h4{{font-family:'Syne',sans-serif;font-size:14px;font-weight:800}}
  .score-meta p{{font-size:11px;color:var(--muted);margin-top:2px}}
  .synth-body{{flex:1;overflow-y:auto;padding:14px 16px;display:flex;flex-direction:column;gap:16px}}
  .synth-body::-webkit-scrollbar{{width:4px}}
  .synth-body::-webkit-scrollbar-thumb{{background:var(--border);border-radius:4px}}
  .synth-section h5{{font-family:'Syne',sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:8px}}
  .summary-text{{font-size:12.5px;line-height:1.6;color:#b0bac6}}
  .improve-item{{border:1px solid var(--border);border-radius:10px;padding:10px 12px;background:var(--surface2);cursor:pointer;transition:all .2s;position:relative;overflow:hidden;margin-bottom:8px}}
  .improve-item::before{{content:'';position:absolute;left:0;top:0;bottom:0;width:3px}}
  .improve-item.good::before{{background:var(--accent)}}
  .improve-item.warn::before{{background:var(--warn)}}
  .improve-item.bad::before{{background:var(--danger)}}
  .improve-item:hover{{border-color:var(--accent);transform:translateX(2px)}}
  .il-good{{color:var(--accent)}}
  .il-warn{{color:var(--warn)}}
  .il-bad{{color:var(--danger)}}
  .improve-title{{font-size:12.5px;font-weight:600;margin-bottom:4px}}
  .improve-text{{font-size:11.5px;color:var(--muted);line-height:1.5}}
  .improve-tip{{margin-top:6px;font-size:11px;color:rgba(37,211,102,.75);line-height:1.4}}
  .metrics-row{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}
  .metric-card{{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:10px 12px}}
  .metric-card-label{{font-size:10px;color:var(--muted);font-weight:500}}
  .metric-card-value{{font-family:'Syne',sans-serif;font-size:17px;font-weight:800;margin-top:2px}}
  .mv-good{{color:var(--accent)}}
  .mv-warn{{color:var(--warn)}}
  .mv-bad{{color:var(--danger)}}
  .metric-card-sub{{font-size:10px;color:var(--muted);margin-top:1px}}
  .obj-card{{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:10px;margin-bottom:8px}}
  .obj-label{{font-size:10px;font-weight:700;padding:2px 6px;border-radius:4px;white-space:nowrap}}
  .obj-label.dada{{background:var(--surface2);color:var(--muted)}}
  .obj-label.ideal{{background:rgba(37,211,102,.15);color:var(--accent)}}
  .empty-state{{flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px;color:var(--muted);font-size:13px}}
  @keyframes flash{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
  .flash{{animation:flash .4s 2}}
</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-brand">
    <div class="topbar-logo">🌱</div>
    <div class="topbar-title">Sales<span>Coach</span> AI — Germinare</div>
  </div>
  <div class="topbar-meta">
    <div class="pill">📅 {date}</div>
    <div class="pill">✦ {total_avaliados} negociações de {total_original} conversas</div>
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
var CONVS={conv_data};
var display=CONVS.slice();
var activeId=-1;
function sc(s){{return s>=8?'score-good':s>=6?'score-mid':'score-low'}}
function arc(s){{return 150.8-(s/10)*150.8}}
function col(s){{return s>=8?'var(--accent)':s>=6?'var(--warn)':'var(--danger)'}}
function esc(t){{return String(t||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}
function renderList(){{
  document.getElementById('convList').innerHTML=display.map(function(c,i){{
    return '<div class="conv-item '+(c.id===activeId?'active':'')+'" onclick="selConv('+c.id+')">'
      +'<div class="conv-item-top"><div class="conv-name">'+esc(c.chat)+'</div><div class="conv-time">'+c.time+'</div></div>'
      +'<div class="conv-preview">'+esc(c.preview)+'</div>'
      +'<div class="conv-footer">'
        +'<div class="score-badge '+sc(c.score)+'">⭐ '+c.score+'</div>'
        +'<div class="tag-chips">'+c.tags.map(function(t){{return '<div class="tag-chip">'+esc(t)+'</div>'}}).join('')+'</div>'
      +'</div></div>';
  }}).join('');
}}
function filterList(){{
  var q=document.getElementById('searchInput').value.toLowerCase();
  display=CONVS.filter(function(c){{return c.chat.toLowerCase().includes(q)||c.tags.join(' ').toLowerCase().includes(q)}});
  renderList();
}}
function selConv(id){{
  activeId=id;
  var c=CONVS.find(function(x){{return x.id===id}});
  if(!c) return;
  document.getElementById('convHeader').style.display='flex';
  document.getElementById('convAvatar').textContent=c.initials;
  document.getElementById('convAvatar').style.background=c.avatarGrad;
  document.getElementById('convContactName').textContent=c.chat;
  document.getElementById('convContactSub').textContent=c.msgs+' mensagens · '+c.vendedor;
  var sp=c.status.replace(/ /g,'');
  document.getElementById('convStatusPill').innerHTML='<div class="status-pill sp-'+sp+'">'+c.status+'</div>';
  // msgs
  document.getElementById('emptyState').style.display='none';
  var area=document.getElementById('messagesArea');
  area.style.display='flex';
  area.innerHTML='<div class="day-sep"><div class="day-sep-line"></div><div class="day-sep-label">'+esc(c.chat)+' · {date}'+'</div><div class="day-sep-line"></div></div>'
    +c.messages.map(function(m,i){{
      var impIdx=c.improvements.findIndex(function(imp){{return imp.msgRef&&m.text.includes(imp.msgRef.substring(0,30))}});
      var hl=impIdx>=0?(' hl-'+c.improvements[impIdx].type):'';
      return '<div class="msg-row '+m.side+'" id="msg-'+id+'-'+i+'">'
        +'<div style="display:flex;flex-direction:column;'+(m.side==='sent'?'align-items:flex-end':'')+'">'
        +'<div class="msg-meta">'+esc(m.sender)+' · '+m.time+'</div>'
        +'<div class="msg-bubble'+hl+'"'+(impIdx>=0?' onclick="fromMsg('+impIdx+','+id+','+i+')"':'')+'>'+esc(m.text)
        +(impIdx>=0?'<div style="margin-top:6px"><span style="font-size:10px;font-weight:700;padding:2px 7px;border-radius:4px;cursor:pointer;background:rgba(37,211,102,.15);color:var(--accent)" onclick="fromMsg('+impIdx+','+id+','+i+')">'+esc(c.improvements[impIdx].label)+' →</span></div>':'')
        +'</div></div></div>';
    }}).join('');
  area.scrollTop=area.scrollHeight;
  // followup
  document.getElementById('followupArea').style.display='block';
  document.getElementById('followupText').textContent=c.followupMsg;
  // score ring
  document.getElementById('scoreArc').style.stroke=c.arcColor;
  document.getElementById('scoreArc').setAttribute('stroke-dashoffset',c.arcOffset);
  document.getElementById('scoreLabel').textContent=c.score;
  document.getElementById('scoreLabel').style.color=c.scoreColor;
  document.getElementById('scoreTitle').textContent=c.scoreLabel;
  document.getElementById('scoreTitle').style.color=c.scoreColor;
  document.getElementById('scoreSubtitle').textContent=c.status+' · '+c.msgs+' msgs';
  // synth
  var m=c.metrics||{{}};
  document.getElementById('synthBody').innerHTML=
    '<div class="synth-section"><h5>📋 Síntese</h5><p class="summary-text">'+esc(c.summary)+'</p></div>'
    +'<div class="synth-section"><h5>📊 Métricas</h5><div class="metrics-row">'
      +'<div class="metric-card"><div class="metric-card-label">Resposta Média</div><div class="metric-card-value '+(parseFloat(m.respostaMed)<5?'mv-good':'mv-warn')+'">'+esc(m.respostaMed||'—')+'</div></div>'
      +'<div class="metric-card"><div class="metric-card-label">Objeções</div><div class="metric-card-value '+(parseInt(m.objecoes)===0?'mv-good':parseInt(m.objecoes)>1?'mv-bad':'mv-warn')+'">'+esc(m.objecoes||'0')+'</div></div>'
      +'<div class="metric-card"><div class="metric-card-label">Mensagens</div><div class="metric-card-value">'+esc(m.msgs||c.msgs)+'</div></div>'
      +'<div class="metric-card"><div class="metric-card-label">Conversão</div><div class="metric-card-value '+(m.conversao==='Sim'?'mv-good':m.conversao==='Parcial'?'mv-warn':'mv-bad')+'">'+esc(m.conversao||'—')+'</div></div>'
    +'</div></div>'
    +'<div class="synth-section"><h5>💡 Análise</h5>'
      +c.improvements.map(function(imp,idx){{
        return '<div class="improve-item '+imp.type+'" id="imp-'+id+'-'+idx+'" onclick="fromImp('+idx+','+id+')">'
          +'<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px">'
          +'<span style="font-size:11px;font-weight:700" class="il-'+imp.type+'">'+esc(imp.label)+'</span>'
          +'<span style="font-size:12px;color:var(--muted)">↗</span></div>'
          +'<div class="improve-title">'+esc(imp.title)+'</div>'
          +'<div class="improve-text">'+esc(imp.text)+'</div>'
          +'<div class="improve-tip">💡 '+esc(imp.tip)+'</div>'
          +'</div>';
      }}).join('')
    +'</div>'
    +(c.objecoes&&c.objecoes.length?
      '<div class="synth-section"><h5>🛡 Objeções</h5>'
      +c.objecoes.map(function(o){{
        return '<div class="obj-card">'
          +'<div style="font-size:12px;font-weight:600;margin-bottom:6px">'+esc(o.objecao)+'</div>'
          +(o.resposta_dada?'<div style="display:flex;gap:6px;margin-bottom:4px;align-items:flex-start"><span class="obj-label dada">Como reagiu</span><span style="font-size:11px;color:#b0bac6;line-height:1.4">'+esc(o.resposta_dada)+'</span></div>':'')
          +(o.resposta_ideal?'<div style="display:flex;gap:6px;align-items:flex-start"><span class="obj-label ideal">Ideal</span><span style="font-size:11px;color:#b0bac6;line-height:1.4">'+esc(o.resposta_ideal)+'</span></div>':'')
          +'</div>';
      }}).join('')+'</div>'
    :'');
  renderList();
}}
function fromImp(impIdx,convId){{
  document.querySelectorAll('.improve-item').forEach(function(e){{e.style.boxShadow=''}});
  var ie=document.getElementById('imp-'+convId+'-'+impIdx);
  if(ie) ie.style.boxShadow='0 0 0 2px rgba(37,211,102,.3)';
  var c=CONVS.find(function(x){{return x.id===convId}});
  if(!c) return;
  var imp=c.improvements[impIdx];
  var mIdx=c.messages.findIndex(function(m){{return imp.msgRef&&m.text.includes(imp.msgRef.substring(0,30))}});
  if(mIdx>=0){{
    var me=document.getElementById('msg-'+convId+'-'+mIdx);
    if(me){{me.scrollIntoView({{behavior:'smooth',block:'center'}});me.classList.add('flash');setTimeout(function(){{me.classList.remove('flash')}},900)}}
  }}
}}
function fromMsg(impIdx,convId,msgIdx){{
  fromImp(impIdx,convId);
}}
function copyFollowup(){{
  var text=document.getElementById('followupText').textContent;
  navigator.clipboard.writeText(text).then(function(){{
    var btn=document.querySelector('.copy-btn');
    btn.textContent='Copiado ✓';
    setTimeout(function(){{btn.textContent='Copiar'}},1500);
  }});
}}
renderList();
if(CONVS.length>0) selConv(CONVS[0].id);
</script>
</body>
</html>"""


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    if not GEMINI_API_KEY:
        print("ERRO: defina a variável GEMINI_API_KEY antes de rodar.")
        print("  export GEMINI_API_KEY=AIza...")
        return

    print(f"\n=== SalesCoach Pipeline — {DATE} ===\n")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        chats = json.load(f)
    print(f"Carregadas: {len(chats)} conversas")

    # F1
    after_f1 = f1_estrutural(chats, min_msgs=4)

    # F2
    after_f2 = f2_semantico(after_f1)

    if not after_f2:
        print("Nenhuma conversa passou os filtros.")
        return

    # F3
    print(f"\nF3 avaliação: rodando {len(after_f2)} conversas...")
    conversations_js = []
    for i, chat in enumerate(after_f2):
        print(f"  [{i+1}/{len(after_f2)}] {chat['chat']}...", end=" ", flush=True)
        try:
            eval_data = f3_avaliar(chat)
            conversations_js.append(build_conv_js(chat, eval_data, i))
            print(f"score={eval_data.get('score', '?')} ✓")
        except Exception as e:
            print(f"ERRO: {e}")

    # Build HTML
    html = build_html(conversations_js, DATE, len(chats), len(after_f2))
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n✅ Gerado: {OUTPUT_FILE}")
    print(f"   {len(chats)} conversas → {len(after_f1)} pós-F1 → {len(after_f2)} pós-F2 → {len(conversations_js)} avaliadas")


if __name__ == "__main__":
    main()
