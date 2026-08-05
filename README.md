<div align="center">

# 🛡️ DataSentinel

### Automated Data Quality & Pipeline Monitoring Platform

A professional Python-based Data Quality Validation and Pipeline Monitoring Platform that automatically validates datasets, detects schema drift, identifies anomalies, generates reports, stores validation history, and supports scheduled executions.

Built with ❤️ using Python.

</div>

---

## 📌 Overview

DataSentinel is an enterprise-inspired Data Quality Monitoring Platform designed to automate dataset validation before it enters downstream analytics or machine learning pipelines.

The platform performs rule-based validation, schema comparison, anomaly detection, report generation, validation history management, and scheduled executions through a simple command-line interface.

The project follows a modular architecture, making it easy to extend with additional connectors, validation rules, and reporting formats.

---

# ✨ Features

## 📂 Data Connectors

- CSV Connector
- Excel Connector
- JSON Connector
- Connector Factory Pattern
- Easy to extend with new data sources

---

## ✅ Data Validation

Supports rule-based validation including

- Not Null Validation
- Unique Value Validation
- Range Validation
- Regex Validation
- Custom Rule Support

---

## 📊 Schema Drift Detection

Automatically detects

- Added Columns
- Removed Columns
- Modified Schema

Useful for monitoring production data pipelines.

---

## 📈 Anomaly Detection

Supports statistical anomaly detection using

- IQR Method
- Z-Score Method

Detects unexpected values in numeric columns.

---

## 📄 Report Generation

Automatically generates

- HTML Report
- PDF Report

Includes

- Validation Summary
- Schema Drift
- Anomaly Summary
- Detailed Rule Results

---

## 💾 Database Logging

Stores validation history in SQLite.

Tracks

- Dataset
- Validation Results
- Schema Results
- Anomaly Results
- Generated Reports
- Timestamp

---

## ⏰ Scheduler

Supports automated validation using APScheduler.

Ideal for

- Daily validation
- Hourly monitoring
- Automated data quality checks

---

## 📧 Notification Support

Integrated modules

- Email Notifications
- Slack Notifications

(Currently optional)

---

## 💻 Rich CLI

Professional command-line interface built using

- Typer
- Rich

Provides a clean validation experience.

---

# 🏗️ Project Architecture

```
                +-------------------+
                |      CLI          |
                +---------+---------+
                          |
                          v
                +-------------------+
                | DataSentinelEngine|
                +---------+---------+
                          |
      -----------------------------------------
      |          |           |                |
      v          v           v                v

 Connectors   Rule Engine  Schema Drift  Anomaly Detection

      |          |           |                |
      -----------------------------------------
                          |
                          v

                Report Generation

               HTML Report | PDF Report

                          |
                          v

                  SQLite Database

                          |
                          v

          Email / Slack Notifications
```

---

# 📁 Folder Structure

```
DataSentinel/

├── src/
│   └── datasentinel/
│
│       ├── alerts/
│       ├── anomaly/
│       ├── cli/
│       ├── connectors/
│       ├── database/
│       ├── models/
│       ├── reports/
│       ├── rules/
│       ├── schema/
│       ├── scheduler/
│       ├── utils/
│       └── engine.py
│
├── configs/
│
├── data/
│   └── sample/
│
├── reports/
│
├── tests/
│
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

---

# 🛠️ Tech Stack

### Language

- Python 3

### Libraries

- Pandas
- Jinja2
- SQLAlchemy
- Typer
- Rich
- APScheduler
- PyYAML
- WeasyPrint
- Requests
- python-dotenv
- OpenPyXL
- Pytest

### Database

SQLite

### Reporting

- HTML
- PDF

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/DataSentinel.git

cd DataSentinel
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install the project

```bash
pip install -e .
```

---

# ⚙️ Configuration

Create a `.env` file

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SLACK_WEBHOOK_URL=your_webhook_url
```

---

# ▶️ Usage

Validate CSV

```bash
datasentinel validate csv data/sample/employees.csv configs/rules.yaml
```

Validate Excel

```bash
datasentinel validate excel data/sample/employees.xlsx configs/rules.yaml
```

Validate JSON

```bash
datasentinel validate json data/sample/employees.json configs/rules.yaml
```

Run Scheduler

```bash
datasentinel schedule csv data/sample/employees.csv configs/rules.yaml --interval 60
```

---

# 📊 Generated Reports

After validation

```
reports/

├── html/
│     report.html
│
└── pdf/
      report.pdf
```

The reports include

- Validation Summary
- Rule Results
- Schema Drift
- Anomaly Detection
- Timestamp

---

# 💾 Validation History

Each validation run is stored in SQLite.

Captured information

- Dataset Name
- Validation Results
- Schema Results
- Anomaly Results
- HTML Report Path
- PDF Report Path
- Timestamp

---

# 🧪 Testing

Run all tests

```bash
pytest
```

Generate coverage

```bash
pytest --cov=src
```

---

# 📷 Screenshots

## CLI

> *(Add screenshot here)*

---

## HTML Report

> *(Add screenshot here)*

---

## SQLite Database

> *(Add screenshot here)*

---

# 🔮 Future Improvements

- PostgreSQL Support
- MySQL Connector
- REST API
- Streamlit Dashboard
- Docker Support
- Kubernetes Deployment
- Airflow Integration
- Machine Learning Based Anomaly Detection
- Cloud Storage Connectors
- Power BI Integration

---

# 🎯 Learning Outcomes

This project demonstrates

- Object-Oriented Programming
- Factory Design Pattern
- Modular Architecture
- File Handling
- Database Integration
- Rule Engine Design
- Statistical Data Validation
- CLI Development
- Report Generation
- Scheduler Integration
- Unit Testing
- Python Packaging

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository

Create a feature branch

```bash
git checkout -b feature-name
```

Commit changes

```bash
git commit -m "Add feature"
```

Push

```bash
git push origin feature-name
```

Create a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ashutosh Singh**

B.Tech CSE (Artificial Intelligence)

Python Developer | AI Enthusiast | Full Stack Learner

GitHub:
https://github.com/ashu2506-py

LinkedIn:
https://linkedin.com/in/ashutosh25o6

---

<div align="center">

### ⭐ If you like this project, consider giving it a Star.

**Made with Python ❤️**

</div>