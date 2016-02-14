zfile = open('tempdata/ssa-babynames-nationwide-2014.txt')

unordered = []
for line in zfile:
  name, sex, babies = line.strip().split(',')
  unordered.append([name, sex, int(babies)])
    
ordered = sorted(unordered, key = lambda name: name[2], reverse=True)
  
for x in range(10):
  print(x+1, '. ', ordered[x][0], ',', ordered[x][1], ',', ordered[x][2], sep='')
  
