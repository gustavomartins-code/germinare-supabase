import { serve } from "https://deno.land/std@0.168.0/http/server.ts";

const GEMINI_API_KEY = Deno.env.get("GEMINI_API_KEY") ?? "";

const SYSTEM_PROMPT = `Você é um especialista em treinamento de vendas B2B no mercado de grãos e rações (DDGs, farelo de soja, milho, casca de soja, caroço de algodão).
A empresa Germinare atua como broker: concilia demanda do comprador com oferta do fornecedor, negociando preço, prazo de pagamento, padrão de qualidade e mês de embarque.

Avalie a transcrição de conversa de WhatsApp de um vendedor usando os critérios abaixo. Responda SEMPRE em JSON puro, sem markdown, sem texto fora do JSON.

CRITÉRIOS DE AVALIAÇÃO (0–10 cada):
1. abertura_rapport: Qualidade da abertura e construção de relacionamento
2. identificacao_necessidade: Uso de perguntas para identificar volume, produto, prazo, preço-alvo e condições
3. apresentacao_solucao: Clareza na apresentação da oferta (produto, preço, condições, embarque)
4. contorno_objecao: Eficácia no tratamento de objeções de preço, prazo ou disponibilidade
5. fechamento: Tentativas de avanço ou fechamento do negócio
6. follow_up: Combinação de próximos passos claros

FORMATO DE RESPOSTA (JSON exato):
{
  "vendedor": "<nome do vendedor identificado na conversa>",
  "contato": "<nome do cliente/contato>",
  "produto_foco": "<produto(s) em negociação>",
  "nota_geral": <média ponderada 0-10, 1 casa decimal>,
  "criterios": {
    "abertura_rapport": {"nota": <0-10>, "obs": "<1-2 frases>"},
    "identificacao_necessidade": {"nota": <0-10>, "obs": "<1-2 frases>"},
    "apresentacao_solucao": {"nota": <0-10>, "obs": "<1-2 frases>"},
    "contorno_objecao": {"nota": <0-10>, "obs": "<1-2 frases>"},
    "fechamento": {"nota": <0-10>, "obs": "<1-2 frases>"},
    "follow_up": {"nota": <0-10>, "obs": "<1-2 frases>"}
  },
  "pontos_positivos": ["<ponto 1>", "<ponto 2>"],
  "oportunidades_perdidas": ["<oportunidade 1>", "<oportunidade 2>"],
  "objecoes_identificadas": [
    {"objecao": "<texto da objeção>", "resposta_dada": "<como o vendedor reagiu>", "resposta_ideal": "<como deveria ter respondido>"}
  ],
  "plano_acao": ["<ação 1 para melhorar>", "<ação 2>", "<ação 3>"],
  "mensagem_followup_sugerida": "<mensagem pronta para o vendedor enviar como continuidade>"
}`;

serve(async (req: Request) => {
  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  };

  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  if (req.method !== "POST") {
    return new Response("Method Not Allowed", { status: 405, headers: corsHeaders });
  }

  let body: { chat: string; mensagens: Array<{ hora: string; de: string; from_me: boolean; texto: string | null; tipo: string | null }> };
  try {
    body = await req.json();
  } catch {
    return new Response("Invalid JSON", { status: 400, headers: corsHeaders });
  }

  if (!body.mensagens || body.mensagens.length === 0) {
    return json({ error: "Sem mensagens para avaliar" }, 400, corsHeaders);
  }

  // Monta a transcrição formatada
  const transcricao = body.mensagens
    .map((m) => {
      const remetente = m.from_me ? "Vanessa (vendedora)" : m.de;
      const texto = m.texto ?? `[${m.tipo ?? "mídia"}]`;
      return `[${m.hora}] ${remetente}: ${texto}`;
    })
    .join("\n");

  const prompt = `Analise esta conversa de WhatsApp do vendedor da Germinare com o contato "${body.chat}":\n\n${transcricao}`;

  if (!GEMINI_API_KEY) {
    return json({ error: "GEMINI_API_KEY não configurada" }, 500, corsHeaders);
  }

  const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}`;

  const geminiBody = {
    system_instruction: { parts: [{ text: SYSTEM_PROMPT }] },
    contents: [{ parts: [{ text: prompt }] }],
    generationConfig: {
      temperature: 0.3,
      responseMimeType: "application/json",
    },
  };

  let result: Record<string, unknown>;
  try {
    const resp = await fetch(geminiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(geminiBody),
    });

    if (!resp.ok) {
      const errText = await resp.text();
      console.error("Gemini error:", errText);
      return json({ error: `Gemini API error: ${resp.status}` }, 502, corsHeaders);
    }

    const geminiResp = await resp.json();
    const rawText = geminiResp?.candidates?.[0]?.content?.parts?.[0]?.text ?? "{}";
    result = JSON.parse(rawText);
  } catch (e) {
    console.error("Parse error:", e);
    return json({ error: "Falha ao processar resposta da IA" }, 500, corsHeaders);
  }

  return json(result, 200, corsHeaders);
});

function json(body: unknown, status = 200, extra: Record<string, string> = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", ...extra },
  });
}
