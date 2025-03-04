import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    # Send an HTTP request to fetch the page
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the page
        title = soup.find("h1").text

        # Extract the first paragraph
        first_paragraph = soup.find("p").text.strip()

        # Extract all headings (h2 and h3)
        headings = [heading.text.strip() for heading in soup.find_all(["h2", "h3"])]

        # Extract all links within the content section
        content_div = soup.find("div", {"class": "mw-parser-output"})
        links = [a["href"] for a in content_div.find_all("a", href=True) if a["href"].startswith("/wiki/")]

        # Display the results
        print(f"Title: {title}\n")
        print(f"First Paragraph: {first_paragraph}\n")
        print("Headings:")
        for h in headings:
            print(f"- {h}")

        print("\nExtracted Links:")
        for link in links[:10]:  # Displaying only first 10 links
            print(f"https://en.wikipedia.org{link}")

    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")

# Wikipedia Machine Learning Page
wiki_url = "https://en.wikipedia.org/wiki/Machine_learning"
scrape_wikipedia(wiki_url)
