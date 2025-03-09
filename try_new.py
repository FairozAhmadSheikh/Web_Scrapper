import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_website(url, target_tags=None, target_attributes=None):
    
    try:
        # Check robots.txt (basic implementation)
        robots_url = urllib.parse.urljoin(url, "/robots.txt")
        try:
           robots_response = requests.get(robots_url)
           if robots_response.status_code == 200:
               robots_txt = robots_response.text
               if "Disallow: /" in robots_txt: # very basic check. more robust parsing is needed for a real application.
                   print(f"Warning: robots.txt disallows scraping from {url}")
                   return [] # return empty list to stop scraping.
        except requests.exceptions.RequestException as e:
            print(f"Warning: Could not access robots.txt: {e}")

        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, "html.parser")
        results = []

        if target_tags:
            for tag_name in target_tags:
                tags = soup.find_all(tag_name, attrs=target_attributes) if target_attributes else soup.find_all(tag_name)
                for tag in tags:
                    results.append(tag.get_text(strip=True)) #Get text and remove extra whitespace.

        else:
            # Extract all text if no tags are specified.
            results = [text for text in soup.stripped_strings]

        return results

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Example usage (replace with your desired URL and tags/attributes):
example_url = "https://www.example.com" # Be sure to use a site you are allowed to scrape.
example_tags = ["p", "h1"]  # Example tags to extract
example_attributes = {'class': 'example-class'} #Example attribute filtering.

scraped_data = scrape_website(example_url, example_tags) #If you want all text, remove the example_tags argument.

if scraped_data:
    for item in scraped_data:
        print(item)
else:
    print("No data scraped or an error occurred.")

# Another example without specific tags (extracts all text):
all_text = scrape_website("https://www.wikipedia.com")
if all_text:
  print("\nAll Text:")
  for text in all_text:
      print(text)