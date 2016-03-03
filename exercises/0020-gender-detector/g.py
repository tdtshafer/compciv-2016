from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
YEAR = 2014
thefilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')

WRANGLED_HEADERS = ['year', 'name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')

namesdict = {}
with open(thefilename, 'r') as thefile:
    for line in thefile:
        name, gender, count = line.split(',')
        if not namesdict.get(name): # need to initialize a new dict for the name
            namesdict[name] = {'M': 0, 'F': 0}
        namesdict[name][gender] += int(count)

my_awesome_list = []

for name, counts in namesdict.items():
    xdict = {}
    xdict['year'] = YEAR # i.e. 2014
    xdict['name'] = name
    xdict['females'] = counts['F']
    xdict['males'] = counts['M']
    xdict['total'] = xdict['males'] + xdict['females']
    # the "likely" gender is determined by comparing females vs males numbers
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])

    # finally, add our new dict, xdict, to my_awesome_list
    my_awesome_list.append(xdict)

    
# let's create the new file to write to
wfile = open(WRANGLED_DATA_FILENAME, 'w')
# turn it into a DictWriter object, and tell it what the fieldnames are
wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
# write the headers row
wcsv.writeheader()
    
def sort_things(xdict):
    # and return a tuple of negative total, and normal name
    return (-xdict['total'], xdict['name'])

my_final_list = sorted(my_awesome_list, key=sort_things)
for row in my_final_list:
    wcsv.writerow(row)
# the end...close the file
wfile.close()

result_file = open(WRANGLED_DATA_FILENAME, 'r')
theextrastep = result_file.readlines()[0:5]
for line in theextrastep:
    print(line.strip())

    

