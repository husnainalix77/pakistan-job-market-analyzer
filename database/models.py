from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Base Class
Base = declarative_base()
# Connection between MYSQL and Python
engine = create_engine(f"mysql+pymysql://root:{DB_PASSWORD}@localhost/job_market_db")
# SQL Alchemy Model

class Job(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    salary = Column(String(255))
    experience_years = Column(Float)
    education = Column(String(100))
    category = Column(String(100))
    date_posted = Column(Date)
    date_scraped = Column(DateTime)

class Skill(Base):
    __tablename__ = "skills"
    skill_id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey("jobs.job_id"), nullable=False)
    skill_name = Column(String(100), nullable=False)    

# Create all tables in MySQL
Base.metadata.create_all(engine)    
    