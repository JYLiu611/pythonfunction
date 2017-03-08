import re
file=open("zhengze_sum.txt")
num=0
for line in file:
    _numberlist_=re.findall("[0-9]+",line)
    if (len(_numberlist_)>=1):
        for each in range(len(_numberlist_)):
            num=num+float(_numberlist_[each])
print num