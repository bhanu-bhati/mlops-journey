# Real-Time Machine Learning Inference & Data Telemetry Pipeline

An enterprise-scale MLOps pipeline designed to ingest live global market datasets, host a containerized predictive model microservice, handle high-velocity network traffic, and automatically monitor for statistical data drift.

[Live Financial Stream] ➔ [Scikit-Learn Brain] ➔ [Docker FastAPI Container] ➔ [Evidently Telemetry]
                                                                                      ⬇
                                                                          [GitHub Actions CI Cloud]## 🚀 Core Engineering Architecture

* **Inference Layer:** Built an asynchronous microservice endpoint using **FastAPI** to serve a serialized multi-dimensional predictive matrix (`house_model.pkl`) trained using **Scikit-Learn Linear Regression**.
* **Live Ingestion Pipeline:** Implemented an automated data extraction script using `yfinance` to scrape real-time market trading metrics, clean raw unstructured arrays, and store them into a tracking database.
* **Telemetry & Validation Engine:** Integrated **Evidently AI** to execute automated statistical **Two-Sample Kolmogorov-Smirnov distribution tests**, comparing historical baseline data against incoming market inputs to flag operational Data Drift.
* **Microservices Containerization:** Engineered a standalone, immutable system layout using **Docker** to encapsulate the core application layer, ensuring 100% environment parity across cross-platform instances.
* **Continuous Integration (CI):** Configured a cloud automation workflow via **GitHub Actions** that provisions an isolated remote Linux cluster, forces modern **Node 24** environment mapping, compiles dependencies, and runs testing scripts upon every repository commit.

## 📊 High-Throughput Load Testing Analysis

The containerized API microservice was stress-tested using **Locust** to evaluate performance bounds, identify system saturation points, and measure structural resiliency.

* **Target Load Configuration:** 5,000 Concurrent Simulated Digital Bots
* **Ramp-Up Execution Speed:** 500 Spawned Users / Second
* **Peak Output Throughput:** **1,324 Requests Per Second (RPS)** (~79,440 Requests / Minute)
* **Operational Failure Percentage:** **0.0%**

### Architectural Diagnostics:
During peak swarming execution, hardware processing cores sustained **100% CPU utilization**, triggering standard passive thermal throttling on the host Apple Silicon ARM64 architecture, shifting throughput limits from 1,800 RPS to a stable 1,324 RPS. The asynchronous execution pattern of the FastAPI layer maintained a zero-failure rate, queueing and resolving concurrent network data packages securely without memory degradation.

## 🗂️ Local Workspace Execution Guide

To stand up this development environment natively on an M1 Mac, execute the following command path:

```bash
# 1. Step inside the workspace and activate the sandbox environment
cd mlops_journey
source my_env/bin/activate

# 2. Extract live daily financial data logs
python3 ingest_live_data.py

# 3. Compute statistical distribution checks and view the visual dashboard
python3 monitor_drift.py
open drift_report.html

# 4. Spin up the containerized microservice server
docker build -t my-ml-container .
docker run -p 8080:8080 my-ml-container
```

## 🛠️ Infrastructure Error Resolution Ledger

* **LEDGER-01: Zsh Path Mismatches:** Resolved direct literal runtime typing mistakes by validating exact system path strings (`python3` vs `pyhton3`).
* **LEDGER-02: Security Permissions:** Overrode Mac security layer locks and Apple SDK license boundaries with structural terminal permissions utilizing `sudo xcodebuild -license accept`.
* **LEDGER-03: Regional DNS Mismatches:** Bypassed regional ISP lookup failures fetching remote developer manifests by altering network interface routing properties to point to universal public addresses (`8.8.8.8` / `1.1.1.1`).
* **LEDGER-04: Serialization Dimension Errors:** Rectified unflattened array output crashes (`TypeError`) by explicitly unpacking structural multi-dimensional response metrics before wrapping JSON responses.
* **LEDGER-05: Library Interface Shifts:** Migrated deprecated nested module imports and old serialization tracking functions (`.json()`) to structural dictionary mapping functions (`.as_dict()`) to retain compatibility with Evidently AI v0.7+.

