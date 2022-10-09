import requests
from bs4 import BeautifulSoup
from src.classDefs import ShirtInfo
import time
import re

start_time = time.time()
baseUrl = "http://www.priyoshop.com/"
shirtUrl = baseUrl + "shirts"
offer999 = baseUrl + "999-tk-offer"
comboOffer = baseUrl + "combo-offer-2"
comboPage2 = "http://www.priyoshop.com/combo-offer-2#/pageSize=30&viewMode=grid&orderBy=15&pageNumber=2"
page = requests.get(comboOffer)
soup = BeautifulSoup(page.content, 'html.parser')
images = soup.select('div.product-item div.picture a img')
prices = soup.select('div.product-item span.price.actual-price')

shirts = []
# for image in images:
#     print(image['src'])

for price in prices:
    print(price.text)
print(len(images))
print(len(prices))

for image, price in zip(images, prices):
    shirts.append(ShirtInfo(image['src'], image['title'], price.text))

with open("C:\\Users\\Tuhin\\Desktop\\priyoshop\\comborlinknprice.txt", "w") as f:
    for shirt in shirts:
        f.write("Image Src: " + shirt.imageSrc + "\n")
        f.write("Title: " + shirt.title + "\n")
        f.write("Price: " + shirt.price + "\n")
for shirt in shirts:
    print(shirt.imageSrc)
    rawImage = requests.get(shirt.imageSrc)
    imgName = (shirt.imageSrc.split('/')).pop().split('.')[0]
    with open("C:\\Users\\Tuhin\\Desktop\\combophotos\\"+ imgName +".jpeg", 'wb') as file:
        for chunk in rawImage:
            file.write(chunk)

# img = requests.get(shirts[0].imageSrc)
# with open("C:\\Users\\tuhin\\Desktop\\"+shirts[0].title+".jpeg", 'wb') as file:
#     for chunk in img:
#         file.write(chunk)

print("Execution time : " + str(time.time() - start_time))

