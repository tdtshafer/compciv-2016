import json

zfile = open('tempdata/googlemaps/stanford.json')
txt = zfile.read()
zfile.close()

mydict = json.loads(txt)

for x in range(len(mydict['results'][0]['address_components'])):
  print((mydict['results'][0]['address_components'][x]['long_name']), end='; ')