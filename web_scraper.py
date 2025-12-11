# Level 3 - Task 1
# Web Scraper using BeautifulSoup
# Cognifyz Technologies Internship Project

import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Check status
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print("\n🔍 Extracted Quotes from Website:\n")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for q, a in zip(quotes, authors):
        print(f"✨ Quote: {q.text}")
        print(f"👤 Author: {a.text}\n")

else:
    print("❌ Failed to fetch the webpage!")
