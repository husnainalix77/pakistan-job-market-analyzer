from sqlalchemy.orm import sessionmaker
import pandas as pd
from database.models import Job, engine
import datetime

Session = sessionmaker(bind=engine) # session bound to mysql

def insert_jobs(csv_path):
    df = pd.read_csv(csv_path)
    df = df.drop_duplicates(subset=["Title", "Company", "City"])
    session = Session()
    inserted = 0
    skipped = 0
    try:
        for _, row in df.iterrows():
            existing = session.query(Job).filter_by(
                    title=row["Title"],
                    company=row["Company"],
                    city=row["City"]
            ).first()
            if existing is not None:
                skipped += 1
                continue
            job = Job(
                    title=row["Title"],
                    company=row["Company"],
                    city=row["City"],
                    salary=row["Salary"] if pd.notna(row["Salary"]) else None,
                    date_scraped=datetime.datetime.now()
                )
            session.add(job)
            inserted += 1
                
        session.commit()
        print(f"Inserted: {inserted} | Skipped: {skipped}")
        
    except Exception as e:
        session.rollback()
        print(f"Error inserting jobs: {e}")
    finally:
        session.close()

def get_all_jobs():
    session = Session()
    try:
        jobs = session.query(Job).all()
        df = pd.DataFrame([{
        "job_id": job.job_id,
        "title": job.title,
        "company": job.company,
        "city": job.city,
        "salary": job.salary,
        "date_scraped": job.date_scraped
        } for job in jobs])
        return df       
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return None
    finally:
        session.close() 
    
if __name__ == "__main__":  
    insert_jobs("data/jobs_raw.csv")
    df = get_all_jobs()
    print(df.head())
    print(f"Total jobs in database: {len(df)}")        