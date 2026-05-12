import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const SUPABASE_URL = Deno.env.get("SUPABASE_URL") ?? "";
const SUPABASE_SERVICE_ROLE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";

serve(async (req: Request) => {
  if (req.method !== "GET") {
    return json({ error: "Method Not Allowed" }, 405);
  }

  const url = new URL(req.url);
  const sender_name = url.searchParams.get("sender_name");
  const date = url.searchParams.get("date"); // YYYY-MM-DD, default = hoje (UTC-3)
  const connected_phone = url.searchParams.get("connected_phone");

  // Data no fuso Brasil (UTC-3)
  const targetDate = date ?? new Date(Date.now() - 3 * 60 * 60 * 1000)
    .toISOString()
    .slice(0, 10);

  const dayStart = `${targetDate}T03:00:00.000Z`; // 00:00 BRT = 03:00 UTC
  const dayEnd   = `${targetDate}T26:59:59.999Z`; // 23:59 BRT = 02:59 UTC +1 dia

  const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);

  let query = supabase
    .from("whatsapp_messages")
    .select("sent_at, from_me, sender_name, sender_phone, connected_phone, chat_name, message_text, message_type, is_group, phone")
    .gte("sent_at", dayStart)
    .lt("sent_at", new Date(new Date(dayStart).getTime() + 24 * 60 * 60 * 1000).toISOString())
    .order("sent_at", { ascending: true });

  if (sender_name) {
    query = query.ilike("sender_name", `%${sender_name}%`);
  }
  if (connected_phone) {
    query = query.eq("connected_phone", connected_phone);
  }

  const { data, error } = await query.limit(500);

  if (error) {
    return json({ error: error.message }, 500);
  }

  // Agrupa por contato (sender_name) se não foi filtrado por um contato específico
  if (!sender_name) {
    const grouped: Record<string, any[]> = {};
    for (const msg of data ?? []) {
      const key = msg.sender_name || msg.phone || "desconhecido";
      if (!grouped[key]) grouped[key] = [];
      grouped[key].push(formatMsg(msg));
    }

    const summary = Object.entries(grouped)
      .sort((a, b) => b[1].length - a[1].length)
      .map(([name, msgs]) => ({
        contato: name,
        total_msgs: msgs.length,
        mensagens: msgs,
      }));

    return json({ date: targetDate, total_contatos: summary.length, contatos: summary });
  }

  // Retorna histórico linear de um contato específico
  const msgs = (data ?? []).map(formatMsg);
  return json({
    date: targetDate,
    sender_name,
    total_msgs: msgs.length,
    mensagens: msgs,
  });
});

function formatMsg(msg: any) {
  // Hora em BRT (UTC-3)
  const hora = new Date(new Date(msg.sent_at).getTime() - 0)
    .toLocaleTimeString("pt-BR", { timeZone: "America/Sao_Paulo", hour: "2-digit", minute: "2-digit" });
  return {
    hora,
    de: msg.from_me ? "EU" : (msg.sender_name || msg.phone),
    chat: msg.chat_name || msg.phone,
    tipo: msg.message_type,
    texto: msg.message_text,
    grupo: msg.is_group,
  };
}

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body, null, 2), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
}
