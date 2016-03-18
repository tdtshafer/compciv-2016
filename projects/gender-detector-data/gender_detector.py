
from os.path import exists, join
from tempdata.zoofoo import detect_gender
from nameparser import HumanName
import csv
import requests
DATA_DIR = 'tempdata'
SJ_DATA_URL = 'http://transparentcalifornia.com/export/san-jose-2014.csv'
SJ_DATA_FILENAME = join(DATA_DIR, 'san-jose-2014.csv')

if not exists(SJ_DATA_FILENAME):
    print("Downloading", SJ_DATA_URL)
    resp = requests.get(SJ_DATA_URL)
    with open(SJ_DATA_FILENAME, 'w') as f:
        f.write(resp.text)
sj_data = list(csv.DictReader(open(SJ_DATA_FILENAME)))


m=0
f=0
na=0
failed_names = []

for person in sj_data:
    name = HumanName(person['Employee Name'])
    if '.' in name['first'] or len(name['first']) == 1:
      use_name = name['middle']
    else:
      use_name = name['first']
    result = detect_gender(use_name)
    
    #print (result['name'], ': ', result['gender'], sep='')
    if result['gender'] == 'M':
      m+=1
    elif result['gender'] == 'F':
      f+=1
    else:
      na+=1
      failed_names.append(result['name'])
      
extrap_m = round((na/len(sj_data))*m)
extrap_f = na-extrap_m

print('By my calcualtion, there were', m, 'males and', f, 'females working for the City of San Jose in 2014.')
print('If we apply the same ratio of male and female to the', na, 
      'names that were not associated with a gender in our database,')
print('there would be an additional', extrap_m,
      'males and', extrap_f, 'females, for a total of', m+extrap_m, 'males and', f+extrap_f, 'females')
print(failed_names)

      



