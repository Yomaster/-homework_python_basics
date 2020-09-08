import itertools
from sys import argv

a = argv[1]

for i in itertools.count(int(a)):
    print(i if i <= 30 else exit())
