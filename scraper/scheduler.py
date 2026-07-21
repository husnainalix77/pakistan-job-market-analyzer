import schedule
import time
from indeed_scraper import run_full_scrape

schedule.every().sunday.at("00:00").do(run_full_scrape)
print("Scheduler running. Waiting for Sunday midnight...")
while True:
    schedule.run_pending()
    time.sleep(60)