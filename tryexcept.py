largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    try:
        num=int(num)
    except:
        if num == "done" :
            print "Invalid input"
            break    
    if largest is None:
            largest=num
            smallest=num
    elif largest<num:
            largest=num
    elif smallest>num:
            smallest=num



print "Maximum is", largest
print "Minimum is",smallest   