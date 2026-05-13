import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const SUPABASE_URL = Deno.env.get("SUPABASE_URL") ?? "";
const SUPABASE_SERVICE_ROLE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";

serve(async (req: Request) => {
  if (req.method !== "POST") {
    return new Response("Method Not Allowed", { status: 405 });
  }

  let payload: any;
  try {
    payload = await req.json();
  } catch {
    return new Response("Invalid JSON", { status: 400 });
  }

  const items: any[] = Array.isArray(payload) ? payload : [payload];
  const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);
  const errors: string[] = [];

  for (const item of items) {
    try {
      // Payload vem como {headers, params, query, body} do n8n/Evolution
      // ou diretamente como {event, data, sender} se enviado direto
      const body = item?.body ?? item;
      const data = body?.data;

      if (!data?.key?.remoteJid) {
        console.log("SKIP: sem data.key.remoteJid", JSON.stringify(body).slice(0, 150));
        continue;
      }

      const remoteJid: string = data.key.remoteJid;
      const fromMe: boolean = data.key.fromMe ?? false;
      const messageId: string = data.key.id ?? `${remoteJid}-${data.messageTimestamp}`;
      const messageType: string = data.messageType ?? "unknown";
      const msg: any = data.message ?? {};
      const phone: string = remoteJid.split("@")[0];
      const isGroup: boolean = remoteJid.endsWith("@g.us");

      // Ignorar mensagens de grupos
      if (isGroup) {
        console.log("SKIP: grupo", remoteJid);
        continue;
      }

      const connectedPhone: string = (body.sender ?? "").split("@")[0];
      const senderName: string | null = fromMe ? null : (data.pushName ?? null);
      const chatName: string = data.groupMetadata?.subject ?? (fromMe ? null : data.pushName) ?? phone;

      let messageText: string | null = null;
      let audioUrl: string | null = null;
      let mediaUrl: string | null = null;
      let mediaCaption: string | null = null;

      if (messageType === "conversation") {
        messageText = msg.conversation ?? null;
      } else if (messageType === "extendedTextMessage") {
        messageText = msg.extendedTextMessage?.text ?? null;
      } else if (messageType === "audioMessage") {
        audioUrl = msg.audioMessage?.url ?? null;
        messageText = "[áudio]";
      } else if (messageType === "imageMessage") {
        mediaUrl = msg.imageMessage?.url ?? null;
        mediaCaption = msg.imageMessage?.caption ?? null;
        messageText = mediaCaption ?? "[imagem]";
      } else if (messageType === "videoMessage") {
        mediaUrl = msg.videoMessage?.url ?? null;
        mediaCaption = msg.videoMessage?.caption ?? null;
        messageText = mediaCaption ?? "[vídeo]";
      } else if (messageType === "documentMessage") {
        mediaUrl = msg.documentMessage?.url ?? null;
        messageText = msg.documentMessage?.fileName ?? "[documento]";
      } else if (messageType === "stickerMessage") {
        mediaUrl = msg.stickerMessage?.url ?? null;
        messageText = "[sticker]";
      } else if (messageType === "locationMessage") {
        messageText = "[localização]";
      } else if (messageType === "contactMessage") {
        messageText = "[contato]";
      } else {
        messageText = `[${messageType}]`;
      }

      const sentAt = data.messageTimestamp
        ? new Date((data.messageTimestamp as number) * 1000).toISOString()
        : new Date().toISOString();

      const record = {
        message_id: messageId,
        instance_id: body.instance ?? null,
        connected_phone: connectedPhone,
        phone,
        chat_name: chatName,
        sender_name: senderName,
        sender_phone: fromMe ? connectedPhone : phone,
        from_me: fromMe,
        message_text: messageText,
        message_type: messageType,
        is_group: isGroup,
        audio_url: audioUrl,
        media_url: mediaUrl,
        media_caption: mediaCaption,
        sent_at: sentAt,
      };

      console.log(`INSERT from_me=${fromMe} type=${messageType} chat=${chatName} text=${(messageText ?? "").slice(0, 40)}`);

      const { error } = await supabase
        .from("whatsapp_messages")
        .upsert(record, { onConflict: "message_id" });

      if (error) {
        console.error("upsert error:", JSON.stringify(error));
        errors.push(error.message);
      }
    } catch (err: any) {
      console.error("item error:", err?.message);
      errors.push(err?.message ?? "unknown error");
    }
  }

  if (errors.length > 0) {
    return new Response(JSON.stringify({ errors }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }

  return new Response("OK", { status: 200 });
});
