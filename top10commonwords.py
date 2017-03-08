# -*- coding:utf-8 -*-  
fileopen=open("top10commonwords.txt")
count=dict()
for line in fileopen:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
lst=list()
for a,b in count.items():
    lst.append((b,a))
        
        
lst.sort(reverse=True)
for number,name in lst[:10]:
    print name,number