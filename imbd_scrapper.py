import requests
from bs4 import BeautifulSoup

def scrape_imdb():
    url = "https://www.imdb.com/chart/top/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    # Send a request to fetch the webpage
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find movie titles and ratings
        movies = soup.find_all('td', class_='titleColumn')
        ratings = soup.find_all('td', class_='ratingColumn imdbRating')
        
        if movies:
            print("Top IMDb Movies:")
            for idx, (movie, rating) in enumerate(zip(movies, ratings), 1):
                title = movie.a.get_text()
                rating = rating.strong.get_text() if rating.strong else "N/A"
                print(f"{idx}. {title} - Rating: {rating}")
        else:
            print("No movie data found. The website structure might have changed.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Run the scraper
scrape_imdb()
