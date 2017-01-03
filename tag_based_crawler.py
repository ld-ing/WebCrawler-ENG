#Yiheng Zhou
#Created: June 5, 2016

import json
import requests
import urllib2, httplib
import sys
import os
from lxml import html
import time
import random


'''
#@copyright Yiheng Zhou
def Generator(username,password,client_id, client_secret,redirect_url):
	#url2 = "https://api.instagram.com/oauth/authorize/?client_id="+ str(client_id) +"&redirect_uri="+ str(redirect_url) +"&response_type=code"
	url = "https://www.instagram.com/accounts/login/?force_classic_login=&next=/oauth/authorize/%3Fclient_id%3D"+client_id+"%26redirect_uri%3D"+redirect_url.replace(':','%3A')+"%26response_type%3Dcode"
	#get the token first
	client = requests.session()
	client.get(url)
	csrftoken = client.cookies['csrftoken']
	hrd = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Length':'101',
	'Content-Type':'application/x-www-form-urlencoded',
	'Host':'www.instagram.com',
	'Origin':'https://www.instagram.com',
	'Referer':url,
	'Upgrade-Insecure-Requests':'1',
	#'Cookie':'fbm_124024574287414=base_domain=.instagram.com; mid=Vk81hwAEAAFZUxlMiEAN6ESvS7wc; ig_pr=1; ig_vw=1332; sessionid=IGSC41ecd552778a838fb5b97b432278be77ce6974738cde0373b5ad0a01593037dc%3AvxTtuHgMUayLGf5Bin025gY0IgDuRiFg%3A%7B%7D; fbsr_124024574287414=X_g7C7R56nze_vekPohK_Ag5EF781BIzapzpAb_-KMc.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUN6bjFkZFhSdkpLeC1uOHpPTnZub0owd3ZSalVXbVoyeExieXZtdHRJZWY0RzhmUmVHTXlRYUt3RUl2a1lWRVcwaTdsY1NoRDkzOElZQ0FYaWZIZmJXT3FaLV9nNVpfeFRnUXhNaWliY1FYQUpUV3RKY2RrRE52ci1GVUYzM0NCRDNqNzJ3aWdlcE56eGNqcnd4MlNhaEhEQjlCd0NNN0lQQUF6aHN6VmQ0cV9ZMlFNeWNhOU1NOWR3VzNWRXRNRGJSTFVHWDRlTXN2WGZIb1dWcDYwNG5iVlV4QlB1WmZwTnRSRE9JRE1pVDRnU09xU2RoVUtsU0EtcjdqaWFGemlINWtPMUNHTmE0ZVVId1JBTk5vbXI5emFpazRhWjJENHdQTF9NaFd1MVF6eW5jWGNNejBVYzZKSlhfcktKeF9CYVU4NnFSOHFrZE9rTVp5SDM5dThmOSIsImlzc3VlZF9hdCI6MTQ1MjIzODY5NSwidXNlcl9pZCI6IjEwMDAwMzY5MTk5NzI0OSJ9; s_network=; csrftoken='+str(csrftoken),
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
	}
	payload = {'username':username, 'password':password,'csrfmiddlewaretoken':str(csrftoken)}
	print 'Logging in the account...'
	response = client.post(url,data=payload,headers=hrd)
	print response
'''


def login(username,password):
	###### STEP 1 #######
	
	#log into Instagram
	
	url = "https://www.instagram.com/accounts/login/ajax/"
	client = requests.session()
	client.get(url)
	csrftoken = client.cookies['csrftoken']
	hrd = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Length':'101',
	'Content-Type':'application/x-www-form-urlencoded',
	'Host':'www.instagram.com',
	'Origin':'https://www.instagram.com',
	'Referer':url,
	'Upgrade-Insecure-Requests':'1',
	#'Cookie':'fbm_124024574287414=base_domain=.instagram.com; mid=Vk81hwAEAAFZUxlMiEAN6ESvS7wc; ig_pr=1; ig_vw=1332; sessionid=IGSC41ecd552778a838fb5b97b432278be77ce6974738cde0373b5ad0a01593037dc%3AvxTtuHgMUayLGf5Bin025gY0IgDuRiFg%3A%7B%7D; fbsr_124024574287414=X_g7C7R56nze_vekPohK_Ag5EF781BIzapzpAb_-KMc.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUN6bjFkZFhSdkpLeC1uOHpPTnZub0owd3ZSalVXbVoyeExieXZtdHRJZWY0RzhmUmVHTXlRYUt3RUl2a1lWRVcwaTdsY1NoRDkzOElZQ0FYaWZIZmJXT3FaLV9nNVpfeFRnUXhNaWliY1FYQUpUV3RKY2RrRE52ci1GVUYzM0NCRDNqNzJ3aWdlcE56eGNqcnd4MlNhaEhEQjlCd0NNN0lQQUF6aHN6VmQ0cV9ZMlFNeWNhOU1NOWR3VzNWRXRNRGJSTFVHWDRlTXN2WGZIb1dWcDYwNG5iVlV4QlB1WmZwTnRSRE9JRE1pVDRnU09xU2RoVUtsU0EtcjdqaWFGemlINWtPMUNHTmE0ZVVId1JBTk5vbXI5emFpazRhWjJENHdQTF9NaFd1MVF6eW5jWGNNejBVYzZKSlhfcktKeF9CYVU4NnFSOHFrZE9rTVp5SDM5dThmOSIsImlzc3VlZF9hdCI6MTQ1MjIzODY5NSwidXNlcl9pZCI6IjEwMDAwMzY5MTk5NzI0OSJ9; s_network=; csrftoken='+str(csrftoken),
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
	}
	payload = {'username':username, 'password':password,'csrfmiddlewaretoken':str(csrftoken)}
	print 'Logging in the account...'
	response = client.post(url,data=payload,headers=hrd)
	return client

def tag_search(tag,level): #username,password,tag):
	client = login(uname,pwd)
	#fetch query results
	url2 = "https://www.instagram.com/explore/tags/"
	url2 = url2+tag+"/"
	query = client.get(url2)
	content = query.content
	tree = html.fromstring(content)
	posts = tree.xpath('//script[@type="text/javascript"]/text()')
	
	media1 = posts[3] #Returns json of all posts from the query
	media1 = media1[21:-1]
	temp = json.loads(media1)
	media = temp['entry_data']['TagPage'][0]['tag']['media']

	while(media['page_info']['has_next_page']):
		if level == 0:
			break
		level = level - 1
		url_page = "https://www.instagram.com/query/"
		client.get(url_page)
		hrd_page = {
			#':authority':'www.instagram.com',
			#':method':'POST',
			#':path':'/query/',
			#':scheme':'https',
			'accept':'application/json, text/javascript, */*; q=0.01',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
			'content-length':'489',
			'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
			'host':'www.instagram.com',
			'origin':'https://www.instagram.com/',
			'referer':'https://www.instagram.com/explore/tags/'+tag+'/',
			#'Cookie':'fbm_124024574287414=base_domain=.instagram.com; mid=Vk81hwAEAAFZUxlMiEAN6ESvS7wc; ig_pr=1; ig_vw=1332; sessionid=IGSC41ecd552778a838fb5b97b432278be77ce6974738cde0373b5ad0a01593037dc%3AvxTtuHgMUayLGf5Bin025gY0IgDuRiFg%3A%7B%7D; fbsr_124024574287414=X_g7C7R56nze_vekPohK_Ag5EF781BIzapzpAb_-KMc.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUN6bjFkZFhSdkpLeC1uOHpPTnZub0owd3ZSalVXbVoyeExieXZtdHRJZWY0RzhmUmVHTXlRYUt3RUl2a1lWRVcwaTdsY1NoRDkzOElZQ0FYaWZIZmJXT3FaLV9nNVpfeFRnUXhNaWliY1FYQUpUV3RKY2RrRE52ci1GVUYzM0NCRDNqNzJ3aWdlcE56eGNqcnd4MlNhaEhEQjlCd0NNN0lQQUF6aHN6VmQ0cV9ZMlFNeWNhOU1NOWR3VzNWRXRNRGJSTFVHWDRlTXN2WGZIb1dWcDYwNG5iVlV4QlB1WmZwTnRSRE9JRE1pVDRnU09xU2RoVUtsU0EtcjdqaWFGemlINWtPMUNHTmE0ZVVId1JBTk5vbXI5emFpazRhWjJENHdQTF9NaFd1MVF6eW5jWGNNejBVYzZKSlhfcktKeF9CYVU4NnFSOHFrZE9rTVp5SDM5dThmOSIsImlzc3VlZF9hdCI6MTQ1MjIzODY5NSwidXNlcl9pZCI6IjEwMDAwMzY5MTk5NzI0OSJ9; s_network=; csrftoken='+str(csrftoken),
			'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
			'x-csrftoken':client.cookies['csrftoken'],
			'x-instagram-ajax':'1',
			'x-requested-with':'XMLHttpRequest'
		}
		#payload_page = {'p':'ig_user('+user_info['id']+')+%7B+media.after('+media['page_info']['end_cursor']+'%2C+12)+%7B%0A++count%2C%0A++nodes+%7B%0A++++caption%2C%0A++++code%2C%0A++++comments+%7B%0A++++++count%0A++++%7D%2C%0A++++date%2C%0A++++dimensions+%7B%0A++++++height%2C%0A++++++width%0A++++%7D%2C%0A++++display_src%2C%0A++++id%2C%0A++++is_video%2C%0A++++likes+%7B%0A++++++count%0A++++%7D%2C%0A++++owner+%7B%0A++++++id%0A++++%7D%2C%0A++++thumbnail_src%2C%0A++++video_views%0A++%7D%2C%0A++page_info%0A%7D%0A+%7D','ref':'users%3A%3Ashow'}
		#payload_page = {'p':'ig_user('+user_info['id']+'){media.after('+media['page_info']['end_cursor']+',12){count,nodes{caption,code,comments{count},date,dimensions{height,width},display_src,id,is_video,likes{count},owner{id},thumbnail_src,video_views},page_info}}', 'ref':'users::show','csrfmiddlewaretoken':client.cookies['csrftoken']}
		payload_page='q=ig_hashtag('+tag+')+%7B+media.after('+media['page_info']['end_cursor']+'%2C+7)+%7B%0A++count%2C%0A++nodes+%7B%0A++++caption%2C%0A++++code%2C%0A++++comments+%7B%0A++++++count%0A++++%7D%2C%0A++++date%2C%0A++++dimensions+%7B%0A++++++height%2C%0A++++++width%0A++++%7D%2C%0A++++display_src%2C%0A++++id%2C%0A++++is_video%2C%0A++++likes+%7B%0A++++++count%0A++++%7D%2C%0A++++owner+%7B%0A++++++id%0A++++%7D%2C%0A++++thumbnail_src%2C%0A++++video_views%0A++%7D%2C%0A++page_info%0A%7D%0A+%7D&ref=tags%3A%3Ashow'
		response = client.post(url_page,data=payload_page,headers=hrd_page)
		content = json.loads(response.content)
#		print content
		media['nodes'] = media['nodes'] + content['media']['nodes']
		media['page_info'] = content['media']['page_info']
		media['posts'] = list()
	if True:
		for post in media['nodes']:
			url3 = "https://www.instagram.com/p/"+post['code']+"/?tagged="+tag+"&__a=1"
			query = client.get(url3)
			content = json.loads(query.content)
			media['posts'].append(content)
		media.pop("nodes",None)
	media.pop('page_info',None)	

	#print temp
	return media


def decode_json_file(file): #With JSON file
	with open(file) as dF:    
		data = json.load(dF)
	
	entry_data = data["entry_data"]
	TP = entry_data["TagPage"]
	TP = TP[0]
	
	tag = TP["tag"]
	m_info = tag["media"]
	
	#Branch 1
	p_info = m_info["page_info"] #Returns page info INCLUDING ENDPOINT
	#print p_info["end_cursor"]
	
	#Branch 2
	nodes = m_info["nodes"]
	
	return {"page_info": p_info, "media_nodes":nodes}

def decode_json(file): #For use in code
	#with open(file) as dF:    
	#	data = json.load(dF)
	
	entry_data = file["entry_data"]
	TP = entry_data["TagPage"]
	TP = TP[0]
	
	tag = TP["tag"]
	m_info = tag["media"]
	
	#Branch 1
	p_info = m_info["page_info"] #Returns page info INCLUDING ENDPOINT
	#print p_info["end_cursor"]
	
	#Branch 2
	nodes = m_info["nodes"]
	
	return {"page_info": p_info, "media_nodes":nodes}
	
	
def get_next(pj):
	pinf = pj["page_info"]
	if (pinf["has_next_page"] == True):
		return pinf["end_cursor"]
	else:
		print "\nFinished gathering posts."
		return "done"

'''
def load_all(pj)
	next = get_next(pj)
	url4 = "https://www.instagram.com/explore/tags/"+TAG+"/?max_id="+next
	client = login
	while(next!="done"):
'''

def get_media_codes(pj):
	nodes = pj["media_nodes"]
	
	codes = []
	
	for i in nodes:
		code = i["code"]
		codes.append(code)
	return codes

	
def get_media_info(pj):
	client = login(uname,pwd) #log into Instagram

	url3 = "https://www.instagram.com/p/"
	nodes = pj["media_nodes"]
	
	lict = []
	
	for i in nodes:
		code = i["code"]
		temp = url3 + code + "/?tagged="+ TAG
		#print temp
		query2 = client.get(temp)
		'''
		tree = html.fromstring(query2.content)
		posts = tree.xpath('//script[@type="text/javascript"]/text()')
		obs = posts[3]
		ocs = obs[21:-1]
		temp = json.loads(ocs)
		'''
		lict.append(query2.content)

		#temp = json.loads(query2.content)
		#t1 = decode_json(temp)
		#lict.append(t1)
	
	return lict


	'''
	code = "BGQmowyxKmd"
	url3 = "https://www.instagram.com/p/"
	url3 = url3 + code + "/?tagged="+ tag
	query2 = client.get(url3)
	print query2.content
	'''

def push_text(data,storage):
	file = open(storage,"w")
	file.write(str(data))
	file.close()

uname = 'zephyr_d'
pwd = 'dsadsahk7'
#st = "query_result.txt"

#TAG = "dank"
TAG = ["selfie", "life", 'love', 'fun', 'girl', 'boy', 'friends', 'summer', 'followme', 'happy', 'beautiful','photooftheday','instadaily','instalike','like4like','follow','beach','photo','cool','baby','me','pretty','portrait','guys','dude','goodday','tired','sleepyhead','earlybird','morning']
save_path = os.getcwd()+ "\\" + "tag_based" + "\\"
if os.path.exists(save_path) is False:
    os.mkdir(save_path)


#file = "data.json"
for i in range(10):
	for i in TAG:
		one = tag_search(i,5)
		time.sleep(int(random.random() * 5))
		temp= save_path + i
		with open(temp,'a+') as output:
			json.dump(one,output)
			output.write('\n')
	time.sleep(int(random.random() * 60))
#two = push_text(one,st)
#three = decode_json(one)
#print three
#four = get_media_info(three)
#print three["entry_data"]


