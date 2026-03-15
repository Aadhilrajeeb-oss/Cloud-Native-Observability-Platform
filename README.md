# Cloud Native Observability Platform with Secure IAM

A **cloud-native observability and monitoring platform** designed to demonstrate modern **DevOps, microservices, and security practices**.

The system includes:

* Containerized microservices
* Observability stack (Prometheus, Grafana, Loki)
* Role-Based Access Control (IAM)
* JWT authentication
* Audit logging for security events
* Interactive monitoring dashboard

This project simulates how **enterprise DevOps platforms monitor applications and enforce access control**.

---

# Architecture

```
Users
  ↓
Frontend Dashboard (Nginx)
  ↓
Authentication Service (JWT + IAM)
  ↓
Microservices
   ├── User Service
   └── Task Service
  ↓
PostgreSQL Database
  ↓
Observability Stack
   ├── Prometheus (Metrics)
   ├── Grafana (Dashboards)
   ├── Loki (Logs)
   └── Alertmanager (Alerts)
```

---

# Features

## DevOps Infrastructure

* Docker containerized services
* Microservices architecture
* Kubernetes deployment support
* CI/CD ready

## Observability

* Prometheus metrics monitoring
* Grafana dashboards
* Loki centralized logging
* Real-time metrics visualization

## Security

* JWT authentication
* Role-based access control (RBAC)
* IAM user management panel
* Audit logging for user activity

## Dashboard

* Live metrics charts
* Task management demo application
* IAM management console
* Monitoring tool integrations

---

# Tech Stack

| Layer            | Technology                    |
| ---------------- | ----------------------------- |
| Frontend         | HTML, JavaScript, TailwindCSS |
| Backend          | FastAPI                       |
| Authentication   | JWT (python-jose)             |
| Database         | PostgreSQL                    |
| Containerization | Docker                        |
| Orchestration    | Kubernetes                    |
| Monitoring       | Prometheus                    |
| Visualization    | Grafana                       |
| Logging          | Loki                          |
| DevOps           | Docker Compose                |

---

# Project Structure

```
cloud-observability-platform
│
├── frontend
│   ├── index.html
│   ├── login.html
│   ├── app.js
│   └── Dockerfile
│
├── services
│   ├── auth-service
│   ├── user-service
│   └── task-service
│
├── prometheus
│   └── prometheus.yml
│
├── loki
│   └── loki-config.yml
│
├── promtail
│   └── promtail-config.yml
│
├── alertmanager
│
├── docker-compose.yml
└── README.md
```

---

# Running the Platform

Clone the repository

```
git clone https://github.com/Aadhilrajeeb-oss/Cloud-Native-Observability-Platform.git
```

Navigate into the project

```
cd cloud-observability-platform
```

Start the platform

```
docker compose up -d --build
```

---

# Access the Platform

| Service    | URL                   |
| ---------- | --------------------- |
| Dashboard  | http://localhost:8080 |
| Prometheus | http://localhost:9090 |
| Grafana    | http://localhost:3000 |
| Task API   | http://localhost:6060 |
| User API   | http://localhost:5000 |

---

# IAM Roles

| Role      | Permissions    |
| --------- | -------------- |
| Admin     | Full access    |
| Developer | Read access    |
| Viewer    | Dashboard only |

Example credentials:

```
admin / admin123
dev / dev123
viewer / view123
```

---

# Audit Logging

Security events are recorded including:

* login attempts
* user creation
* role changes
* unauthorized API requests

Example audit log:

```
2026-03-15 - admin logged in successfully
2026-03-15 - User analyst created with role viewer
2026-03-15 - Unauthorized task creation attempt by viewer
```

---

# Future Improvements

* Kubernetes Helm deployment
* GitHub Actions CI/CD pipeline
* Prometheus alert rules
* Distributed tracing with OpenTelemetry
* Cloud deployment (AWS/GCP)

---

# Author

DevOps / Cloud Engineering Portfolio Project

Created to demonstrate:

* DevOps architecture
* Observability engineering
* Secure IAM access control
* Cloud-native application monitoring
