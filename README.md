<div align="center">

# 🇵🇰 Pakistan Job Market Analyzer & Salary Predictor

### An automated end-to-end Data Science & ML system for Pakistan's job market

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql&logoColor=white)](https://mysql.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge)](https://sqlalchemy.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.0-green?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium.dev)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-blue?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-red?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Latest-blue?style=for-the-badge)](https://xgboost.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge)]()

</div>

---

## 📌 Problem Statement

Pakistan produces **300,000+ CS graduates annually** — yet no centralized, data-driven tool exists to answer the most critical career questions:

- 📊 Which skills do Pakistani employers **actually** demand in 2026?
- 💰 What salary should I **realistically** expect in Lahore vs Karachi?
- 🏙️ Which city and industry has the **most active hiring**?

This project solves that gap with a fully automated data science pipeline.

---

## 🏗️ System Architecture

```
Indeed Pakistan
      │
      ▼
┌─────────────────┐
│ Selenium Scraper│  ← Bypasses bot detection, handles JS rendering
│ + BeautifulSoup │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   MySQL Database│  ← Normalized schema, SQLAlchemy ORM
│  (jobs + skills)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Pandas Pipeline│  ← Cleaning, EDA, Feature Engineering
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ML Classifier  │  ← Logistic Regression, 89.52% accuracy
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│Streamlit Dashboard← Interactive 4-tab web application
└─────────────────┘
```

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Scraping | Selenium + undetected-chromedriver | Bot detection bypass |
| Parsing | BeautifulSoup4 | HTML extraction |
| Database | MySQL + SQLAlchemy ORM | Structured storage |
| Processing | Pandas + NumPy | Cleaning & transformation |
| NLP | TF-IDF Vectorizer | Job title feature extraction |
| Visualization | Matplotlib + Seaborn | EDA plots |
| ML | Scikit-learn + XGBoost | Job category classification |
| Deployment | Streamlit | Interactive dashboard |
| Automation | schedule library | Weekly auto-scraping |

---

## ✅ Project Progress

| Phase | Description | Status |
|---|---|---|
| 1 | Project Setup & MySQL Schema | ✅ Complete |
| 2 | Web Scraping — Indeed Pakistan | ✅ Complete |
| 3 | Database Storage with SQLAlchemy | ✅ Complete |
| 4 | Data Cleaning & EDA | ✅ Complete |
| 5 | Feature Engineering | ✅ Complete |
| 6 | ML Modeling — Job Category Classifier | ✅ Complete |
| 7 | Streamlit Interactive Dashboard | ⏳ In Progress |
| 8 | Deployment & Portfolio Polish | ⏳ Upcoming |

---

## 📊 Phase 2 — Web Scraping

- ✅ Selenium + undetected-chromedriver bypasses bot detection
- ✅ Pagination — 10 pages per search query
- ✅ **1,566 raw listings** scraped across 5 categories × 3 cities
- ✅ Weekly scheduler configured

**Categories:** Software Engineer, Data Analyst, Mechanical Engineer, Accountant, Electrical Engineer
**Cities:** Lahore, Karachi, Islamabad

---

## 🗄️ Phase 3 — Database Storage

- ✅ SQLAlchemy ORM models for normalized MySQL schema
- ✅ Credentials secured via `.env`
- ✅ Duplicate detection on every insert
- ✅ **620 unique jobs in MySQL**

---

## 🔍 Phase 4 — Data Cleaning & EDA

- ✅ 24 city variations → 5 clean categories
- ✅ Rule-based category extraction — 98.5% accuracy
- ✅ 5 professional visualizations

### Key EDA Findings

| # | Finding | Insight |
|---|---|---|
| 1 | Software Engineering = 61% of jobs | Pakistan's market is tech-dominated |
| 2 | Karachi (236) ≈ Lahore (231) | Both equally strong — 75% of all listings |
| 3 | 100% salary hidden | Our predictor fills this gap |
| 4 | Contour Software — 24 listings | Most active employer |
| 5 | SQA Engineer = 3rd most common title | QA is highly demanded |

---

## ⚙️ Phase 5 — Feature Engineering

- ✅ Seniority extracted from titles (0=Junior, 1=Mid, 2=Senior, 3=Lead)
- ✅ Label encoded city and category
- ✅ TF-IDF vectorizer on job titles (50 features)
- ✅ Final feature matrix: 620 × 52
- ✅ Encoders saved — `le_city.pkl`, `le_category.pkl`

---

## 🤖 Phase 6 — ML Modeling

### Model Comparison

| Model | Accuracy |
|---|---|
| **Logistic Regression** | **89.52%** ← Winner |
| Random Forest | 87.10% |
| XGBoost | 87.10% |
| Baseline (majority class) | 61.29% |

### Key Results
- ✅ All 3 models significantly outperform 61.29% baseline
- ✅ Logistic Regression wins — TF-IDF creates linearly separable features
- ✅ Data Science & AI — 100% F1 score
- ✅ Software Engineering — 99% recall
- ✅ Finance & Accounting — 93% F1 score
- ✅ Models saved — `category_model.pkl`, `tfidf_vectorizer.pkl`

### Saved Model Artifacts
```
models/
├── category_model.pkl      # Logistic Regression classifier
├── tfidf_vectorizer.pkl    # TF-IDF vectorizer (50 features)
├── le_city.pkl             # City label encoder
└── le_category.pkl         # Category label encoder
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE jobs (
    job_id           INT AUTO_INCREMENT PRIMARY KEY,
    title            VARCHAR(255) NOT NULL,
    company          VARCHAR(255) NOT NULL,
    city             VARCHAR(100),
    salary           VARCHAR(255) DEFAULT NULL,
    experience_years FLOAT DEFAULT NULL,
    education        VARCHAR(100),
    category         VARCHAR(100),
    date_posted      DATE,
    date_scraped     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE skills (
    skill_id   INT AUTO_INCREMENT PRIMARY KEY,
    job_id     INT NOT NULL,
    skill_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE
);
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- MySQL 8.0+
- Google Chrome

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/husnainalix77/pakistan-job-market-analyzer.git
cd pakistan-job-market-analyzer

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo DB_PASSWORD=your_mysql_password > .env

# 5. Setup MySQL database
python database/models.py

# 6. Run the scraper
python scraper/indeed_scraper.py

# 7. Insert data into MySQL
python -m database.db_manager

# 8. Run notebooks
jupyter notebook notebooks/

# 9. Launch dashboard
streamlit run app/app.py
```

---

## 📁 Repository Structure

```
pakistan-job-market-analyzer/
│
├── scraper/
│   ├── indeed_scraper.py    # Selenium + BS4 scraping logic
│   ├── scheduler.py         # Automated weekly scraping
│   └── utils.py             # Shared utility functions
│
├── database/
│   ├── models.py            # SQLAlchemy ORM table definitions
│   ├── db_manager.py        # Insert, query, duplicate detection
│   └── schema.sql           # Raw SQL schema reference
│
├── notebooks/
│   ├── 01_EDA_and_feature_engineering.ipynb
│   └── 02_modeling.ipynb
│
├── models/
│   ├── category_model.pkl   # Trained Logistic Regression
│   ├── tfidf_vectorizer.pkl # TF-IDF vectorizer
│   ├── le_city.pkl          # City label encoder
│   └── le_category.pkl      # Category label encoder
│
├── app/
│   └── app.py               # Streamlit dashboard
│
├── .env                     # MySQL credentials (not in repo)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Key Engineering Decisions

**Why TF-IDF over raw features?**
City + seniority alone gave 61% accuracy (same as baseline).
Adding TF-IDF on job titles jumped to 89.52% — title keywords
are the strongest predictor of job category.

**Why Logistic Regression over XGBoost?**
TF-IDF creates sparse, high-dimensional, linearly separable features.
Linear models like Logistic Regression handle this better than
tree-based models. XGBoost and Random Forest both scored 87.10%.

**Why save 4 separate artifacts?**
Dashboard needs all 4 to function — model predicts, TF-IDF transforms
title input, le_city encodes city, le_category decodes prediction back
to readable category name.

---

## 👨‍💻 About the Author

<div align="center">

**Husnain Maroof**

3rd Year Mechatronics & Control Engineering
University of Engineering & Technology (UET), Lahore

*Open to remote opportunities in Data Science & ML Engineering*

[![GitHub](https://img.shields.io/badge/GitHub-husnainalix77-black?style=for-the-badge&logo=github)](https://github.com/husnainalix77)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Husnain%20Maroof-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/husnainalix77)

</div>

---

<div align="center">

⭐ **Star this repo to follow the build progress** ⭐

*Actively committing — check the commit history*

</div>
