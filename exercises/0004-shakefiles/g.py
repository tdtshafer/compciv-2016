import glob
import os
tragic_path = os.path.join('tempdata','tragedies','*')
tragic_filenames = glob.glob(tragic_path)
for fname in tragic_filenames:
  txtfile = open(fname)
  total_lines = 0
  for line in txtfile:
    total_lines+=1
  txtfile.close()
  starting_line_num = total_lines - 5
  txtfile = open(fname)
  for line_num in range(total_lines):
    line = txtfile.readline()
    if line_num >= starting_line_num:
      the_line = str(line_num + 1) + ': ' + line.strip()
      print(the_line)
  txtfile.close()