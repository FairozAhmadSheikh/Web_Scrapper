# pip install requests beautifulsoup4 pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the site
url = "https://remoteok.com/remote-dev-jobs"

# Custom headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send GET request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")