byTwo = 'Numbe'
bySeven = 'rwang'
byBoth = 'Numberwang!'

for x in range(1,31):
  if x % 2 == 0 and x % 7 == 0:
    print(byBoth)
  elif x % 2 == 0:
    print(byTwo)
  elif x % 7 == 0:
    print(bySeven)
  else:
    print(x)