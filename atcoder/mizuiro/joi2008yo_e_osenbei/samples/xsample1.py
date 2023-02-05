import os
import sys
import pprint
from itertools import product
xprint=pprint.pprint
R,C = map(int,sys.stdin.readline().split(" "))
print("R={} C={}".format(R,C))
lines = []
for r in range(0,R):
    line = list(map(int,sys.stdin.readline().split(" ")))
    lines.append(line)
xprint(lines)
lines = list(zip(*lines))
