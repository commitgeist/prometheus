# Prometheus
Instalação do agent -> https://github.com/prometheus/node_exporter/releases


<!-- ## URL DA IMAGEM DO Prometheus -->
Acesse -> https://hub.docker.com/r/prom/prometheus
Download -> https://github.com/prometheus-community/windows_exporter
Instalação no Windows -> msiexec windows_exporter-0.23.1-amd64.msi --collectors.enabled
# Docker 

<!-- Comando quebrando linhas -->
docker run \
    -p 9090:9090 \
    -v  %cd%\prometheus\prometheus.yaml:/etc/prometheus/prometheus.yml \
    prom/prometheus


<!-- Comando em uma única linha -->
docker run --name prometheus --rm -d -p 9090:9090  -v %cd%\prometheus\prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus


# Grafana

Override:
    Tutorial -> https://www.codementor.io/@dhananjaykumar/docker-compose-between-files-and-projects-21aryt2p2l

    Command -> docker compose -f .\docker-compose.yaml -f .\docker-compose.override.yaml up -d

# Docker
    Instalação em container -> https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/