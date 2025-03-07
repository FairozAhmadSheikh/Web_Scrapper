import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/international"

def fetch_news():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find news articles (updated selector)
    articles = soup.select("h3 a", limit=10)

    for article in articles:
        headline = article.text.strip()
        link = article["href"]
        print(headline, "-", link)

if __name__ == "__main__":
    fetch_news()
