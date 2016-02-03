import json

zfile = open('tempdata/googlemaps/stanford.json')
txt = zfile.read()
zfile.close()

mydict = json.loads(txt)

print(mydict['results'][0]['formatted_address'], end=';')
print(mydict['results'][0]['geometry']['location']['lng'], end=';')
print(mydict['results'][0]['geometry']['location']['lat'])
