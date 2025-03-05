import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    # Send a request to fetch the webpage
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all quotes
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        
        if quotes:
            print("Quotes from Quotes to Scrape:")
            for idx, (quote, author) in enumerate(zip(quotes, authors), 1):
                print(f"{idx}. {quote.get_text()} - {author.get_text()}")
        else:
            print("No quotes found. The website structure might have changed.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Run the scraper
scrape_quotes()