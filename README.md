# Cloud Native Observability Platform with Secure IAM

A **cloud-native observability platform** built using the **Prometheus ecosystem** for monitoring, logging, visualization, and alerting of containerized applications.

This platform demonstrates how modern DevOps teams implement **production-grade monitoring stacks** for microservices environments.

---

# Architecture

The platform consists of the following components:

* **Prometheus** → Metrics collection
* **Grafana** → Visualization dashboards
* **Loki** → Centralized logging
* **Promtail** → Log collection agent
* **Alertmanager** → Alert routing
* **Node Exporter** → System metrics
* **Demo Microservice (FastAPI)** → Sample monitored application
* **Docker** → Containerized deployment

Architecture Flow:

```
                   Grafana
               /      |      \
              /       |       \
       Prometheus    Loki    Alertmanager
            |          |
       Node Exporter  Promtail
            |          |
        Demo App (FastAPI)
```

---

# Features

* Real-time infrastructure monitoring
* Centralized log aggregation
* Containerized observability stack
* Custom Grafana dashboards
* Alerting using Alertmanager
* Role-based access control
* Microservice metrics monitoring

---

# Tech Stack

| Component        | Technology        |
| ---------------- | ----------------- |
| Containerization | Docker            |
| Monitoring       | Prometheus        |
| Visualization    | Grafana           |
| Logging          | Loki              |
| Log Collection   | Promtail          |
| Alerting         | Alertmanager      |
| Backend Service  | FastAPI           |
| Metrics Exporter | Prometheus Client |

---

# Project Structure

```
cloud-native-observability-platform
│
├── app
├── prometheus
├── loki
├── promtail
├── alertmanager
├── grafana
├── docker-compose.yml
└── README.md
```

---

# Deployment

Clone repository

```
git clone https://github.com/YOUR_USERNAME/cloud-native-observability-platform.git
```

Enter project

```
cd cloud-native-observability-platform
```

Start the observability stack

```
docker compose up -d --build
```

---

# Access Services

Grafana

```
http://localhost:3000
```

Prometheus

```
http://localhost:9090
```

Demo Application

```
http://localhost:8000
```

Alertmanager

```
http://localhost:9093
```

---

# Example Metrics

Prometheus collects metrics such as:

* CPU usage
* Memory usage
* Network traffic
* Request rate
* Container health

Example metric:

```
app_requests_total
```

---

# Observability Capabilities

| Capability              | Tool          |
| ----------------------- | ------------- |
| Metrics Monitoring      | Prometheus    |
| Log Aggregation         | Loki          |
| Dashboard Visualization | Grafana       |
| Alerting                | Alertmanager  |
| Container Monitoring    | Node Exporter |

---

# Screenshots

Add screenshots here after deployment:

* Grafana dashboards
* Prometheus metrics queries
* Loki log explorer

---

# Future Improvements

* Kubernetes deployment using Helm
* OpenTelemetry distributed tracing
* Multi-cluster monitoring
* OAuth authentication
* CI/CD integration

---

# Author

DevOps / Cloud Engineering Portfolio Project
