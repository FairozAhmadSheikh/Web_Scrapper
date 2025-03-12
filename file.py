import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_headings_paragraphs(url):
    """
    Scrapes headings (h1-h6) and paragraphs (p) from a website.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        dict: A dictionary containing lists of headings and paragraphs, or None on error.
    """
    try:
        robots_url = urllib.parse.urljoin(url, "/robots.txt")
        try:
            robots_response = requests.get(robots_url)
            if robots_response.status_code == 200:
                robots_txt = robots_response.text
                if "Disallow: /" in robots_txt:
                    print(f"Warning: robots.txt disallows scraping from {url}")
                    return None
        except requests.exceptions.RequestException as e:
            print(f"Warning: Could not access robots.txt: {e}")

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        headings = []
        for i in range(1, 7):  # Scrape h1 to h6
            for heading in soup.find_all(f"h{i}"):
                headings.append(heading.get_text(strip=True))

        paragraphs = []
        for paragraph in soup.find_all("p"):
            paragraphs.append(paragraph.get_text(strip=True))

        return {"headings": headings, "paragraphs": paragraphs}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage (using wikipedia's main page as an example, as it is relatively stable)
example_url = "https://en.wikipedia.org/wiki/Main_Page"

scraped_data = scrape_headings_paragraphs(example_url)

if scraped_data:
    print("Headings:")
    for heading in scraped_data["headings"]:
        print(f"- {heading}")

    print("\nParagraphs:")
    for paragraph in scraped_data["paragraphs"]:
        print(f"- {paragraph}")
else:
    print("Scraping failed.")