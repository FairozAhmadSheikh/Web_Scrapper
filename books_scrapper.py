from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

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
        wait = WebDriverWait(driver, 10)
        
        # Wait until books are loaded
        wait.until(EC.presence_of_element_located((By.XPATH, "//article[@class='product_pod']")))
        
        # Extract book titles, prices, and availability
        books = driver.find_elements(By.XPATH, "//article[@class='product_pod']")
        
        book_data = []
        for book in books:
            title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
            price = book.find_element(By.CLASS_NAME, "price_color").text
            availability = book.find_element(By.XPATH, ".//p[contains(@class, 'instock')]" ).text.strip()
            
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