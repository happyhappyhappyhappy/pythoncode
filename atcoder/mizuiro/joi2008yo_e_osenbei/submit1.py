import sys
# from collections import defaultdict
# import heapq,copy
import copy
from logging import getLogger, StreamHandler, DEBUG
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
xdebug=logger.debug

H,W = MI()
Gorg = list()
for x in range(0,H):
    Gorg.append(LI())

for bit in range(1,2**H):
    G = copy.copy(Gorg)
    turnList = list()
    for shift in range(0,H):
        if( ((bit >> shift) & 1) == 1):
            turnList.append(shift)
    xdebug("bit = {} -> turnList={}".format(bit,turnList))
    # TODO: turnListができあがったのでこれに設置した値でひっくり返します
