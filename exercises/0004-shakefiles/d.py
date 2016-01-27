import os
fname = os.path.join('tempdata','tragedies','hamlet')
hamletfile = open(fname)

for line in range(5):
  print(hamletfile.readline().strip())
hamletfile.close()