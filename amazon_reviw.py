from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Function to scrape Amazon reviews using Selenium
def scrape_amazon_reviews(product_url, pages=1):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    reviews = []

    for page in range(1, pages + 1):
        review_url = f"{product_url}&pageNumber={page}"
        driver.get(review_url)
        time.sleep(2)  # Wait for page to load
        
        # Find all review containers
        review_containers = driver.find_elements(By.XPATH, "//div[@data-hook='review']")
        
        if not review_containers:
            print("No reviews found or Amazon blocked the request.")
            break
        
        for review in review_containers:
            try:
                rating = review.find_element(By.XPATH, ".//i[@data-hook='review-star-rating']").text.strip()
                title = review.find_element(By.XPATH, ".//a[@data-hook='review-title']").text.strip()
                reviewer = review.find_element(By.XPATH, ".//span[@class='a-profile-name']").text.strip()
                full_review = review.find_element(By.XPATH, ".//span[@data-hook='review-body']").text.strip()

                reviews.append([reviewer, rating, title, full_review])

                print(f"⭐⭐⭐ REVIEW ⭐⭐⭐")
                print(f"Reviewer: {reviewer}")
                print(f"Rating: {rating}")
                print(f"Title: {title}")
                print(f"Review: {full_review}\n")
                print("-" * 60)

            except Exception as e:
                continue  # Skip if elements are missing

    driver.quit()

    # Save to CSV
    with open("amazon_reviews.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Reviewer", "Rating", "Title", "Review"])
        writer.writerows(reviews)

    print(f"\n✅ {len(reviews)} reviews saved to 'amazon_reviews.csv'")

# Example Amazon Review Page URL (Change ASIN)
amazon_review_url = "https://www.amazon.com/product-reviews/B09G9FPHY3/"
scrape_amazon_reviews(amazon_review_url, pages=2)
