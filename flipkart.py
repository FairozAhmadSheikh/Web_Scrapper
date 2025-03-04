import requests
from bs4 import BeautifulSoup

def scrape_flipkart_reviews(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = requests.get(product_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract review containers
        reviews = soup.find_all("div", {"class": "_27M-vq"})

        if not reviews:
            print("No reviews found. Flipkart might be blocking automated scraping.")
            return
        
        print(f"Scraping reviews from: {product_url}\n")
        
        # Loop through reviews and extract details
        for review in reviews[:10]:  # Scrape first 10 reviews
            rating = review.find("div", {"class": "_3LWZlK"})
            title = review.find("p", {"class": "_2-N8zT"})
            full_review = review.find("div", {"class": "t-ZTKy"})
            reviewer = review.find("p", {"class": "_2sc7ZR _2V5EHH"})
            
            print("⭐⭐⭐ REVIEW ⭐⭐⭐")
            print(f"Reviewer: {reviewer.text.strip() if reviewer else 'Unknown'}")
            print(f"Rating: {rating.text.strip() if rating else 'No rating'} / 5")
            print(f"Title: {title.text.strip() if title else 'No title'}")
            print(f"Review: {full_review.text.strip() if full_review else 'No review'}")
            print("-" * 60)

    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")

# Example Flipkart product page (modify as needed)
flipkart_product_url = "https://www.flipkart.com/apple-iphone-14-pro-space-black-128-gb/p/itmdb32e3c997112"  # Example product
scrape_flipkart_reviews(flipkart_product_url)
