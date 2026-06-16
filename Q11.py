""". Web Scraping Task: 
• Scrape this website: http://quotes.toscrape.com
• Get all quotes and authors
• Print only quotes by 'Albert Einstein'
• Save ALL quotes to 'quotes.json'
• Print total number of quotes scraped"""

import requests
from bs4 import BeautifulSoup
import json

try:
    url = "http://quotes.toscrape.com"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quote_data = []

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:

        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        quote_data.append({
            "quote": text,
            "author": author
        })

        if author == "Albert Einstein":
            print(text)

    with open("quotes.json", "w") as file:
        json.dump(quote_data, file, indent=4)

    print("Total Quotes:", len(quote_data))

except Exception as e:
    print("Error:", e)