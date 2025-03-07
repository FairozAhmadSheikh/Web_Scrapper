import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/international"

def fetch_news():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("h3", class_="fc-item__title", limit=10)

    for article in articles:
        print(article.text.strip(), "-", article.a["href"])

if __name__ == "__main__":
    fetch_news()
