zfile = open('tempdata/ssa-babynames-nationwide-2014.txt')

females = []
males = []

for line in zfile:
  name, sex, babies = line.strip().split(',')
  if sex == 'F':
    females.append(name)
    females.append(int(babies))
  else:
    males.append(name)
    males.append(int(babies))
    
print('Top baby girl names', '\n1.', females[0], females[1], '\n2.', females[2], females[3], '\n3.', females[4], females[5], '\n4.', females[6], females[7], '\n5.', females[8], females[9])

print('Top baby boy names', '\n1.', males[0], males[1], '\n2.', males[2], males[3], '\n3.', males[4], males[5], '\n4.', males[6], males[7], '\n5.', males[8], males[9])