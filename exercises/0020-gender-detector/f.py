from os.path import join, basename
from glob import glob

START_YEAR = 1950
END_YEAR = 2015

for year in range(START_YEAR, END_YEAR, 5):
    DATA_DIR = 'tempdata'
    thefilename = join(DATA_DIR, 'yob' + str(year) + '.txt')

    totalsdict_count = {'M':0, 'F':0, 'T':0}
    totalsdict_names = {'M': set(), 'F': set(), 'T': set()}

    thefile =  open(thefilename, 'r')


    for line in thefile:
        name, gender, babies = line.split(',')
        totalsdict_names[gender].add(name)
        totalsdict_count[gender]+= int(babies)
        totalsdict_names['T'].add(name)
        totalsdict_count['T']+= int(babies)
        
    t = round(totalsdict_count['T']/len(totalsdict_names['T']))
    m = round(totalsdict_count['M']/len(totalsdict_names['M']))
    f = round(totalsdict_count['F']/len(totalsdict_names['F']))
    
    print(year)
    print('Total: %d babies per name'% t)
    print('Total: %d babies per name'% m)
    print('Total: %d babies per name'% f)