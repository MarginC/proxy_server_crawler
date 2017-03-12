#!/bin/sh

l=`scrapy list`
for s in $l
do
	scrapy crawl $s
done
