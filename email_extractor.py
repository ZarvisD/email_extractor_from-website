import requests
import re
chk=[]
fetched_url=[]
urls="http://www.dalailama.com/"
useful_urls=[]
r=requests.get(urls)
print r
result=re.findall(r'http[s]?://[\w\d./-]+',r.content)
for each_item in result:
	fetched_url.append(each_item)
for f in fetched_url:
	if urls in f:
		useful_urls.append(f)
	else:
		pass

for s in useful_urls:
	s1=requests.get(s)
	s2=s1.content
	s3=re.findall(r'[\w\d_.-]+@[\w\d_.-]+',s2)
	if not s3:
		pass
	else:
		print s3
