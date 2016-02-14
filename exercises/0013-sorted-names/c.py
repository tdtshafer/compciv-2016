from os.path import join
import operator

DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')

unordered = []
namesdict = {}

with open(FPATH) as f:
  for line in f:
    name, sex, babies = line.strip().split(',')
    if namesdict.get(name):
      namesdict[name] += int(babies)
    else:
      namesdict[name] = int(babies)

  for name in namesdict:
    if namesdict[name] >=2000:
      unordered.append([name, namesdict[name], len(name)])
    
ordered = sorted(unordered, key=operator.itemgetter(2, 1), reverse=True)

for x in range(10):
  print(ordered[x][0].ljust(11), str(ordered[x][1]).rjust(13), sep='')
