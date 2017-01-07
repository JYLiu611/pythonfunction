largest=None
number=0
for num in [9,41,12,3,74,15]:
    number=number+1
    if largest is None:
        largest=num
    elif largest<num:
        largest=num
print "the largest is",largest,";","\n","It`s number is",number