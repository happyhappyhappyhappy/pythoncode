from itertools import product
import sys
import pprint

xprint=pprint.pprint
R,C = map(int,sys.stdin.readline().split())
xprint("{}-{}".format(R,C))
lines = list()
for r in range(0,R):
    line1 = list(map(int,sys.stdin.readline().split()))
    lines.append(line1)
xprint(lines)
lines = zip(*lines)
# xprint(lines)
# for l in lines:
#     xprint(l)
ans = 0
for p in product([0,1],repeat=R):
    sm = 0
    for line1 in lines:
        cnt = 0
        
