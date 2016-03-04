from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')


rfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(rfile))

bigdatarows = []
for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])  
    if r['total'] > 99:
        bigdatarows.append(r)

to_print = [0,0,0,0,0]
x=0

print("Popular names with a gender ratio bias of less than or equal to:")
for genderratio in (60, 70, 80, 90, 99):
  for r in bigdatarows:
    if r['ratio'] <= genderratio:
      to_print[x]+=1
  print('  ', genderratio, '%: ', to_print[x], '/', len(bigdatarows), sep='')
  x+=1
