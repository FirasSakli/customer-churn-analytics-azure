# 📊 Enterprise Customer Churn Analytics Platform (Microsoft Azure)

## Overview
This project implements an **end-to-end customer churn analytics platform** using the **Microsoft Azure ecosystem**, following enterprise data engineering and analytics best practices.

The goal is to demonstrate how raw customer data can be transformed into **actionable business insights**, including **churn prediction** and **revenue-at-risk analysis**, using a **cost-aware, serverless architecture**.

---

## Business Problem
Customer churn is a critical business problem, especially in subscription-based industries such as telecommunications.

This project answers key business questions:
- Which customer segments are most likely to churn?
- What factors drive churn?
- How much **revenue is at risk** due to churn?
- How can decision-makers monitor churn **in near real time**?

---

## Architecture (High-Level)

```
Raw CSV Data
   ↓
Local Data Cleaning & Validation (Python)
   ↓
Azure Data Lake Storage Gen2 (Bronze / Silver)
   ↓
Azure Synapse Serverless SQL (Analytics Views)
   ↓
Power BI Desktop (DirectQuery)
```

### Key Design Principles
- **Separation of concerns** (bronze / silver / gold concepts)
- **Serverless-first** (no Spark clusters, no dedicated SQL pools)
- **Cost awareness** (pay-per-query analytics)
- **Interpretability over black-box ML**
- **EU data residency** (Germany West Central)

---

## Data Pipeline

### 1. Local Processing
- Raw data ingested and validated locally using Python
- Data cleaned and standardized into a **silver dataset**
- Stored in **Parquet** format for analytics efficiency

### 2. Cloud Storage
- Azure Data Lake Storage Gen2 used as the central data lake
- Folder structure mirrors enterprise lakehouse patterns:
```
datalake/
  bronze/
  silver/
  gold/
```

### 3. Analytics Layer
- Azure Synapse **Serverless SQL** queries Parquet data directly
- SQL views provide a **stable analytics contract**
- No infrastructure provisioning required

---

## Machine Learning
Two churn models were developed and compared:
- **Logistic Regression** (baseline, interpretable)
- **Random Forest** (non-linear, higher performance)

---

## Business Intelligence & KPIs

### Power BI (DirectQuery)
Power BI Desktop connects directly to Azure Synapse using **DirectQuery**, ensuring:
- No data duplication
- Live querying of cloud data
- Enterprise-style BI architecture

### Key KPIs
- **Customer Count**
- **Churn Rate**
- **Revenue at Risk**
- **Churn by Contract Type**
- **Churn by Payment Method**

---

## Technology Stack

### Programming & Data
- Python
- SQL
- Pandas, NumPy, Scikit-learn
- Parquet

### Cloud & Analytics
- Azure Data Lake Storage Gen2
- Azure Synapse Serverless SQL

### BI & Visualization
- Power BI Desktop
- DirectQuery
- DAX

---

## Repository Structure
```
.
├── data/
├── src/
├── notebooks/
├── powerbi/
├── docs/
└── README.md
```

---

## Author
**Firas Sakli**  
M.Sc. Web and Data Science — University of Koblenz  

GitHub: https://github.com/FirasSakli  
LinkedIn: https://www.linkedin.com/in/firas-sakli-872658183/
