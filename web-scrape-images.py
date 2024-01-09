import requests
from scrapy import Selector
import urllib.request

# Obtain HTML
html= requests.get('https://all-free-download.com/free-photos/crocodile.html').text

# Initiate selector
selector = Selector(text=html)

# Obtain URLs for the images
URLs = selector.css('img::attr(src)').extract()

# Filter through the URLs to use URLs of images only
images = []
for item in URLs:
    if '.jpg' in item:
        images.append(item) 

# Write each image to a specific directory
number=0
for item in images:
    path= '/Users/briannagrissom/CrocGator/croc'
    urllib.request.urlretrieve(item, path + str(number) +'.jpeg')
    number= number + 1

