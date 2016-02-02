import string

zfile = open('tempdata/ssa-babynames-nationwide-2014.txt')

mydict = {}
for line in zfile:
    name, sex, babies = line.strip().split(',')
    last = name[-1]
    if mydict.get(last):
        mydict[last] += int(babies)
    else:
        mydict[last] = int(babies)
for letter in string.ascii_lowercase:
  print(letter,': ', mydict[letter], sep='')