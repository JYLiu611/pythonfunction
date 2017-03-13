import urllib 
from bs4 import *
import re
#like : http://python-data.dr-chuck.net/known_by_Fikret.html
url=raw_input("Enter URL:")
count=raw_input("Enter count:")
position=raw_input("Enter position:")
try:
    for i in range(int(count)):
        html=urllib.urlopen(url).read()
        soup=BeautifulSoup(html)
    
        links=soup.find_all('a')
        print "Retrieving: ",url
        url=links[int(position)-1].get("href")
    print "Retrieving: ",url
except:
    print "Wrong "