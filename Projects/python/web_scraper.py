import requests
from bs4 import BeautifulSoup

"""
1. Url of the website to scrape
2. Send an HTTP GET request to the url
3. Parse the HTML content of the page
4. Find specific tags with a specific class
5. Print the tags
6. Run the scraper

"""
try:
    url = "https://www.news24.com"

    response = requests.get(url)

    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    target_tags = soup.find_all("div", class_ = "example-class")

    if target_tags:
        for tag in target_tags:
            print(tag)

    else:
        print(f"No tags withh the class 'example-class'")

except request.excerptions.RequestException as e:
    print(f"An error occurred: {e}")
          