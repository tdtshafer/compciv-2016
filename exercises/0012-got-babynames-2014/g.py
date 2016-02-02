import string

zfile = open('tempdata/ssa-babynames-nationwide-2014.txt')

mydict = {'M': {}, 'F': {}}
for line in zfile:
  name, sex, babies = line.strip().split(',')
  last = name[-1]
  if mydict[sex].get(last):
      mydict[sex][last] += int(babies)
  else:
      mydict[sex][last] = int(babies)
print('letter'.ljust(8), 'F'.rjust(8), 'M'.rjust(8), sep='')
print('-'*24)
for letter in string.ascii_lowercase:
  print(letter.ljust(8), str(mydict['F'][letter]).rjust(8), str(mydict['M'][letter]).rjust(8), sep='')