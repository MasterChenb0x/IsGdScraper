#!/usr/bin/python3

from selenium import webdriver
import time

driver=webdriver.Firefox()
#driver.get("https://u.cubeupload.com/Beans/gVgzF4.jpeg")

pics = []
with open("image-filez.txt", "r") as images:
    for image in images:
        pics.append(image[:-1])
driver.set_page_load_timeout(10)
for p in pics:
    try:
        driver.get(p)
        time.sleep(3)
    except:
        print("Moving on...")

#print(pics)
