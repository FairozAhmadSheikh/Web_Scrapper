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

# Find job listings
jobs = soup.find_all("tr", class_="job")

job_data = []

# Extract details from each job posting
for job in jobs:
    try:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("div", class_="location").text.strip() if job.find("div", class_="location") else "Worldwide"
        tags = [tag.text.strip() for tag in job.find_all("span", class_="tag")]
        link = "https://remoteok.com" + job.get("data-href")

        job_data.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Tags": ", ".join(tags),
            "Link": link
        })
    except Exception as e:
        print("Error parsing job:", e)
# Convert to DataFrame
df = pd.DataFrame(job_data)

# Save to CSV
df.to_csv("remote_jobs.csv", index=False)