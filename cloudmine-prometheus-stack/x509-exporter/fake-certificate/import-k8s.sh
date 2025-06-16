kubectl create secret tls expired-cert \
  --cert=expired.crt \
  --key=expired.key \
  --namespace=monitoring
