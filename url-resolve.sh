#!/bin/bash

filename="$1"
while read -r line
do
	curl -sSL --ssl -o /dev/null -w %{url_effective} http://is.gd/$line >> urls-resolved.txt
	echo -e "\n" >> urls-resolved.txt
	sleep 2
done < "$filename"

#curl -Ls -o /dev/null -w %{url_effective} http://is.gd/$1
