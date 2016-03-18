from os.path import join
from nameparser import HumanName
import json
DATA_DIR = 'tempdata'
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
datarows = json.load(open(WRANGLED_JSON_FILENAME))

def detect_gender(name):
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 
              'females': None, 'total': 0 }
    for row in datarows:
      if row['name'].upper() == name.upper():
          result = row
          break
    return result
  
def extract_usable_name(name):
    temp = HumanName(name)
    if '.' in temp['first'] or len(temp['first']) == 1:
      if ' ' in temp['middle']:
        return temp['middle'].split()[0]
      elif '-' in temp['middle']:
        return temp['middle'].split('-')[0]
      else:
        return temp['middle']
    elif ' ' in temp['first']:
      return temp['first'].split()[0]
    elif '-' in temp['first']:
        return temp['first'].split('-')[0]
    else:
      return temp['first']
    