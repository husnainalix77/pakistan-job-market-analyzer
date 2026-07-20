<div align="center">

# 🇵🇰 Pakistan Job Market Analyzer & Salary Predictor

### An automated end-to-end Data Science & ML system for Pakistan's job market

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql&logoColor=white)](https://mysql.com)
[![Selenium](https://img.shields.io/badge/Selenium-4.0-green?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium.dev)
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
│  XGBoost Model  │  ← Salary Prediction + Job Classification
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
| Database | MySQL + SQLAlchemy | Structured storage |
| Processing | Pandas + NumPy | Cleaning & transformation |
| Visualization | Matplotlib + Seaborn | EDA plots |
| ML | Scikit-learn + XGBoost | Prediction models |
| Deployment | Streamlit | Interactive dashboard |
| Automation | schedule library | Weekly auto-scraping |

---

## ✅ Project Progress

| Phase | Description | Status |
|---|---|---|
| 1 | Project Setup & MySQL Schema | ✅ Complete |
| 2 | Web Scraping — Indeed Pakistan | 🔄 In Progress |
| 3 | Database Storage with SQLAlchemy | ⏳ Upcoming |
| 4 | Data Cleaning & EDA | ⏳ Upcoming |
| 5 | Feature Engineering | ⏳ Upcoming |
| 6 | ML Modeling (Regression + Classification) | ⏳ Upcoming |
| 7 | Streamlit Interactive Dashboard | ⏳ Upcoming |
| 8 | Portfolio Polish & Deployment | ⏳ Upcoming |

---

## 🗄️ Database Schema

```sql
-- Jobs table
CREATE TABLE jobs (
    job_id        INT AUTO_INCREMENT PRIMARY KEY,
    title         VARCHAR(255) NOT NULL,
    company       VARCHAR(255) NOT NULL,
    city          VARCHAR(100),
    salary_min    INT DEFAULT NULL,
    salary_max    INT DEFAULT NULL,
    experience_years FLOAT DEFAULT NULL,
    education     VARCHAR(100),
    category      VARCHAR(100),
    date_posted   DATE,
    date_scraped  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Skills table (normalized — one row per skill per job)
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

# 4. Setup MySQL database
# Open MySQL Workbench → run database/schema.sql

# 5. Run the scraper
python scraper/indeed_scraper.py

# 6. Launch dashboard (Phase 7)
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
│   └── utils.py             # Helper functions
│
├── database/
│   ├── models.py            # SQLAlchemy ORM table definitions
│   ├── db_manager.py        # Insert, query, update operations
│   └── schema.sql           # Raw SQL schema reference
│
├── notebooks/
│   ├── 01_EDA.ipynb         # Exploratory Data Analysis
│   ├── 02_cleaning.ipynb    # Data Cleaning
│   ├── 03_features.ipynb    # Feature Engineering
│   └── 04_modeling.ipynb    # ML Models
│
├── models/
│   ├── salary_model.pkl     # Trained salary predictor
│   └── category_model.pkl   # Trained job classifier
│
├── app/
│   └── app.py               # Streamlit dashboard (4 tabs)
│
├── requirements.txt
└── README.md
```

---

## 🧠 Key Engineering Decisions

**Why undetected-chromedriver over standard Selenium?**
Indeed Pakistan loads content dynamically via JavaScript. Standard
requests/BeautifulSoup cannot render JS. undetected-chromedriver
bypasses bot detection that blocks standard Selenium.

**Why normalize skills into a separate table?**
Storing skills as a comma-separated string in one column makes
querying impossible. A normalized schema lets us query:
"how many jobs require Python?" in a single SQL statement.

**Why XGBoost for salary prediction?**
Salary data is tabular, sparse (many None values), and contains
categorical features (city, education). XGBoost handles all of
these natively and outperforms linear models on such data.

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
