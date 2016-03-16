from os.path import exists, join
from tempdata.zoofoo import detect_gender
from nameparser import HumanName
import csv
import requests
DATA_DIR = 'tempdata'
SJ_DATA_URL = 'http://transparentcalifornia.com/export/san-jose-2014.csv'
SJ_DATA_FILENAME = join(DATA_DIR, 'san-jose-2014.csv')

if not exists(SJ_DATA_FILENAME):
    print("Downloading", SJ_DATA_URL)
    resp = requests.get(SJ_DATA_URL)
    with open(SJ_DATA_FILENAME, 'w') as f:
        f.write(resp.text)
sj_data = list(csv.DictReader(open(SJ_DATA_FILENAME))) 