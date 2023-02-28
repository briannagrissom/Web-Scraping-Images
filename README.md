# WebScrapingImages
Web scraping images to use for image classification project.

This involved:

1) Loading the website's HTML into a Python variable through the requests library.
2) Using XPATH/CSS through a scrapy Selector to extract links for the images.
3) Filter the links through a for loop to ensure the links only contain images.
4) Use the urllib package within a for loop to quickly and efficiently download the image links to a specified folder.
