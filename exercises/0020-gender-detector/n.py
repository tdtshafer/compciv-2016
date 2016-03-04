from os.path import join
from zoofoo import detect_gender
          
males = [0,0]
females = [0,0]
NA = 0
test_names = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']

for name in test_names:
  result = detect_gender(name)
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