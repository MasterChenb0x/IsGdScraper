#!/usr/bin/python
from subprocess import call

call(['./proxy-scraper.py'])

proxy_file = open('proxylist.txt')
proxies = proxy_file.readlines()
proxy_file.close()
#proxy_file = open('fresh_proxies.txt')
#proxies = proxies + proxy_file.readlines()
#proxy_file.close()

for proxy in proxies:
  call(['./isgd.py',proxy.replace('\n','')])
