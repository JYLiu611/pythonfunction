import urllib
from bs4 import *

url=raw_input(":")

html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

tags=soup.find_all('a')

for tag in tags:
    print tag.get('href',None)