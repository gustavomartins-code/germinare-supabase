import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const SUPABASE_URL = Deno.env.get("SUPABASE_URL") ?? "";
const SUPABASE_SERVICE_ROLE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";
const PAGE_SIZE = 1000;

serve(async (req: Request) => {
  if (req.method !== "GET") {
    return json({ error: "Method Not Allowed" }, 405);
  }

  const url = new URL(req.url);
  const sender_name = url.searchParams.get("sender_name");
  const date = url.searchParams.get("date"); // YYYY-MM-DD, default = hoje (BRT)
  const connected_phone = url.searchParams.get("connected_phone");

  // Data no fuso Brasil (UTC-3)
  const targetDate = date ?? new Date(Date.now() - 3 * 60 * 60 * 1000)
    .toISOString()
    .slice(0, 10);

  const dayStart = `${targetDate}T03:00:00.000Z`; // 00:00 BRT = 03:00 UTC
  const dayEnd = new Date(new Date(dayStart).getTime() + 24 * 60 * 60 * 1000).toISOString();

  const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);

  // Paginar para buscar todos os registros sem limite de 500
  const allData: any[] = [];
  let page = 0;
  while (true) {
    let query = supabase
      .from("whatsapp_messages")
      .select("sent_at, from_me, sender_name, sender_phone, connected_phone, chat_name, message_text, message_type, is_group, phone, audio_url, media_url, media_caption")
      .gte("sent_at", dayStart)
      .lt("sent_at", dayEnd)
      .order("sent_at", { ascending: true })
      .range(page * PAGE_SIZE, (page + 1) * PAGE_SIZE - 1);

    if (sender_name) query = query.ilike("sender_name", `%${sender_name}%`);
    if (connected_phone) query = query.eq("connected_phone", connected_phone);

    const { data, error } = await query;
    if (error) return json({ error: error.message }, 500);
    if (!data || data.length === 0) break;

    allData.push(...data);
    if (data.length < PAGE_SIZE) break;
    page++;
  }

  // Agrupa por chat_name
  if (!sender_name) {
    const grouped: Record<string, any[]> = {};
    for (const msg of allData) {
      if (msg.is_group) continue;
      const key = msg.chat_name || msg.phone || "desconhecido";
      if (!grouped[key]) grouped[key] = [];
      grouped[key].push(formatMsg(msg));
    }

    const summary = Object.entries(grouped)
      .sort((a, b) => b[1].length - a[1].length)
      .map(([name, msgs]) => ({
        contato: name,
        total_msgs: msgs.length,
        is_group: false,
        mensagens: msgs,
      }));

    return json({
      date: targetDate,
      total_contatos: summary.length,
      total_msgs: allData.length,
      contatos: summary,
    });
  }

  const msgs = allData.map(formatMsg);
  return json({ date: targetDate, sender_name, total_msgs: msgs.length, mensagens: msgs });
});

function formatMsg(msg: any) {
  const hora = new Date(msg.sent_at)
    .toLocaleTimeString("pt-BR", { timeZone: "America/Sao_Paulo", hour: "2-digit", minute: "2-digit" });
  return {
    hora,
    de: msg.from_me ? "EU" : (msg.sender_name || msg.phone),
    chat: msg.chat_name || msg.phone,
    tipo: msg.message_type,
    texto: msg.message_text,
    audio_url: msg.audio_url ?? null,
    media_url: msg.media_url ?? null,
    media_caption: msg.media_caption ?? null,
    grupo: msg.is_group,
  };
}

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body, null, 2), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
}
