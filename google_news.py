from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape_google_news():
    url = "https://news.google.com/"
    
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    
    # Use WebDriver Manager to handle ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to fully load
        
        # Extract all headlines (h3 tags)
        headlines = driver.find_elements(By.TAG_NAME, "h3")
        
        news_data = []
        for idx, headline in enumerate(headlines, 1):
            news_data.append({"Rank": idx, "Headline": headline.text})
        
        # Convert to DataFrame and save as CSV
        df = pd.DataFrame(news_data)
        df.to_csv("google_news_headlines.csv", index=False)
        
        print("Google News Headlines Scraped and Saved to google_news_headlines.csv")
    
    finally:
        driver.quit()

# Run the scraper
scrape_google_news()
