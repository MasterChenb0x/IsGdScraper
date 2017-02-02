#!/usr/bin/env python
from subprocess import call

call(['./proxy_scraper.php'])

#proxy_file = open('proxies.txt')
#proxies = proxy_file.readlines()
#proxy_file.close()
proxy_file = open('fresh_proxies.txt')
proxies = proxy_file.readlines()
proxy_file.close()

for proxy in proxies:
  call(['./isgd.sh',proxy.replace('\n','')])
