import os
fname = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
rajfile = open(fname)
total_lines = 4766
print_now = total_lines -5
for line_num in range(total_lines):
  line = rajfile.readline()
  if line_num >= print_now:
    the_line = str(line_num +1) + ': ' + line.strip()
    print(the_line)
    line_num+=1
  else:
    line_num+=1
rajfile.close()
