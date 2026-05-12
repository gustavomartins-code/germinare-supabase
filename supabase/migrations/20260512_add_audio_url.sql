-- Adiciona coluna audio_url para armazenar URL do áudio da Z-API
-- Permite transcrição posterior no pipeline SalesCoach
ALTER TABLE whatsapp_messages
ADD COLUMN IF NOT EXISTS audio_url TEXT DEFAULT NULL;
