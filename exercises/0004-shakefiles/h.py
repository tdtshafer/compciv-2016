from os.path import join
from glob import glob

all_line_count = 0
all_nonblank_line_count = 0

filepattern = join('tempdata', '**', '*')
filenames = glob(filepattern)

print (filenames)

for fname in filenames:
  total_line_count = 0
  nonblank_line_count = 0
  txtfile = open(fname, 'r')
  for line in txtfile:
    total_line_count+=1
    if line.strip() != '':
      nonblank_line_count+=1
  txtfile.close()
  print(fname, 'has', nonblank_line_count,
      'non-blank lines out of', total_line_count, 'total lines')
  all_nonblank_line_count+=nonblank_line_count
  all_line_count+=total_line_count
print('All together, Shakespeare\'s', 
      len(filenames), 'text files have:')
print(all_nonblank_line_count, 'non-blank lines out of', 
      all_line_count, 'total lines')

