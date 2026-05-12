#!/bin/bash
# Deploy da Edge Function avaliar-conversa
# Requer: SUPABASE_PROJECT_REF e GEMINI_API_KEY definidos

set -e

SUPABASE_PROJECT_REF="${SUPABASE_PROJECT_REF:-pgmtlxgihzongbuncnpm}"

echo "=== Deploy: avaliar-conversa ==="

if [ -z "$GEMINI_API_KEY" ]; then
  echo "ERRO: defina GEMINI_API_KEY antes de rodar."
  echo "Exemplo: export GEMINI_API_KEY=AIza..."
  exit 1
fi

echo "Linkando ao projeto $SUPABASE_PROJECT_REF..."
npx supabase link --project-ref "$SUPABASE_PROJECT_REF"

echo "Configurando GEMINI_API_KEY..."
npx supabase secrets set GEMINI_API_KEY="$GEMINI_API_KEY"

echo "Fazendo deploy..."
npx supabase functions deploy avaliar-conversa --no-verify-jwt

echo ""
echo "=== Deploy concluído! ==="
echo "URL: https://$SUPABASE_PROJECT_REF.supabase.co/functions/v1/avaliar-conversa"
