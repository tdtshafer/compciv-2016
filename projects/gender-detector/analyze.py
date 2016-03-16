from os.path import exists, join
from operator import itemgetter
import requests
import csv
import json

DATA_DIR = 'tempdata'
W_FILENAME = join(DATA_DIR, 'classified_data.csv')
c_data = list(csv.DictReader(open(W_FILENAME)))    

#F1 CALCULATIONS 
m_comp = 0
f_comp = 0
na_comp = 0
m=0
f=0
na=0
m2=0
f2=0
na2=0

minimum = input('Input a minimum salary in dollars for the gender comparison:')

if not minimum.isdigit():
  print('\nTry again! Use a number this time.\n')


for person in c_data:  
  if person['gender'] == 'M':
    m+=1
    if round(float(person['compensation'])) > int(minimum):
      m2+=1
      m_comp+= round(float(person['compensation']))
  elif person['gender'] == 'F':
    f+=1
    if round(float(person['compensation'])) > int(minimum):
      f2+=1
      f_comp+= round(float(person['compensation']))
  else:
    na+=1
    if round(float(person['compensation'])) > int(minimum):
      na2+=1
      na_comp+= round(float(person['compensation']))
      
avg_m_salary = round(m_comp/m2)
avg_f_salary = round(f_comp/f2)
avg_na_salary = round(na_comp/na2)


print('\nSAN JOSE IN 2014: FACET ONE - SALARIES')
print('Average Male Salary: $', avg_m_salary, sep='')
print('Average Female Salary: $', avg_f_salary, sep='')
print('Average Uncategorized Salary: $', avg_na_salary, '\n', sep ='')

#F2 CALCULATIONS
unique_names = {'M': set(), 'F': set(), 'NA': set()}

for person in c_data:
  unique_names[person['gender']].add(person['name'])

print('SAN JOSE IN 2014: FACET TWO - UNIQUE NAMES')
print('Total Males:', m)
print('Unique Male Names:',len(unique_names['M']))
print('Total Females:', f)
print('Unique Female Names:',len(unique_names['F']))
print('Total Uncategorized:', na)
print('Unique Uncategorized Names:',len(unique_names['NA']), '\n')

#F3 CALCULATIONS

boys = unique_names['M']
girls = unique_names['F']
nas = unique_names['NA']

#list organized M, F, NA
total_length = [0,0,0]

mleading_name = ''
mties = []
fleading_name = ''
fties = []
naleading_name = ''
naties = []


for x in range(len(boys)):
  total_length[0] += len(list(boys)[x])
  if len(list(boys)[x]) > len(mleading_name):
    mties.clear()
    mleader = len(list(boys)[x])
    mleading_name = list(boys)[x]
    mties.append(list(boys)[x])
  elif len(list(boys)[x]) == len(mleading_name):
    mties.append(list(boys)[x])
    

for y in range(len(girls)):
  total_length[1] += len(list(girls)[y])
  if len(list(girls)[y]) > len(fleading_name):
    fties.clear()
    fleader = len(list(girls)[y])
    fleading_name = list(girls)[y]
    fties.append(list(girls)[y])
  elif len(list(girls)[y]) == len(fleading_name):
    fties.append(list(girls)[y])
    
  
for z in range(len(nas)):
  total_length[2] += len(list(nas)[z])
  if len(list(nas)[z]) > len(naleading_name):
    naties.clear()
    naleader = len(list(nas)[z])
    naleading_name = list(nas)[z]
    naties.append(list(nas)[z])
  elif len(list(nas)[z]) == len(naleading_name):
    naties.append(list(nas)[z])
    
  
print('SA JOSE IN 2014: FACET THREE - NAME LENGTH')
print('Average Male Name Length:', round(total_length[0]/len(boys), 2), 'letters')
print('Longest Male Name:', mleading_name)
print('Average Female Name Length:', round(total_length[1]/len(girls), 2), 'letters')
print('Longest Female Name:', fleading_name)
print('Average Uncategorized Name Length:', round(total_length[2]/len(nas), 2), 'letters')
print('Longest Uncategorized Name: ', naleading_name, ' (tied with ', naties[1], ')\n', sep='')






