FROM ubuntu:latest

WORKDIR /usr/src/observability

RUN apt-get update -y && apt-get upgrade -y

COPY . /usr/src/observability/


#RUN apt-get install wget -y && wget wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz

RUN tar xvf node_exporter-1.3.1.linux-amd64.tar.gz


RUN cd node_exporter-1.3.1.linux-amd64 \
    cp node_exporter /usr/local/bin \
    cp node_exporter.service /etc/systemd/system \
    cd .. \
    rm -rf ./node_exporter-1.3.1.linux-amd64 \
    useradd --no-create-home --shell /bin/false node_exporter



RUN systemctl daemon-reload \
    systemctl enable node_exporter \
    systemctl start node_exporter \
    ufw allow 9100 \
    iptables -I INPUT -p tcp -m tcp --dport 9100 -j ACCEPT
