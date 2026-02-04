url = "https://dhrumilmehta.com/"

import requests
response = requests.get(url)

import bs4
soup = bs4.BeautifulSoup(response.text, "html.parser")

css_selector = "#social-media-links li a"
elements = soup.select(css_selector)

# get the href attributes
link_urls = [element['href'] for element in elements]

print(link_urls)