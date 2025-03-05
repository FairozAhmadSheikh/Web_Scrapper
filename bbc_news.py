import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    url = "https://www.bbc.com/news"
    
    # Send a request to fetch the webpage
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all article titles
        articles = soup.find_all('h3')
        
        print("Latest BBC News Headlines:")
        for idx, article in enumerate(articles, 1):
            print(f"{idx}. {article.get_text(strip=True)}")
    else:
        print("Failed to retrieve the webpage.")

# Run the scraper
scrape_bbc_news()
