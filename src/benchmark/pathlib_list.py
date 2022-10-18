import sys
from pathlib import Path
from data import DIR_PATH

if sys.argv[1] == "r":
    a = list(Path(DIR_PATH).glob("**/*"))
else:
    a = list(Path(DIR_PATH).glob("**"))
l = list(a)
#print(len(l))
