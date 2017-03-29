import urllib 
import json
while(True):
    url="http://maps.googleapis.com/maps/api/geocode/json?"
    place=raw_input("place:")
    if len(place) < 1 : break
    gm=urllib.urlopen(url+urllib.urlencode({'sensor':'false','address': place}))
    try: data=gm.read()
    except: print "Something is wrong"
    info=json.loads(data)
    if "status" not in info or info["status"]!="OK":
        print '==== Failure To Retrieve ===='
        break
    lat=info["results"][0]["geometry"]["location"]["lat"]
    lng=info["results"][0]["geometry"]["location"]["lng"]
    formatted_address=info["results"][0]["formatted_address"]
    print formatted_address,"lat:",lat, "lng:",lng
    print json.dumps(info,indent=4)