name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
names=list()
count=dict()
for line in handle:
    if line.startswith("From "):
        names.append(line.split()[1])
for name in names:
    count[name]=count.get(name,0)+1

ming=None
ci=None
for mingzi,cishu in count.items():
    if ming is None or cishu>ci:
#    if ming == None or cishu>ci:	
        ming=mingzi
        ci=cishu
print ming,ci    