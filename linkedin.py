from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define your LinkedIn credentials
linkedin_username = ""
linkedin_password = ""

# Path to your ChromeDriver
chromedriver_path = '/usr/local/bin/chromedriver'

# Setup Selenium with Chrome web driver using Service
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Open LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Locate the username and password fields
username_field = driver.find_element(By.NAME, 'session_key')
password_field = driver.find_element(By.NAME, 'session_password')

# Input login credentials
username_field.send_keys(linkedin_username)
password_field.send_keys(linkedin_password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(3)

# After login, navigate to a public profile page

# Wait for the page to load
time.sleep(3)

# Define scrape_jobs function after the profile extraction
def scrape_jobs(keyword, location):
    # Search jobs with a keyword and location
    search_url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location={location}"
    driver.get(search_url)
    time.sleep(3)

    # Scrape job titles and links
    jobs = driver.find_elements(By.CSS_SELECTOR, 'a.job-card-container__link.job-card-list__title')
    for job in jobs:
        print(f"Job Title: {job.text}")
        print(f"Link: {job.get_attribute('href')}\n")

# Example usage: Scraping job listings
scrape_jobs('Data Scientist', 'New York, New York')

# Close the browser
driver.quit()
