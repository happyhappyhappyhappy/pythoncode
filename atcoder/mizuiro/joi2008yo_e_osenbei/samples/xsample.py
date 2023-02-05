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
zlines = zip(*lines)
# xprint(lines)
# for l in lines:
#     xprint(l)
ans = 0
PR = product((0,1),repeat=R)
nowpat = 0
for bit in PR:
    xprint("-----現在 = {}-----".format(nowpat))

    for r in range(0,R):
        xprint("    ---r({})---".format(type(r)))
        xprint(r)
        xprint("    ---bit({})---".format(type(bit)))
        xprint(bit)
        xprint("    ---bit[r]({})---".format(type(bit[r])))
        xprint(bit[r])
    nowpat = nowpat + 1
countline = 0
for line in zlines:
    xprint("---nowline {}---".format(countline))
    for r in range(0,R):
        print("     ---r---")
        print(r)
        print("     ---line({})---".format(type(line)))
        print(line)
        print("     ---line[r]({})---".format(type(line[r])))
        print(line[r])
    countline = countline+1
# for p in product([0,1],repeat=R):
#     sm = 0
#     for line1 in lines:
#         cnt = 0
