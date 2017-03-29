import urllib 
import json
while(True):
    url="http://python-data.dr-chuck.net/geojson?"
    place=raw_input("place:")
    if len(place) < 1 : break
    gm=urllib.urlopen(url+urllib.urlencode({'sensor':'false','address': place}))
    try: data=gm.read()
    except: print "Something is wrong"
    info=json.loads(data)
    if "status" not in info or info["status"]!="OK":
        print '==== Failure To Retrieve ===='
        break
    lat=info["results"][0]["place_id"]
    print lat