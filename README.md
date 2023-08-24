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



# Métricas

1. **Sum (Soma):**
   Imagine que você tem várias coisas pequenas e quer saber quanto todas elas somadas pesam. A soma é basicamente isso. No contexto de métricas, como as que você vê em um sistema de monitoramento, o "sum" nos diz a quantidade total de alguma coisa. Por exemplo, a soma do espaço livre em todos os discos.

2. **Rate (Taxa):**
   O "rate" é como dizer "quanto isso está mudando por unidade de tempo". Vamos comparar isso a medir o quão rápido você está andando ou correndo. Se você caminhar 100 metros em 1 minuto, você está se movendo a uma taxa de 100 metros por minuto. No contexto das métricas, o "rate" nos mostra quanto uma métrica está mudando ao longo do tempo. Por exemplo, o quanto o espaço livre em disco está diminuindo a cada segundo.

3. **Irate (Taxa Instantânea):**
   O "irate" é como uma versão rápida do "rate". Imagina que você olha para o velocímetro do carro e vê a velocidade instantânea naquele exato momento. O "irate" é semelhante. Ele nos mostra a taxa instantânea de mudança de uma métrica naquele momento específico.

4. **Increase (Aumento):**
    O "increase" é como o "rate", mas em vez de mostrar a taxa de mudança, ele nos mostra o quanto uma métrica aumentou em um período específico. É como ver quanto dinheiro você ganhou em um mês em comparação com o mês anterior.

    Agora, você pode combinar esses conceitos para entender melhor o que a consulta `sum(rate(windows_logical_disk_free_bytes[30s]))` está fazendo. Essa consulta está calculando a taxa de mudança do espaço livre em disco (quanto espaço livre está diminuindo) nos últimos 30 segundos e, em seguida, somando todas essas mudanças. Em outras palavras, ela está te dando uma ideia de quanto espaço livre foi consumido nos últimos 30 segundos em todos os discos e juntando essas mudanças para ter um número total.

    Lembre-se de que essas métricas são usadas para monitorar o desempenho do seu sistema e entender como os recursos estão sendo usados. É como se fosse um termômetro para o seu computador, permitindo que você saiba quando alguma coisa está mudando mais rápido do que o normal ou quando algo precisa ser ajustado.


    # Query's
    sum(rate(windows_cpu_cstate_seconds_total{state="c1"}[5m])) / sum(rate(windows_cpu_cstate_seconds_total{}[5m])) * 100
