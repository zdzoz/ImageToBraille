import urllib.request
import string
import random

def downloader(image_url):
    file_name = random.randrange(1,10000)
    random_str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    full_file_name = random_str + str(file_name) + '.png'
    urllib.request.urlretrieve(image_url,full_file_name)


downloader("https://s1.narvii.com/image/ws45li53clncpxdjivdk7o3wars77rxa_hq.jpg")