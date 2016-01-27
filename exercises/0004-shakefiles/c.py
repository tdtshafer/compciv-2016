import shutil
import requests
import os

zname = os.path.join('tempdata','matty.shakespeare.tar.gz')
shutil.unpack_archive(zname, extract_dir = 'tempdata')
