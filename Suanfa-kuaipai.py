def kuaipai(a,left,right):
    basic=a[int(left)]
    i=int(left)
    j=int(right)-1
    while i!=j:
        while a[j]>=basic:
            print "a[%d]="%j,a[j],basic,j-1
            j=j-1 
        while a[i]<=basic and i!=int(right)-1:
            i=i+1
        changenum=a[i]
        a[i]=a[j]
        a[j]=changenum
    if i==j:
        changenum=a[i]
        a[i]=a[int(left)]
        a[int(left)]=changenum
    return a    
 
a=[]
num=raw_input()         
a=num.split()
kuaipai(a,0,len(a))
print a