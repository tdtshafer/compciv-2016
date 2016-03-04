from os.path import join
import json
import csv
DATA_DIR = 'tempdata'

WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')

rfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(rfile))

for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])  

json_file = open(WRANGLED_JSON_FILENAME, 'w')
jsontext = json.dumps(datarows, indent=2)
json_file.write(jsontext)
json_file.close()

csvcharcnt = open(WRANGLED_DATA_FILENAME).read()
jsoncharcnt = open(WRANGLED_JSON_FILENAME).read()
print("CSV has", len(csvcharcnt), "characters")
print("JSON has", len(jsoncharcnt), "characters")
# let's calculate how many times bigger the character increase is
ratio = round(((len(jsoncharcnt) - len(csvcharcnt)) / len(csvcharcnt)), 1)
print("JSON requires", ratio, "times more text characters than CSV")