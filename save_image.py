# Author: Li Ding
# Instagram Data Crawler, modified from Yiheng Zhou's
# Created: Jan. 2017
# Python 2


import json
import os
import urllib


def tag_based(tag):
	save_path = os.getcwd()+ "\\" + tag + '_image'
	if os.path.exists(save_path) is False:
		os.mkdir(save_path)
	file = []
	for line in open(tag, 'r'):
		file.append(json.loads(line))
	x=1
	for url in file:
		for img in url['posts']:
			temp= save_path + '\\%s.jpg' %img['media']['owner']['username']
			if os.path.exists(temp) is False:
				print( u'Downloading image No.%s' % x + ' for tag - ' + tag)
				try:
					image_data = urllib.urlopen(img['media']['display_src']).read()
					with open(temp, 'wb') as image_file:
						image_file.write(image_data)
					image_file.close()
				except:
					print( u"Fail in %s"%img['media']['display_src'])
			x+=1
	print( u'Complete downloading %d image(s) for tag %s'%(x, tag))


# Download images from a tag data
TAG = ["selfie"]

for i in TAG:
	tag_based(i)



