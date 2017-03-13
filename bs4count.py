import urllib 
from bs4 import *
import re

url="http://python-data.dr-chuck.net/comments_344147.html"

html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

comments=soup.find_all('span')
count=0
num=0
for line in comments:
    num+=int(line.contents[0])
    count+=1
print "count",count                                                         
print "num",num    