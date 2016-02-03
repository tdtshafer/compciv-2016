import json

zfile = open('tempdata/mapzen/stanford.json')
txt = zfile.read()
zfile.close()

mydict = json.loads(txt)

print('type:', mydict['type'])
print('text:', mydict['geocoding']['query']['text'])
print('size:', mydict['geocoding']['query']['size'])
print('boundary.country:', mydict['geocoding']['query']['boundary.country'])