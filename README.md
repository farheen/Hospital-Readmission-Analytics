# 🏥 Hospital Readmission Analytics

## 📝 One-Liner
Analyzing hospital patient readmissions with Python and Power BI to identify high-risk groups and reduce readmission rates.

---

## 📖 Overview
This project uses the **UCI Diabetes 130-US Hospitals dataset** to study patient admissions and readmissions.  
The goal is to preprocess the raw data with Python, engineer a readmission flag, and prepare a dataset for visualization in Power BI.

---

## 🛠️ Tech Stack
- **Python (Pandas)** → ETL & preprocessing  
- **Power BI** → Dashboard (to be built later)  
- **Dataset** → [UCI Diabetes 130 Hospitals](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008)  

---

## 🚀 How to Run
1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt

## 🏗️ Architecture

```mermaid
flowchart LR
    A[Raw Dataset CSV] --> B[Python Preprocessing ETL]
    B --> C[Processed Data CSV]
    C --> D[Power BI Dashboard]

