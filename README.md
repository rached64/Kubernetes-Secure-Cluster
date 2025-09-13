# 🛡️ Kubernetes Secure Cluster

This project demonstrates how to build a **secure, observable, and resilient Kubernetes architecture** using open-source DevSecOps tools.  
It combines monitoring, logging, threat detection, policy enforcement, and chaos engineering into one ecosystem.

---

## 🚀 Architecture Overview

- **Cluster Setup**:  
  - 6 VMs → 3 Masters, 2 Workers, 1 HA Load Balancer  
  - Automated provisioning with **Ansible**  

- **Tools Integrated**:
  - 🔍 **Trivy** → Container image vulnerability scanning  
  - 🔐 **Kyverno** → Policy enforcement (Admission Controller)  
  - 🛡 **Falco** → Real-time runtime security detection  
  - 🤖 **Robusta** → Automated incident response & notifications  
  - 📊 **Prometheus + Grafana + Alertmanager** → Monitoring, dashboards & alerting  
  - 📂 **Loki + OpenObserve** → Centralized logging & search  
  - 🌀 **Chaos Mesh** → Chaos engineering & resilience testing  

---

## 🔄 Communication Between Tools

- **Ansible** → configures the cluster  
- **Trivy & Kyverno** → Prevent vulnerabilities & enforce security before deployment  
- **Falco + FalcoSidekick** → Detect anomalies & forward alerts  
- **Prometheus & Grafana** → Collect & visualize metrics  
- **Loki & OpenObserve** → Aggregate and analyze logs  
- **Robusta** → Automated playbooks for response  
- **Chaos Mesh** → Injects failures to validate resilience  
- **Slack** → Central place for team alerts  
