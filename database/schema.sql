CREATE DATABASE IF NOT EXISTS job_market_db;
USE job_market_db;

DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS jobs;

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