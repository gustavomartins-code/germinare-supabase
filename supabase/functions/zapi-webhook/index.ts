import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const ZAPI_CLIENT_TOKEN = Deno.env.get("ZAPI_CLIENT_TOKEN") ?? "";
const SUPABASE_URL = Deno.env.get("SUPABASE_URL") ?? "";
const SUPABASE_SERVICE_ROLE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";

serve(async (req: Request) => {
  // Validação do Client-Token da Z-API
  if (ZAPI_CLIENT_TOKEN) {
    const clientToken = req.headers.get("Client-Token");
    if (clientToken !== ZAPI_CLIENT_TOKEN) {
      return new Response("Unauthorized", { status: 401 });
    }
  }

  if (req.method !== "POST") {
    return new Response("Method Not Allowed", { status: 405 });
  }

  let body: Record<string, unknown>;
  try {
    body = await req.json();
  } catch {
    return new Response("Invalid JSON", { status: 400 });
  }

  // Ignora eventos sem messageId (ex: notificações de status, conexão)
  if (!body.messageId) {
    return new Response("OK", { status: 200 });
  }

  // Extrai texto de qualquer tipo de mensagem
  const messageText =
    (body.text as any)?.message ??
    (body.image as any)?.caption ??
    (body.video as any)?.caption ??
    (body.document as any)?.fileName ??
    (body.audio ? "[áudio]" : null) ??
    (body.sticker ? "[sticker]" : null) ??
    (body.location ? "[localização]" : null) ??
    null;

  // Salva a URL do áudio para transcrição posterior no pipeline
  const audioUrl = (body.audio as any)?.audioUrl ?? null;

  // Determina o tipo da mensagem
  const messageType = body.text
    ? "text"
    : body.image
    ? "image"
    : body.audio
    ? "audio"
    : body.video
    ? "video"
    : body.document
    ? "document"
    : body.sticker
    ? "sticker"
    : body.location
    ? "location"
    : "unknown";

  // Em grupos, o remetente está em participantPhone; em chats privados, em phone
  const senderPhone =
    (body.participantPhone as string) ?? (body.phone as string);

  const record = {
    message_id: body.messageId as string,
    instance_id: body.instanceId as string,
    connected_phone: (body.connectedPhone as string) ?? "",
    phone: body.phone as string,
    chat_name: (body.chatName as string) ?? null,
    sender_name: (body.senderName as string) ?? null,
    sender_phone: senderPhone,
    from_me: (body.fromMe as boolean) ?? false,
    message_text: messageText,
    message_type: messageType,
    status: (body.status as string) ?? null,
    is_group: (body.isGroup as boolean) ?? false,
    forwarded: (body.forwarded as boolean) ?? false,
    is_edit: (body.isEdit as boolean) ?? false,
    audio_url: audioUrl,
    // momment é o campo correto da Z-API (typo histórico deles)
    sent_at: new Date(body.momment as number).toISOString(),
  };

  const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);

  const { error } = await supabase
    .from("whatsapp_messages")
    .insert(record);

  if (error) {
    console.error("Supabase insert error:", JSON.stringify(error));
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }

  return new Response("OK", { status: 200 });
});
