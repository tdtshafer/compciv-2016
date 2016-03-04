from os.path import join
import json
DATA_DIR = 'tempdata'
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
datarows = json.load(open(WRANGLED_JSON_FILENAME))

def detect_gender(name):
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in datarows:
      if row['name'].upper() == name.upper():
          result = row
          break
    return result