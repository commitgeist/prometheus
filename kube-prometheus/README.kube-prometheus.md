# kube-prometheus: Stack de Monitoramento para Kubernetes

## O que é kube-prometheus?

**kube-prometheus** é um projeto que fornece uma stack completa de monitoramento para ambientes Kubernetes. Inclui:

- **Prometheus Operator**
- **Prometheus** pré-configurado para Kubernetes
- **Grafana** com dashboards prontos
- **AlertManager** com regras de alerta
- **Node Exporter**
- **kube-state-metrics**
- Diversos **ServiceMonitors** prontos para uso

---

## Comparativo entre Abordagens

| Característica              | kube-prometheus                       | Manifests Vanilla                    |
|----------------------------|----------------------------------------|--------------------------------------|
| Instalação                 | Rápida, via repositório oficial       | Manual, passo a passo                |
| Flexibilidade              | Baixa                                 | Alta                                 |
| Curva de aprendizado       | Mais rasa                             | Mais profunda                        |
| Personalização             | Limitada                              | Total                                |
| Ideal para...              | Produção rápida, padrão comunitário   | Aprendizado, ambientes customizados  |

---

## Arquitetura kube-prometheus

```
┌─────────────────────────────────────────────────────────┐
│                 kube-prometheus                         │
│                                                         │
│  ┌─────────────────┐    ┌─────────────────┐            │
│  │ PROMETHEUS      │    │ PROMETHEUS      │            │
│  │ OPERATOR        │ -> │ INSTANCE        │            │
│  └─────────────────┘    └─────────────────┘            │
│                                                         │
│  ┌─────────────────┐    ┌─────────────────┐            │
│  │ GRAFANA         │    │ ALERTMANAGER    │            │
│  └─────────────────┘    └─────────────────┘            │
│                                                         │
│  ┌─────────────────┐    ┌─────────────────┐            │
│  │ NODE EXPORTER   │    │ KUBE-STATE      │            │
│  └─────────────────┘    │ METRICS         │            │
│                         └─────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

---

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/prometheus-operator/kube-prometheus.git
cd kube-prometheus

# 2. Instale os CRDs
kubectl apply --server-side -f manifests/setup

# 3. Aguarde os CRDs
kubectl wait --for condition=Established --all CustomResourceDefinition --namespace=monitoring

# 4. Instale o stack completo
kubectl apply -f manifests/
```

---

## Componentes principais

### 1. Prometheus Operator

```yaml
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: kube-prometheus
spec:
  serviceAccountName: prometheus-kube-prometheus
  serviceMonitorSelector:
    matchLabels:
      team: frontend
```

### 2. ServiceMonitor

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: my-app
spec:
  selector:
    matchLabels:
      app: my-app
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
```

### 3. PrometheusRule

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: my-rules
spec:
  groups:
  - name: my-app-rules
    rules:
    - alert: HighErrorRate
      expr: rate(http_errors_total[5m]) > 0.1
```

---

## Quando Usar Cada Abordagem?

### Manifests Vanilla:
- Aprendizado
- Controle completo
- Integrações customizadas

### kube-prometheus:
- Produção rápida
- Dashboards prontos
- Equipe pequena
- Manutenção simples

---

## Exemplo Prático: Comparação

### Vanilla:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
data:
  prometheus.yml: |
    scrape_configs:
    - job_name: 'my-app'
      static_configs:
      - targets: ['my-app:8080']
```

### kube-prometheus:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: my-app
spec:
  selector:
    matchLabels:
      app: my-app
  endpoints:
  - port: metrics
```