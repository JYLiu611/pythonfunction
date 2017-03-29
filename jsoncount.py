import json
import urllib
count=0
#url="http://python-data.dr-chuck.net/comments_42.json"
url=raw_input("Enter location:")
data=urllib.urlopen(url).read()
info=json.loads(data)
for item in range(len(info["comments"])):
    count+=info["comments"][item]["count"]
print count    