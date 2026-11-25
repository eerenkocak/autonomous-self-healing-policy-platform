# Autonomous SRE Self-Healing, Chaos Engineering & OPA Policy-as-Code Platform

[English Documentation](#english-version) | [Turkce Dokumantasyon](#turkce-versiyon)

---

## <a name="english-version"></a>English Version

This repository demonstrates an enterprise **Platform Engineering & Site Reliability Engineering (SRE)** architecture combining **Policy-as-Code Governance (Open Policy Agent - Rego v1)**, **Chaos Engineering fault injection**, and an event-driven **Autonomous Self-Healing Engine** that automatically recovers degraded services and generates **SRE Incident Post-Mortem** reports with zero human intervention.

### Key Platform Engineering & SRE Capabilities

* **Policy-as-Code Security & FinOps Guardrails (`policies/k8s_guardrails.rego`):** Uses Open Policy Agent (OPA Rego v1) to audit Kubernetes manifests pre-deployment, blocking containers that lack `runAsNonRoot: true` (Security) or `resources.limits.memory` (FinOps).
* **Chaos Engineering Fault Injection (`chaos/chaos_monkey.sh`):** Simulates unexpected production outages by terminating critical runtime services to validate platform resilience.
* **Autonomous Self-Healing Engine (`remediator/engine.py`):** Continuously monitors target service health endpoints, detects failures within seconds, executes automated container recovery via Docker Engine API, and calculates **MTTR (Mean Time To Recovery)**.
* **Automated Incident Post-Mortem Generation (`incidents/`):** Produces structured Markdown SRE post-mortem reports capturing detection timestamps, recovery timestamps, root cause, and MTTR metrics after every self-healing event.

### Project Structure

```text
autonomous-self-healing-policy-platform/
|-- policies/
|   `-- k8s_guardrails.rego      # OPA Rego v1 Security & FinOps admission policies
|-- samples/

|   |-- bad-deployment.yaml      # Non-compliant manifest (blocked by OPA)
|   `-- good-deployment.yaml     # Hardened & bounded manifest (approved by OPA)
|-- remediator/

|   |-- engine.py                # Event-driven self-healing & MTTR post-mortem engine
|   `-- Dockerfile               # Alpine Python runtime with Docker CLI integration
|-- chaos/
|   `-- chaos_monkey.sh          # Controlled fault injection script
|-- incidents/
|   `-- POSTMORTEM_INC-*.md      # Auto-generated SRE incident post-mortem reports
|-- docker-compose.yml           # Target microservice & autonomous remediator stack
|-- .gitignore
`-- README.md
```

---

## <a name="turkce-versiyon"></a>Turkce Versiyon

Bu depo; **Policy-as-Code Yonetisimi (Open Policy Agent - Rego v1)**, **Kaos Muhendisligi (Chaos Engineering)** ve insan mudahalesine gerek kalmadan bozulan servisleri kurtarip otomatik **SRE Post-Mortem** raporu ureten **Otonom Self-Healing Motorunu** bir araya getiren kurumsal bir **Platform Engineering & SRE** mimarisidir.

### One Cikan Platform Engineering ve SRE Yetenekleri

* **Policy-as-Code Guvenlik ve FinOps Anayasasi (`policies/k8s_guardrails.rego`):** Open Policy Agent (OPA) kullanarak Kubernetes manifestlerini dagitim oncesi denetler; `runAsNonRoot: true` (Guvenlik) veya `resources.limits.memory` (FinOps) eksik olan konteynerleri reddeder.
* **Kaos Muhendisligi Simülasyonu (`chaos/chaos_monkey.sh`):** Sistem dayanikliligini test etmek icin kritik servisleri beklenmedik sekilde sonlandirarak ariza enjeksiyonu yapar.
* **Otonom Self-Healing Motoru (`remediator/engine.py`):** Hedef servis sagligini surekli izler, kesintiyi saniyeler icinde tespit eder, otomatik kurtarma aksiyonu alir ve **MTTR (Ortalama Kurtarma Suresi)** degerini hesaplar.
* **Otomatik Olay Sonrasi Analiz Raporu (`incidents/`):** Her kurtarma operasyonu sonrasinda tespit zamani, kurtarma suresi ve kok neden analizini iceren kurumsal Markdown Post-Mortem raporu olusturur.
