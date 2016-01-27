import os
fname = os.path.join('tempdata','tragedies','hamlet')
hamletfile = open(fname)
line_num = 0
for line in hamletfile:
  line_num+=1
hamletfile.close()
print(fname, 'has', line_num, 'lines.')