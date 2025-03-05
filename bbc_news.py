import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    url = "https://www.bbc.com/news"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    # Send a request to fetch the webpage
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all article titles
        articles = soup.find_all('h3')
        
        if articles:
            print("Latest BBC News Headlines:")
            for idx, article in enumerate(articles, 1):
                print(f"{idx}. {article.get_text(strip=True)}")
        else:
            print("No headlines found. The website structure might have changed.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Run the scraper
scrape_bbc_news()
