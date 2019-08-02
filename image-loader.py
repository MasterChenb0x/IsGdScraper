#!/usr/bin/python3

from selenium import webdriver
import time

driver=webdriver.Firefox()

pics = []

# Open previously sorted file of images
with open("image-filez.txt", "r") as images:
    for image in images:
        pics.append(image[:-1])

# Load each image into your default browser
driver.set_page_load_timeout(10)
for p in pics:
    try:
        driver.get(p)
        time.sleep(3)
    except:
        print("Moving on...") # Skip images that have trouble resolving

