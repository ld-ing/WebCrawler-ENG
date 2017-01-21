# WebCrawler-ENG
WebCrawler for Instagram, Python 2.

--------------------
## Info
Author: Li Ding  
Instagram Data Crawler, modified from Yiheng Zhou's  
Created: Jan. 2017  
Python 2  

--------------------
## Usage
1. Use tag_based_crawler.py to store the data of posts under a list of tags. It will create a json file for each tag.
2. Use save_image.py to download images with a json created by 1. It shall be in the same directory as the json file.
3. A simple bash file will be helpful for both programs to avoid network error, which looks like :
```
#!/bin/bash
for i in $(seq 1 10000)
do
	python tag_based_crawler.py
done
```
