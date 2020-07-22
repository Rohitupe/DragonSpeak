import requests
from bs4 import BeautifulSoup
import time

url = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?"

allData = requests.get(url)
# print(allData.text)
time.sleep(4)

htmlData = BeautifulSoup(allData.text , 'html.parser')
time.sleep(4)
data = htmlData.find_all("div",class_="maincounter-number")
empty = []
for info in data:
    information = str(info.span.text)
    empty.append(information)
print(empty)


