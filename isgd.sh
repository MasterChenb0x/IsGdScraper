#!/bin/bash

# Set the proxy from the argument passed by the proxy_scraper.php file
export http_proxy=$1

# Set the link var to one of the generated is.gd link parameters
link=`head -1 testlinks.txt`
if [ -z "$link" ]; then
	echo "EOF"
	exit 1
fi

# Resolve link and store for later viewing
curl -Ls -o /dev/null -m 2 -w %{url_effective} http://is.gd/$link >> urls-resolved.txt
echo -e "\n" >> urls-resolved.txt

# Remove the generated link from the list
sed -i '1d' testlinks.txt

