#!/bin/bash
# Deploy da Edge Function zapi-webhook para o Supabase
# Execute este script no terminal dentro da pasta germinare-supabase

set -e

echo "=== Deploy Germinare: zapi-webhook ==="

# 1. Verificar variáveis obrigatórias
if [ -z "$SUPABASE_PROJECT_REF" ]; then
  echo "ERRO: defina SUPABASE_PROJECT_REF antes de rodar."
  echo "Exemplo: export SUPABASE_PROJECT_REF=abcdefghijklmnop"
  exit 1
fi

if [ -z "$ZAPI_CLIENT_TOKEN" ]; then
  echo "AVISO: ZAPI_CLIENT_TOKEN não definido. A function ficará sem autenticação."
fi

if [ -z "$SUPABASE_SERVICE_ROLE_KEY" ]; then
  echo "ERRO: defina SUPABASE_SERVICE_ROLE_KEY antes de rodar."
  exit 1
fi

# 2. Link ao projeto
echo "Linkando ao projeto $SUPABASE_PROJECT_REF..."
npx supabase link --project-ref "$SUPABASE_PROJECT_REF"

# 3. Setar secrets
echo "Configurando secrets..."
npx supabase secrets set ZAPI_CLIENT_TOKEN="$ZAPI_CLIENT_TOKEN"
npx supabase secrets set SUPABASE_SERVICE_ROLE_KEY="$SUPABASE_SERVICE_ROLE_KEY"

# 4. Deploy da function
echo "Fazendo deploy da function..."
npx supabase functions deploy zapi-webhook --no-verify-jwt

echo ""
echo "=== Deploy concluído! ==="
echo "URL da sua Edge Function:"
echo "https://$SUPABASE_PROJECT_REF.supabase.co/functions/v1/zapi-webhook"
echo ""
echo "Cole essa URL nos campos 'On send' e 'On receiving' da Z-API."
