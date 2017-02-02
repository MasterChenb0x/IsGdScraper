#!/bin/bash
export http_proxy=$1

link=`head -1 testlinks.txt`
if [ -z "$link" ]; then
	echo "EOF"
	exit 1
fi
curl -Ls -o /dev/null -m 2 -w %{url_effective} http://is.gd/$link >> urls-resolved.txt
#curl -Ls -o /dev/null -m 2 -w %{url_effective} http://chenb0x.net/index.html 
echo -e "\n" >> urls-resolved.txt
sed -i '1d' testlinks.txt

