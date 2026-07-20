from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time

def setup_driver():
    """Configures and launches an undetected Chrome browser instance"""
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options, version_main=150)
    driver.set_page_load_timeout(60)
    return driver

def scrape_jobs(driver, url):
    """Navigates to the URL and waits for page to load"""
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

# Main Program
if __name__ == "__main__":
    driver = setup_driver()
    url = "https://pk.indeed.com/q-ai-ml-engineer-l-lahore-jobs.html?vjk=81354d08b1fa35d6"
    jobs = scrape_jobs(driver, url)
    for job in jobs:
        print(job)
    driver.quit()    