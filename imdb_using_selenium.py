from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def scrape_imdb():
    url = "https://www.imdb.com/chart/top/"
    
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service("chromedriver")  # Ensure chromedriver is in your path
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to fully load
        
        # Extract movie titles and ratings
        movies = driver.find_elements(By.XPATH, "//td[@class='titleColumn']/a")
        ratings = driver.find_elements(By.XPATH, "//td[@class='ratingColumn imdbRating']/strong")
        
        print("Top IMDb Movies:")
        for idx, (movie, rating) in enumerate(zip(movies, ratings), 1):
            print(f"{idx}. {movie.text} - Rating: {rating.text}")
    
    finally:
        driver.quit()

# Run the scraper
scrape_imdb()
