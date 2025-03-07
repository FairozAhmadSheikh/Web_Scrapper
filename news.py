import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/international"

def fetch_news():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        print("❌ Failed to fetch the website")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("h3", class_="fc-item__title", limit=10)

    print("\n🔹 Latest News 🔹\n")
    for i, article in enumerate(articles, start=1):
        headline = article.text.strip()
        link = article.a["href"]
        print(f"{i}. {headline} → {link}")

if __name__ == "__main__":
    fetch_news()
