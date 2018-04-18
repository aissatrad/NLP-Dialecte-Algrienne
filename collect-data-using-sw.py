# -*- coding: utf-8 -*-
import re
import  codecs
import requests
from init import *
from time import sleep
from random import randint
import re
from data import SW

count=0
def req_facebook(request):
    r = requests.get("https://graph.facebook.com/v2.12/" + request, {'access_token': app_token})
    return r
for id in data:
	req = id+"/feed?fields=comments.summary(true).limit(100){message,id},message&limit=100"
	fb=codecs.open("fb.csv", "a", "utf-8")
	results = req_facebook(req).json()
	if "data" in results:
		posts = results["data"]
	else:
		posts={}
	if "paging" in results and "next" in results["paging"]:
		hasNext=results["paging"]["next"]
	for i in range(len(posts)):
		posts=results["data"][i]
		if "message" in posts:
			msg = re.sub(r'[\s+,+]',' ', posts["message"])
			if len(msg.split()) in range(2, 50) and any(w in SW for w in msg.split()):
				id_msg = results["data"][i]["id"]
				fb.write(id_msg)
				fb.write(",")
				fb.write(msg)	
				fb.write("\n")
				count +=1
		cmts = results["data"][i]["comments"]["data"]
		for j in range(len(cmts)):
			if "message" in cmts[j]:
				msg =re.sub(r'[\s+,+]', ' ', cmts[j]["message"])
				if len(msg.split()) in range(2, 50) and any(w in SW for w in msg.split()):
					id_msg =cmts[j]["id"]
					fb.write(id_msg)
					fb.write(",")
					fb.write(msg)
					fb.write("\n")
					count +=1
	while True:
		sleep(randint(1,3))
		results = requests.get(hasNext).json()
		if "paging" in results and "next" in  results["paging"]:
			hasNext= results["paging"]["next"]
		else:
			print("done")
			break
		if "data" in results:
			posts = results["data"]
		else:
			posts = {}
		for i in range(len(posts)):
			posts=results["data"][i]
			if "message" in posts:
				msg = re.sub(r'[\s+,+]',' ', posts["message"])
				if len(msg.split()) in range(2, 50) and any(w in SW for w in msg.split()):
					id_msg = results["data"][i]["id"]
					fb.write(id_msg)
					fb.write(",")
					fb.write(msg)	
					fb.write("\n")
					count += 1
			cmts = results["data"][i]["comments"]["data"]
			for j in range(len(cmts)):
				if "message" in cmts[j]:
					msg =re.sub(r'[\s+,+]', ' ', cmts[j]["message"])
					if len(msg.split()) in range(2, 50) and  any(w in SW for w in msg.split()):
						id_msg =cmts[j]["id"]
						fb.write(id_msg)
						fb.write(",")
						fb.write(msg)
						fb.write("\n")
						count +=1
					


	print(count)
print("...........................", count)
