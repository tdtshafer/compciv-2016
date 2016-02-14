import operator

zfile = open('tempdata/ssa-babynames-nationwide-2014.txt')

flist = []
mlist = []

for line in zfile:
  name, sex, babies = line.strip().split(',')
  if 'x' in name.lower():
    if sex == 'F':
      flist.append([name, sex, babies])
    elif sex == 'M':
      mlist.append([name, sex, babies])
flist = sorted(flist, key=operator.itemgetter(1), reverse=True)
mlist = sorted(mlist, key=operator.itemgetter(1), reverse=True)

print('Female')
for f in range(5):
  print(f+1, '. ', flist[f][0].ljust(11), str(flist[f][2]).rjust(11), sep='')

print('Male')
for m in range(5):
  print(m+1, '. ', mlist[m][0].ljust(11), str(mlist[m][2]).rjust(11), sep='')
   