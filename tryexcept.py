hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate per Hours:")
try:
    h = float(hrs)
    rate = float(rate)
    if h>=40:
        m=40*rate+(h-40)*1.5*rate
    else:
        m=h*rate
    print m
except:
    print"Something wrong happened."