import os
import yaml
import requests
from bs4 import BeautifulSoup as bs
from downloadImage import downloader

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

url = cfg['url']

print("Search for: ", end="")
term = input()

result = requests.get(f"{url}{term}")
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

# downloader("https://s1.narvii.com/image/ws45li53clncpxdjivdk7o3wars77rxa_hq.jpg")