import json

zfile = open('tempdata/googlemaps/stanford.json')
txt = zfile.read()
zfile.close()

mydict = json.loads(txt)

if len(mydict['results'][0]['formatted_address'])==0:
  print('No results.')
elif len(mydict['results'][0]['formatted_address'])>=2:
  print(mydict['results'][0]['formatted_address'])
else:
  for x in range(len(mydict['results'][0]['formatted_address'])):
    print((mydict['results'][0]['formatted_address'][x]))
