
from os.path import exists, join
from gender import extract_usable_name, detect_gender
import csv


DATA_DIR = 'tempdata'
SJ_DATA_FILENAME = join(DATA_DIR, 'wrangled_data.csv')
C_FILENAME = join(DATA_DIR, 'classified_data.csv')
C_HEADERS = ['name', 'gender' , 'ratio' , 'females', 'males', 'total', 'compensation']

sj_data = list(csv.DictReader(open(SJ_DATA_FILENAME)))

classified_data = []

for person in sj_data:
    use_name = extract_usable_name(person['Employee Name'])
    result = detect_gender(use_name)
    result['compensation'] = float(person['Total Pay & Benefits'])
    classified_data.append(result)
    
    
wfile = open(C_FILENAME, 'w')
wcsv = csv.DictWriter(wfile, fieldnames=C_HEADERS)
wcsv.writeheader()

for row in classified_data:
   wcsv.writerow(row)
wfile.close()

