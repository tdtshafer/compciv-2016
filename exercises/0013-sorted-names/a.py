import os
import requests
  
if not os.path.exists('tempdata'):
  os.makedirs('tempdata')

zurl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
  
resp = requests.get(zurl)

zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()

mytxt = resp.text

length = len(mytxt)

print("There are", length, "characters in", zname)