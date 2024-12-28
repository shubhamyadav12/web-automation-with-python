import requests

import html5lib


from bs4 import BeautifulSoup


response = requests.get("https://en.wikipedia.org/wiki/Fallacy")

soup = BeautifulSoup(response.content, "html5lib")
 
print(soup.prettify())