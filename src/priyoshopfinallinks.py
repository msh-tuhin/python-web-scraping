import requests
from bs4 import BeautifulSoup

baseURL = "http://priyoshop.com/"
soup = BeautifulSoup(requests.get(baseURL).content, 'html.parser')
sublinks = soup.select('ul.sublist li a.with-subcategories')
links = soup.select('ul.sublist li a')
links_href = []
sublinks_href = []
links_products = []
sublinks_products = []
file = open("C:\\Users\\Tuhin\\Desktop\\priyoshop\\priyoshopfinallinks2.txt", "w")
file2 = open("C:\\Users\\Tuhin\\Desktop\\priyoshop\\products.txt", "w")
for link in links:
    href = baseURL + link['href'][1:]
    links_href.append(href)
    links_products.append(link.text.strip())

for link in sublinks:
    href = baseURL + link['href'][1:]
    sublinks_href.append(href)
    sublinks_products.append(link.text.strip())

links_products = set(links_products) - set(sublinks_products)
links_href = set(links_href) - set(sublinks_href)
print(len(links_href))
print(len(set(links_products)))
for link_href in links_href:
    file.write(link_href + "\n")
# products = set(links_products)
for product in set(links_products):
    file2.write(product.strip() + "\n")
file.close()
file2.close()


