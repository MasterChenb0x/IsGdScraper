#!/usr/bin/python

import requests

with open("proxylist.txt", "r") as p:
	for line in p:
		requests.get("https://chenb0x.net/asterisk-the-busy-box", proxies={"http": p, "https": p})

p.close()
