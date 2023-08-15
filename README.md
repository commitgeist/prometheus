# prometheus
Instalação do agent -> https://github.com/prometheus/node_exporter/releases

# https://hub.docker.com/r/prom/prometheus


# Comando quebrando linhas
docker run \
    -p 9090:9090 \
    -v  %cd%\prometheus\prometheus.yaml:/etc/prometheus/prometheus.yml \
    prom/prometheus


# Comando em uma única linha
docker run --name prometheus --rm -d -p 9090:9090  -v %cd%\prometheus\prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus