#!/bin/bash

sed -e 's/ /\n/g' $1 | sed -e 's/^\n//g' | sed 's/^[^[:alpha:]]\+//' | sed 's/[^[:alpha:]]\+$//' | awk '{
    if (NF!=0){
	print tolower($0) | "sort -u"
    }}'
