#!/bin/bash

filename="$1"
while read -r line
do
	echo -e 'AUTHENTICATE ""\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051
	torify curl http://whatismyip.org >> test-urls-resolved.txt
	echo -e "\n" >> test-urls-resolved.txt
	sleep 2
done < "$filename"

#curl -Ls -o /dev/null -w %{url_effective} http://is.gd/$1
