import sys
from fastglob import glob
from data import DIR_PATH

if sys.argv[1] == "r":
    a = glob(DIR_PATH, recursive=True)
else:
    a = glob(DIR_PATH, recursive=False)
l = list(a)
#print(len(l))
