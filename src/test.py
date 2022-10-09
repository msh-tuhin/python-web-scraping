import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get("https://www.daraz.com.bd/").content, 'html.parser')
soup.prettify()