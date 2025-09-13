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

<img width="1780" height="1053" alt="architecture" src="https://github.com/user-attachments/assets/dae1dc3b-ec15-4960-b81b-d164effb34dd" />


Important Note: The playbook installs Kubernetes on Ubuntu 24.04. Before execution:

    Review and modify all inventory variables and file paths for your specific environment

    Validate the playbook in a staging or development environment before applying to production systems
    Usage:
    ansible-playbook -i inventory.ini kubernetes-setup.yml

  
All other configuration files use the .yaml extension and contain configurations for security tools like Falco and other cluster components. 
Additional files may include informational content and supplementary documentation.    


