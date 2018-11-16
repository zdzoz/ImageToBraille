import os
import yaml
import requests
from bs4 import BeautifulSoup as bs
from downloadImage import downloader

with open("config.yml", 'r') as ymlfile:
    url = yaml.load(ymlfile)

e = 0
unum = 0
print("Press Enter to start: ")
e = input()
try:
    if int(e) == 69:
        unum = 69
    else:
        unum = 0
except:
    pass

print(f"searching with {url[unum]}")
print("Search for: ", end="")
term = input()

if url[unum] == url[0]:
    result = requests.get(f"{url[unum]}{term}&tbm=isch")
else:
    result = requests.get(f"{url[unum]}{term}")
print(result.status_code)

c = result.content

soup = bs(c, 'html.parser')


if not os.path.isdir("temp"):
        os.mkdir("temp")

file = open(os.path.join("temp", "page.html"), "w")
file.writelines(soup.prettify())
file.close()

imgs = soup.findAll("a", {"class": "image_wrapper"})

file = open(os.path.join("temp", "imgs.txt"), 'w')
for tag in imgs:
    file.write(f"{tag.img['data-src']}\n")
file.close()

downloader(imgs[0].img['data-src'])
