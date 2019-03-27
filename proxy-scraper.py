#!/usr/local/bin/python3

import requests
from bs4 import BeautifulSoup
import random
import sys

# Functionas
def get_proxies():
	"""
	Grab a list of proxies from which to scrape.
	"""
	proxyDomain = ['https://sslproxies.org',
		'https://free-proxy-list.net']
	proxies = []

	for site in proxyDomain:
		r = requests.get(site)

		soup = BeautifulSoup(r.content, 'html.parser')
	
		table = soup.find('table',{'id' : 'proxylisttable'})
		for row in table.find_all('tr'):
			columns = row.find_all('td')
			try:
				proxies.append("%s:%s" % (columns[0].get_text(),columns[1].get_text()))
			except:
				pass
	return proxies



# Constants
user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

#url = "https://chenb0x.net/asterisk-the-busy-box"

proxylist = get_proxies()
"""
for proxy in proxylist[:]:
	print(proxy)
	proxylist.remove(proxy)
	print("{0} proxies left".format(len(proxylist)))


for proxy in proxylist:
	print(proxy)
	user_agent = random.choice(user_agent_list)
	headers = {"User-Agent": user_agent}
	try:
		print("Scraping: " + url)
		r = requests.head(url, allow_redirects=True, timeout=3, proxies={"http": proxy, "https": proxy}, headers=headers)
	except:
		pass

#print(proxies)
#for proxy in proxylist[:]:

urls = 0

"""
with open("links-generated.txt", "r") as f:
	with open("valid.txt", "w") as v:
		try:
			proxy = proxylist[random.randint(0,len(proxylist)-1)]
			proxylist.remove(proxy)
			for i in range(1,3600):
		except ValueError:
			# Ran out of proxies! Get more.
			proxylist = get_proxies()

"""
			try:
				for line in f:
					urls += 1
					if len(line) != 7: continue
					try:
						url = "https://is.gd/" + line[:-1]
						r = requests.head(url, allow_redirects=True, timeout=1)
						if "is.gd" not in r.url:
							v.write("{1} resolved to: {0}\n".format(r.url, url))
					except Exception as e:
						continue

	except KeyboardInterrupt:
		print "\nTested {0} URLs.".format(urls)
"""
