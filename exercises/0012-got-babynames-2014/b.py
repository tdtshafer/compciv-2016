zfile = open('tempdata/ssa-babynames-nationwide-2014.txt')

total_babies = 0

for line in zfile:
  name, sex, babies = line.strip().split(',')
  total_babies += int(babies)
print('There are', total_babies, 'babies whose names were recorded in 2014.')