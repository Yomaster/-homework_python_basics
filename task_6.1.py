import itertools
from sys import argv

a = argv[1]

for i in itertools.count(int(a)):
    if i <= 30:
        print(i)
    else:
        break
