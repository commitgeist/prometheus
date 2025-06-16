mkdir -p /tmp/test-expired-cert
cd /tmp/test-expired-cert

# Gera chave privada
openssl genrsa -out expired.key 2048

# Gera CSR
openssl req -new -key expired.key -subj "/CN=expired.test.local" -out expired.csr

# Gera certificado expirado (vencido em 2023)
openssl x509 -req \
  -in expired.csr \
  -signkey expired.key \
  -out expired.crt \
  -startdate 20230101000000Z \
  -enddate   20230102000000Z
