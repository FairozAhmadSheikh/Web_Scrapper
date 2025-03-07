import requests
from bs4 import BeautifulSoup

# Target news website (public access)
URL = "https://www.theguardian.com/international"

def fetch_news():
    # Send a GET request to fetch the webpage
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    
    # Check if request was successful
    if response.status_code != 200:
        print("❌ Failed to fetch the website")
        return
    
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all news headlines (h3 elements with class)
    articles = soup.find_all("h3", class_="fc-item__title", limit=10)  # Get top 10
    
    print("\n🔹 Latest News from The Guardian 🔹\n")
    
    # Loop through each news item and extract title + link
    for i, article in enumerate(articles, start=1):
        headline = article.text.strip()
        link = article.a["href"]
        
        print(f"{i}. 📰 {headline}")
        print(f"   📎 {link}")
        print("-" * 80)

if __name__ == "__main__":
    fetch_news()
