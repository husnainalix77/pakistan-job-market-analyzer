"""
indeed_scraper.py
=================
Web scraper for Indeed Pakistan job listings.
Uses Selenium with undetected-chromedriver to bypass bot detection
and BeautifulSoup to parse and extract job data from loaded pages.

Scraped Fields:
    - Job Title
    - Company Name
    - City / Location
    - Salary (where available)

Usage:
    python scraper/indeed_scraper.py

Author: Husnain Maroof
GitHub: https://github.com/husnainalix77
"""
import pandas as pd
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time

def setup_driver() -> object:
    """
    Configure and launch an undetected Chrome browser instance.
    
    Uses undetected-chromedriver to bypass bot detection systems
    that would block standard Selenium WebDriver.
    
    Returns:
        driver (uc.Chrome): Configured Chrome WebDriver instance
    """
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options, version_main=150)
    driver.set_page_load_timeout(60)
    return driver

def scrape_jobs(driver: object, url: str) -> list:
    """
    Navigate to a URL and extract job listings from the page.
    
    Args:
        driver (uc.Chrome): Active Chrome WebDriver instance
        url (str): Indeed Pakistan search URL to scrape
        
    Returns:
        list: List of dictionaries, each containing one job's data.
              Returns empty list if page fails to load.
    """
    try:
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        jobs = []
        job_cards = soup.find_all("div", {"data-testid": "slider_item"})
        
        for card in job_cards:
            title = card.find("span", id=lambda x: x and x.startswith("jobTitle-"))
            title = title.text.strip() if title else None
            company = card.find("span", {"data-testid": "company-name"})
            company = company.text.strip() if company else None
            city = card.find("div", {"data-testid": "text-location"})
            city = city.text.strip() if city else None
            salary_div = card.find("div", id="salaryInfoAndJobType")
            salary = salary_div.text.strip() if salary_div else None
            job = {'Title': title,
                   'Company': company,
                   'City': city,
                   'Salary': salary}
            jobs.append(job)
        return jobs
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

def get_urls(query: str, city: str, num_pages: int) -> list:
    """
    Generate paginated Indeed Pakistan search URLs.
    
    Args:
        query (str): Job search term e.g. 'software engineer'
        city (str): Target city e.g. 'lahore'
        num_pages (int): Number of pages to scrape (each page has ~15 jobs)
        
    Returns:
        list: List of URLs for all pages of the search results
    """
    urls = []
    query = query.replace(" ", "+")
    for page in range(0, num_pages * 10, 10):
        url = f"https://pk.indeed.com/jobs?q={query}&l={city}&start={page}"
        urls.append(url)
    return urls

def run_full_scrape() -> None:
    """
    Execute complete scraping pipeline across all queries and cities.
    
    Scrapes multiple job categories across Lahore, Karachi, and Islamabad.
    Saves results to data/jobs_raw.csv with deduplication handled
    in the database layer.
    
    Returns:
        None — saves results directly to CSV file
    """
    driver = setup_driver()
    queries = [
    "software engineer", "data analyst", "mechanical engineer",
    "accountant", "electrical engineer", "graphic designer",
    "marketing manager", "hr manager", "civil engineer",
    "teacher", "nurse", "sales executive", "python developer",
    "project manager", "business analyst", "network engineer",
    "web developer", "content writer", "customer service",
    "supply chain"
        ]
    cities = ["lahore", "karachi", "islamabad"]
    all_jobs = []
    
    for query in queries:
        for city in cities:
            urls = get_urls(query, city, 10)
            for url in urls:
                print(f"Scraping: {url}")
                jobs = scrape_jobs(driver, url)
                all_jobs.extend(jobs)
                time.sleep(3)
    
    df = pd.DataFrame(all_jobs)
    df.to_csv("data/jobs_raw.csv", index=False)
    print(f"Total Jobs Collected: {len(all_jobs)}")
    driver.quit()
    
# Main Program
if __name__ == "__main__":
    run_full_scrape()
  