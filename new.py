import requests
from bs4 import BeautifulSoup

# Define the target URL
url = "https://en.wikipedia.org/wiki/Machine_learning"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all article titles (assuming they are within <h2> tags)
    articles = soup.find_all('h2')
    
    # Extract and print the data
    for article in articles:
        title = article.text.strip()
        link = article.find('a')['href'] if article.find('a') else "No Link"
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
