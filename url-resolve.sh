#!/bin/bash

filename="$1"
while read -r line
do
	curl -Ls -o /dev/null -w %{url_effective} http://is.gd/$line >> urls-resolved.txt
	echo -e "\n" >> urls-resolved.txt
	sleep 1
done < "$filename"

#curl -Ls -o /dev/null -w %{url_effective} http://is.gd/$1
