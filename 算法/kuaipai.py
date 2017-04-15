
# coding: utf-8

# In[20]:

def kuaipai(a,left,right):
    basic=a[left]
    i=left
    j=right-1
    if i>=j:
        return a
    while i!=j:
        while int(a[j])>=int(basic) and j>i:
            j=j-1
        a[i]=a[j]        
        while int(a[i])<=int(basic) and j>i:
            i=i+1
        a[j]=a[i]
    a[i]=basic
    kuaipai(a,left,i)
    kuaipai(a,i+1,right)
    return a
    
a=[]
num=raw_input()         
a=num.split()
kuaipai(a,0,len(a))
print a


# In[ ]:




# In[ ]:



