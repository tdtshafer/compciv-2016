import os
import requests
  
if not os.path.exists('tempdata/mapzen'):
  os.makedirs('tempdata/mapzen')
  
if not os.path.exists('tempdata/googlemaps'):
  os.makedirs('tempdata/googlemaps')

urlz = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'

urlx = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'

respz = requests.get(urlz)
respx = requests.get(urlx)
  
zname = os.path.join('tempdata', 'googlemaps', 'stanford.json')
zfile = open(zname, 'wb')
zfile.write(respz.content)
zfile.close()

xname = os.path.join('tempdata', 'mapzen', 'stanford.json')
xfile = open(xname, 'wb')
xfile.write(respx.content)
xfile.close()

print('Downloading from:', urlz)
print('Writing to:', zname)
print('Wrote', len(respz.text.splitlines()), 'lines and', len(respz.text), 'characters')
print('Downloading from:', urlx)
print('Writing to:', xname)
print('Wrote ', len(respx.text.splitlines()), 'lines and', len(respx.text), 'characters')