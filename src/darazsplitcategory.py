import requests
from bs4 import BeautifulSoup

baseURL = "https://www.daraz.com.bd/"
page = requests.get(baseURL)
soup = BeautifulSoup(page.content, 'html.parser')

mainCategoryLinks = soup.select('a.main-category')
categoryLinks = soup.select('a.category')
subCategoryLinks = soup.select('a.subcategory')

mainHrefs = []
categoryHrefs = []
subHrefs = []

for mlink in mainCategoryLinks:
    mainHrefs.append(mlink['href'])

for link in categoryLinks:
    categoryHrefs.append(link['href'])

for slink in subCategoryLinks:
    subHrefs.append(slink['href'])

print(len(mainHrefs))
print(len(set(mainHrefs)))
print(len(categoryHrefs))
print(len(set(categoryHrefs)))
print(len(subHrefs))
print(len(set(subHrefs)))

# with open("C:\\Users\\Tuhin\\Desktop\\daraz\\darazmain.txt", "w") as f:
#     for href in set(mainHrefs):
#         f.write(href + "\n")
#
# with open("C:\\Users\\Tuhin\\Desktop\\daraz\\darazcategory.txt", "w") as f:
#     for href in set(categoryHrefs):
#         f.write(href + "\n")
with open("C:\\Users\\Tuhin\\Desktop\\daraz\\darazsub.txt", "w") as f:
    for href in set(subHrefs):
        f.write(href + "\n")