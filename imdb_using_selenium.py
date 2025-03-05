from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_imdb():
    url = "https://www.imdb.com/chart/top/"
    
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    # Use WebDriver Manager to handle ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to fully load
        
        # Extract movie titles, ratings, and years
        movies = driver.find_elements(By.XPATH, "//td[@class='titleColumn']/a")
        years = driver.find_elements(By.XPATH, "//td[@class='titleColumn']/span")
        ratings = driver.find_elements(By.XPATH, "//td[@class='ratingColumn imdbRating']/strong")
        
        movie_data = []
        
        for idx, (movie, year, rating) in enumerate(zip(movies, years, ratings), 1):
            movie_data.append({
                "Rank": idx,
                "Title": movie.text,
                "Year": year.text.strip("()"),
                "Rating": rating.text
            })
        
        # Convert to DataFrame and save as CSV
        df = pd.DataFrame(movie_data)
        df.to_csv("imdb_top_movies.csv", index=False)
        
        print("Top IMDb Movies Scraped and Saved to imdb_top_movies.csv")
    
    finally:
        driver.quit()

# Run the scraper
scrape_imdb()