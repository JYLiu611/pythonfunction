import xml.etree.ElementTree as ET
import urllib
xml=" http://python-data.dr-chuck.net/comments_344144.xml"
data=urllib.urlopen(xml).read()

tree=ET.fromstring(data)

print "Retrieving:",xml
print "Retrieved %d characters"%len(data)

stuff=tree.findall('comments/comment')
sum=0
count=0
for item in stuff:
    sum+=int(item.find('count').text)
    count+=1
print "Count:",count 
print "Sum:",sum
# sum1=0
# count1=0
# stuff2=tree.findall('.//count')
# for item in stuff2:
    # sum1+=int(item.text)
    # count1+=1
# print "Count:",count1 
# print "Sum:",sum1  