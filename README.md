# Azure Retail Pipeline

[![CI/CD](https://github.com/igobymatthew/Azure_Retail_Pipeline/actions/workflows/deploy.yml/badge.svg)](https://github.com/igobymatthew/Azure_Retail_Pipeline/actions)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

> **Status:** In Development  
> A demonstration project for Azure data pipeline skills using ADF, Azure SQL, Databricks, SSIS, and Python.

---

## 📑 Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Future Enhancements](#future-enhancements)

---

## 📌 Overview
This project simulates a retail business scenario by implementing an end-to-end Azure data pipeline using:
- Azure Data Factory (ADF) for orchestration
- Azure SQL Database for centralized storage
- Databricks for transformations
- Python for business logic and anomaly detection
- SSIS for legacy data integration (optional)

---

## 🧱 Architecture
**Data Flow:**

```
CSV / Legacy SQL → ADF / SSIS → Azure SQL DB → Databricks → Azure SQL Reporting → Power BI (optional)
```

---

## 🛠️ Technologies Used
- **Azure Data Factory (ADF)**
- **Azure SQL Database**
- **Azure Databricks (PySpark)**
- **SSIS**
- **Python (pandas)**
- **GitHub Actions (CI/CD)**

---

## 📁 Folder Structure

```text
azure-retail-pipeline/
├── data/         # Sample CSV files
├── notebooks/    # Databricks transformation scripts
├── python/       # ETL and analytics scripts (Python)
├── ssis/         # SSIS package or notes
├── adf/          # ADF pipeline definitions (JSON)
├── sql/          # SQL schema and scripts
├── diagrams/     # Architecture diagrams and flowcharts
└── README.md     # Project documentation
```

---

## 🚀 Setup Instructions

### Prerequisites
- Azure Subscription
- Azure SQL Database + logical server
- Azure Data Factory
- Azure Databricks workspace

### Step-by-Step
1. Deploy the SQL schema using `sql/create_sales_table.sql`
2. Import ADF pipeline JSON via Azure Portal or CLI
3. Upload `notebooks/sales_transform.py` to Databricks
4. Run `python/detect_anomalies.py` locally or via automation

---

## 🔮 Future Enhancements
- Power BI dashboard integration
- Key Vault for secure credentials
- CI/CD pipeline for ADF, SQL, Python, and Databricks
- Terraform/Bicep infrastructure automation

---

## 📄 License
MIT — feel free to fork and adapt.

