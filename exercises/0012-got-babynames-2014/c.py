zfile = open('tempdata/ssa-babynames-nationwide-2014.txt')

daenerys_babies = 0
khaleesi_babies = 0

for line in zfile:
  name, sex, babies = line.strip().split(',')
  if sex == 'F':
    if 'Daenerys' in name:
      daenerys_babies+=int(babies)
    elif 'Khalees' in name:
      khaleesi_babies+=int(babies)
    elif 'Khaless' in name:
      khaleesi_babies+=int(babies)
print('Daenerys:', daenerys_babies)
print('Khaleesi:', khaleesi_babies)