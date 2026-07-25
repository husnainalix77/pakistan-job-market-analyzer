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
| Database | MySQL + SQLAlchemy ORM | Structured storage with ORM |
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
| 2 | Web Scraping — Indeed Pakistan | ✅ Complete |
| 3 | Database Storage with SQLAlchemy | ✅ Complete |
| 4 | Data Cleaning & EDA | ✅ Complete |
| 5 | Feature Engineering | ⏳ Upcoming |
| 6 | ML Modeling (Regression + Classification) | ⏳ Upcoming |
| 7 | Streamlit Interactive Dashboard | ⏳ Upcoming |
| 8 | Portfolio Polish & Deployment | ⏳ Upcoming |

---

## 📊 Phase 2 Results — Web Scraping

- ✅ Built automated scraper using Selenium + undetected-chromedriver
- ✅ Bypassed Cloudflare bot detection — switched to Indeed Pakistan
- ✅ Implemented pagination — scrapes 10 pages per search query
- ✅ Scraped **5 job categories × 3 cities × 10 pages = 1,566 raw listings**
- ✅ Weekly scheduler configured for automated scraping every Sunday

**Categories scraped:** Software Engineer, Data Analyst, Mechanical Engineer, Accountant, Electrical Engineer

**Cities covered:** Lahore, Karachi, Islamabad

---

## 🗄️ Phase 3 Results — Database Storage

- ✅ SQLAlchemy ORM models for `jobs` and `skills` tables
- ✅ Secure MySQL connection via `.env` — password never in code
- ✅ Duplicate detection — skips existing records on re-run
- ✅ **620 unique jobs stored in MySQL**

```
Run 1: Inserted: 620 | Skipped: 0
Run 2: Inserted: 0   | Skipped: 620  ← duplicate detection working
```

---

## 🔍 Phase 4 Results — Data Cleaning & EDA

- ✅ Standardized 24 city name variations into 5 clean categories
- ✅ Extracted job categories using rule-based keyword matching (98.5% accuracy)
- ✅ 5 professional visualizations with data-driven insights
- ✅ Cleaned dataset saved to `data/cleaned_data.csv`

### Key Findings from EDA

| # | Finding | Insight |
|---|---|---|
| 1 | Software Engineering = 61% of all jobs | Pakistan's job market is overwhelmingly tech-focused |
| 2 | Karachi (236) ≈ Lahore (231) | Both are equally strong tech hubs — 75% of all listings |
| 3 | 100% of listings hide salary | Makes our salary predictor genuinely valuable |
| 4 | Contour Software has 24 listings | Most active employer — 50% ahead of second place |
| 5 | SQA Engineer is 3rd most common title | Quality assurance is highly demanded in Pakistan |

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

# 8. Run EDA notebook
jupyter notebook notebooks/01_EDA.ipynb

# 9. Launch dashboard (Phase 7)
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
│   ├── db_manager.py        # Insert, query, duplicate detection
│   └── schema.sql           # Raw SQL schema reference
│
├── notebooks/
│   └── 01_EDA.ipynb         # Data cleaning & EDA — 5 visualizations
│
├── models/
│   ├── salary_model.pkl     # Trained salary predictor
│   └── category_model.pkl   # Trained job classifier
│
├── app/
│   └── app.py               # Streamlit dashboard (4 tabs)
│
├── .env                     # MySQL credentials (not in repo)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Key Engineering Decisions

**Why undetected-chromedriver?**
Indeed Pakistan loads content via JavaScript. undetected-chromedriver
bypasses bot detection that blocks standard Selenium.

**Why SQLAlchemy ORM?**
ORM lets us work with Python objects instead of SQL strings. Portable —
anyone can recreate the database by running models.py.

**Why .env for credentials?**
Passwords never appear in code. Industry standard for all projects.

**Why rule-based category extraction?**
Keyword matching on job titles achieves 98.5% accuracy without
needing training data — fast, interpretable, and maintainable.

**Why normalize skills into a separate table?**
Enables efficient querying — "how many jobs require Python?" in one SQL statement.

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
