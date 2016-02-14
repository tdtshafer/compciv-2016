from os.path import join
import numpy
import operator

DATADIR = 'tempdata'
FPATH = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')

unordered = []
namesdict = {}

totals = numpy.array([0,0,0,0,0,0])
  

with open(FPATH) as f:
  for line in f:
    name, sex, babies = line.strip().split(',')
    if namesdict.get(name):
      namesdict[name] += int(babies)
    else:
      namesdict[name] = int(babies)

  for name in namesdict:
    unordered.append([name, namesdict[name]])
    
ordered = sorted(unordered, key=operator.itemgetter(1), reverse=True)

top1 = 10
top2 = 100
top3 = 1000
top4 = 10000



for x in range(len(ordered)):
  current_babies = ordered[x][1]
  if x < top1:
    totals[0] += current_babies
    totals[5] += current_babies
  elif x < top2:
    totals[1] += current_babies
    totals[5] += current_babies
  elif x < top3:
    totals[2] += current_babies
    totals[5] += current_babies
  elif x < top4:
    totals[3] += current_babies
    totals[5] += current_babies
  else:
    totals[4] += current_babies
    totals[5] += current_babies

denom = totals[5]
    
percent =  totals/denom

print('Names ', 1, ' to ', top1, ': ', round(percent[0]*100, 1), sep='')
print('Names ', top1+1, ' to ', top2, ': ', round(percent[1]*100, 1), sep='')
print('Names ', top2+1, ' to ', top3, ': ', round(percent[2]*100, 1), sep='')
print('Names ', top3+1, ' to ', top4, ': ', round(percent[3]*100, 1), sep='')
print('Names ', 10001, ' to ', len(ordered), ': ', round(percent[4]*100, 1),sep='')
 

