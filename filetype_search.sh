#!/bin/bash
FILE="sorted-urls-resolved-cleaned.txt"
#RESULT=`grep $line\$ $FILE | wc -l`
while IFS= read -r line; do
    RESULT=`grep $line\$ $FILE | wc -l`
    echo "$line: $RESULT"
done < $1
