import json

zfile = open('tempdata/googlemaps/stanford.json')
txt = zfile.read()
zfile.close()

mydict = json.loads(txt)

print(mydict['status'])