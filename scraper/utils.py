"""
utils.py
========
Utility functions shared across the Pakistan Job Market Analyzer pipeline.
Used by both notebooks and the Streamlit dashboard.

Functions:
    - classify_city: Standardize city name variations
    - classify_category: Extract job category from title
    - extract_seniority: Extract seniority level from title

Author: Husnain Maroof
GitHub: https://github.com/husnainalix77
"""
def classify_city(city:str) -> str:
    """
    Standardize city name variations to 5 clean categories.
    
    Args:
        city (str): Raw city name from scraped data
        
    Returns:
        str: Standardized city name — Lahore, Karachi, Islamabad, 
             Rawalpindi, or Other
    """
    if city.startswith("Lahore"):
        return "Lahore"
    elif city.startswith("Karachi") or city in  ["Korangi", "Korangi Creek", "Drigh Colony", "New Karachi"]:
        return "Karachi"
    elif city.startswith("Rawalpindi"):
        return "Rawalpindi"
    elif city.startswith("Islamabad"):
        return "Islamabad"
    else:
        return "Other"    

def classify_category(title: str) -> str:
    """Classify job title into a category using keyword matching."""
    title = title.lower()
    if any(word in title for word in [
            "mechanical", "civil", "electrical", "mep", "solar", "hvac",
            "plc", "mechatronics", "automation", "firmware", "instrumentation",
            "structural", "production", "manufacturing"
        ]):
            return "Engineering"
    elif any(word in title for word in [
        "software", "developer", "qa", "sqa", "flutter", "ios", "android",
        "java", "python", "backend", "frontend", "full stack", "fullstack",
        "wordpress", "react", "node", "php", "laravel", "game", "mobile",
        "web", "quality assurance", "dev ops", "devops", "engineer",
        "architect", "intern", "trainee", "fresh graduate"
    ]):
        return "Software Engineering"
    
    elif any(word in title for word in [
        "data", "analyst", "ml", "machine learning", "artificial intelligence",
        "ai", "llm", "nlp", "deep learning", "business intelligence", "power bi"
    ]):
        return "Data Science & AI"
    
    elif any(word in title for word in [
        "accountant", "finance", "audit", "tax", "accounts", "bookkeeper",
        "payroll", "financial", "cost accountant"
    ]):
        return "Finance & Accounting"
    
    elif any(word in title for word in [
        "teacher", "lecturer", "professor", "instructor", "tutor"
    ]):
        return "Education"
    
    elif any(word in title for word in [
        "marketing", "sales", "content", "seo", "social media", "brand",
        "digital marketing", "copywriter"
    ]):
        return "Sales & Marketing"
    
    elif any(word in title for word in [
        "hr", "human resource", "recruiter", "talent", "people operations"
    ]):
        return "Human Resources"
    
    elif any(word in title for word in [
        "network", "devops", "cloud", "infrastructure", "system admin",
        "cybersecurity", "security", "noc", "soc"
    ]):
        return "IT Infrastructure"
    
    elif any(word in title for word in [
        "manager", "business analyst", "project manager", "product manager",
        "product owner", "scrum", "agile", "operations"
    ]):
        return "Management"
    
    elif any(word in title for word in [
        "designer", "ui", "ux", "graphic", "creative", "visual"
    ]):
        return "Design"
    
    else:
        return "Other"

def extract_seniority(title: str) -> int:
    """
    Extract seniority level from job title using keyword matching.
    
    Args:
        title (str): Job title from scraped listing
        
    Returns:
        int: Seniority level — 0=Junior, 1=Mid, 2=Senior, 3=Lead
    """
    title = title.lower()
    if any(word in title for word in ["junior", "trainee", "fresh", "associate", "intern"]):
        return 0
    elif any(word in title for word in ["senior", "lead", "principal", "staff"]):
        return 2
    elif any(word in title for word in ["manager", "head", "director"]):
        return 3
    else:
        return 1 # mid level