zfile = open('tempdata/ssa-babynames-nationwide-2014.txt')

m_babies = 0
f_babies = 0

for line in zfile:
  name, sex, babies = line.strip().split(',')
  if sex == 'M':
    m_babies+=int(babies)
  else:
    f_babies+=int(babies)
  
print('F:', f_babies, '\nM:', m_babies)