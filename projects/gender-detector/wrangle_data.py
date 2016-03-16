from os.path import exists, join
import requests
import csv
import json

DATA_DIR = 'tempdata'
W_FILENAME = join(DATA_DIR, 'wrangled_data.json')
SJ_DATA_FILENAME = join(DATA_DIR, 'wrangled_data.csv')
URL = 'http://transparentcalifornia.com/export/san-jose-2014.csv'
sj_data = list(csv.DictReader(open('tempdata/san-jose-2014.csv')))

wrangled_dict = {}

for person in sj_data:
    for_dict = {}
    for_dict['name'] = person['Employee Name']
    for_dict['base_pay'] = person['Base Pay']
    for_dict['ot_pay'] = person['Overtime Pay']
    for_dict['total_compensation'] = person['Total Pay & Benefits']
    wrangled_dict[for_dict['name']] = for_dict

if not exists(W_FILENAME):
    with open(W_FILENAME, 'w') as f:
      json.dump(wrangled_dict, f, indent=2)
    

resp = requests.get(URL)
with open(SJ_DATA_FILENAME, 'w') as f:
    f.write(resp.text)
    
#print('So, I wrote all this, made a beautiful json file, and found it as a lot easier to just use the original csv. I did not want to just delete it, so I left it here for you. Check out wrangled_data.json to see the other version')