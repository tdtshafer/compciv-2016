import requests
from os import makedirs
PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)
alpha = ['a','b','c','d','e']
i = 0

URLS = [
        'http://images.nypl.org/index.php?id=5033986&t=w',  
        'http://images.nypl.org/index.php?id=G98F793_007&t=w', 
        'http://images.nypl.org/index.php?id=56207&t=w',
        'http://images.nypl.org/index.php?id=1248613&t=w',
        'http://images.nypl.org/index.php?id=1606205&t=w'
       ]

for url in URLS:
    print("Downloading", url)
    resp = requests.get(url)
    fname = 'pics/'+alpha[i]+'.jpg'
    print("Saving to", fname)
    with open(fname, 'wb') as w:
        w.write(resp.content)
    i+=1