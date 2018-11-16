import os
import yaml
import requests
from bs4 import BeautifulSoup as bs
from downloadImage import downloader

with open("config.yml", 'r') as ymlfile:
    url = yaml.load(ymlfile)

e = 0
unum = 0
print("Press Enter to start: ", end="")
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

try:
    if url[unum] == url[0]:
        imgs = soup.findAll("img")
        downloader(imgs[0]['src'])
    else:
        imgs = soup.findAll("a", {"class": "image_wrapper"})
        downloader(imgs[0].img['data-src'])
except:
    print("\nERROR: Couldn't find an image to download.")
