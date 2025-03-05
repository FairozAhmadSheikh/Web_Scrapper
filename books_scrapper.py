from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_books():
    url = "http://books.toscrape.com/"
    
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
        time.sleep(3)  # Allow time for the page to load
        
        # Extract book titles, prices, and availability
        books = driver.find_elements(By.XPATH, "//article[@class='product_pod']")
        
        book_data = []
        for book in books:
            title = book.find_element(By.TAG_NAME, "h3").text
            price = book.find_element(By.CLASS_NAME, "price_color").text
            availability = book.find_element(By.CLASS_NAME, "instock.availability").text.strip()
            
            book_data.append({
                "Title": title,
                "Price": price,
                "Availability": availability
            })
        
        # Convert to DataFrame and save as CSV
        df = pd.DataFrame(book_data)
        df.to_csv("books_data.csv", index=False)
        
        print("Books data scraped and saved to books_data.csv")
    
    finally:
        driver.quit()

# Run the scraper
scrape_books()
