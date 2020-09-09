import itertools
from sys import argv

a = argv[1]

for i, element in enumerate(itertools.cycle(list(a)), 1):
    if i <= len(list(a)) * 2:
        print(element)
    else:
        break
