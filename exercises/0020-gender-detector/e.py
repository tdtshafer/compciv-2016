from os.path import join, basename
from glob import glob

YEAR = 2014
DATA_DIR = 'tempdata'
thefilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')

totalsdict_count = {'M':0, 'F':0, 'T':0}
totalsdict_names = {'M': set(), 'F': set(), 'T': set()}

thefile =  open(thefilename, 'r')


for line in thefile:
    name, gender, babies = line.split(',')
    totalsdict_names[gender].add(name)
    totalsdict_count[gender]+= int(babies)
    totalsdict_names['T'].add(name)
    totalsdict_count['T']+= int(babies)


print('Total: %d names for %d babies'% (len(totalsdict_names['T']), totalsdict_count['T']))
print('    M: %d names for %d babies'% (len(totalsdict_names['M']),totalsdict_count['M']))
print('    F: %d names for %d babies'% (len(totalsdict_names['F']),totalsdict_count['F']))
