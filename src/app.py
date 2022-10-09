import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()

priyoshop_url = "http://www.priyoshop.com/"
daraz_url = "https://www.daraz.com.bd/"
page = requests.get(priyoshop_url)
soup = BeautifulSoup(page.content, 'html.parser')
links = soup.select("ul.top-menu a")
file = open("C:\\Users\\Tuhin\\Desktop\\priyoshop\\priyoshoplinks.txt", "w")
shirtLinks = []
for link in links:
    href = link['href']
    if 'shirts' in href:
        shirtLinks.append(priyoshop_url+href[1:])
    print(priyoshop_url+href[1:])
    file.write(priyoshop_url+href[1:]+"\n")
file.close()

print()
print()
for shirtLink in shirtLinks:
    print(shirtLink)
print(len(shirtLinks))
print(len(links))
print("\n\n")

page = requests.get(daraz_url)
soup = BeautifulSoup(page.content, 'html.parser')
mainCategory = soup.select("a.main-category")
subcategory = soup.select("a.subcategory")
print("Here are the main categories:\n\n")

file = open("C:\\Users\\Tuhin\\Desktop\\daraz\\darazlinks.txt", "w")
darazShirtLinks = []
for link in mainCategory:
    if 'shirt' in link['href']:
        darazShirtLinks.append(link['href'])
    print(link['href'])
    file.write(link['href']+"\n")

print("Here are the sub categories:\n\n")
for link in subcategory:
    if 'shirt' in link['href']:
        darazShirtLinks.append(link['href'])
    print(link['href'])
    file.write(link['href']+"\n")

file.close()

print("here are the shirt links:\n\n")
for link in darazShirtLinks:
    print(link)
print(len(mainCategory))
print(len(subcategory))
print(len(darazShirtLinks))
# link = links[0]['href']
# print(soup.prettify())

print(requests.get(shirtLinks[0]).status_code)
print("Execution time : " + str(time.time() - start_time))