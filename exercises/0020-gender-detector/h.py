from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')


rfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(rfile))

for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])

print("Most popular names with <= 60% gender skew:")
bigdatarows = sorted(datarows, key=lambda r: r['total'], reverse=True)
fxrows = [r for r in datarows if r['ratio'] <= 60 ]

for row in fxrows[0:5]:
    print(row['name'].ljust(10), row['gender'], row['ratio'], row['total'])