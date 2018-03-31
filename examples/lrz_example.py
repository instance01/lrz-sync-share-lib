from os import listdir
from os.path import isfile, join
from lrz_sync_share import lrz_session
from config import CREDS


BOOKS_DIR = "/home/instance/books/fiction/"


lrz = lrz_session(CREDS["username"], CREDS["password"], CREDS["shibboleth"])
lrz.login()

for filename in listdir(BOOKS_DIR):
    full_filename = join(BOOKS_DIR, filename)
    if isfile(full_filename):
        lrz.upload("books/fiction", full_filename)
        print(lrz.get_link("books/fiction", filename))
