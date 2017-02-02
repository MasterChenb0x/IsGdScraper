#!/usr/bin/env python
from subprocess import call

# Scrape for new proxies
call(['./proxy_scraper.php'])

# Save proxies to a file
proxy_file = open('fresh_proxies.txt')
proxies = proxy_file.readlines()
proxy_file.close()

# Every proxy address scrapes to resolve one is.gd url
for proxy in proxies:
  call(['./isgd.sh',proxy.replace('\n','')])
