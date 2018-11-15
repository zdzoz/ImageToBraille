import urllib.request
import string
import random
import os

def downloader(image_url):
    file_name = random.randrange(1,10000)
    random_str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    full_file_name = random_str + str(file_name) + '.png'
    if not os.path.isdir("pics"):
        os.mkdir("pics")
    urllib.request.urlretrieve(image_url, os.path.join("pics", full_file_name))