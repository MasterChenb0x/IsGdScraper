#!/usr/bin/python
import requests
import sys

urls = 0

print "Working..."
try:
	with open("testlinks.txt", "r") as f:
		with open("valid.txt", "w") as v:
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
