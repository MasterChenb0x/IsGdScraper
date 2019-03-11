#!/usr/bin/env python

import socks
import socket
from urllib.request import urlopen

url = 'http://geoiptool.com/'

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150)
socket.socket = socks.socksocket

response = urlopen(url)
print(response.read())
