import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/international"

def fetch_news():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find article sections
    articles = soup.find_all("a", class_="u-faux-block-link__overlay", limit=10)

    for article in articles:
        print(article.text.strip(), "-", article["href"])

if __name__ == "__main__":
    fetch_news()
