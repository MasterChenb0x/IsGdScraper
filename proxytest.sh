#!/bin/bash

# List of User Agents
useragent[1]="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
useragent[2]="Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12 Version/12.16"
useragent[3]="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
useragent[4]="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"
useragent[5]="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
useragent[6]="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
useragent[7]="Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
useragent[8]="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
useragent[9]="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
useragent[10]="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"

NUM=$[ ( $RANDOM % 10 ) + 1 ]
UAGENT=${useragent[$NUM]}
 
file="proxylist.txt"
#while read line
#do
export https_proxy=$1
export http_proxy=$1
wget -U "$UAGENT" https://chenb0x.net/asterisk-the-busy-box -O /dev/null -t 1 -T 2 --max-redirect 0 --https-only
sleep 1
#done < "$file"

#wget https://chenb0x.net/asterisk-the-busy-box -O /dev/null -t 1 -T 4 -q
