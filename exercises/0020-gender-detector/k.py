from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')

rfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(rfile))

for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])  


def name_search (name):
      result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
      
      for row in datarows:
        if row['name'].upper() == name.upper():
            result = row
            break
      return result
         
males = [0,0]
females = [0,0]
NA = 0
test_names = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']

for name in test_names:
  result = name_search(name)
  if result['gender'] == 'M':
    males[0]+=1
    males[1]+=result['males']
    females[1]+=result['females']
  elif result['gender'] == 'F':
    females[0]+=1
    females[1]+=result['females']
    males[1]+=result['males']
  else:
    NA+=1
  print(name, result['gender'], result['ratio'])
    
print("Total:")
print("F:", females[0], 'M:', males[0], 'NA:', NA)
print('females:', females[1], 'males:', males[1])

