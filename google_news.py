from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_google_news():
    url = "https://news.google.com/"
    
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    # Use WebDriver Manager to handle ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        
        # Scroll down to load more content
        body = driver.find_element(By.TAG_NAME, "body")
        for _ in range(5):  # Adjust the range for more scrolling
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
        
        # Wait until headlines are visible
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        
        # Extract all headlines (h3 tags)
        headlines = driver.find_elements(By.TAG_NAME, "h3")
        
        news_data = []
        for idx, headline in enumerate(headlines, 1):
            if headline.text.strip():  # Ignore empty headlines
                news_data.append({"Rank": idx, "Headline": headline.text.strip()})
        
        # Convert to DataFrame and save as CSV
        df = pd.DataFrame(news_data)
        df.to_csv("google_news_headlines.csv", index=False)
        
        print("Google News Headlines Scraped and Saved to google_news_headlines.csv")
    
    finally:
        driver.quit()

# Run the scraper
scrape_google_news()