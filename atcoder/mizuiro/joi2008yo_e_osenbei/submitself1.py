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

maxok = -1
for bit in range(0,2**H):
    nowok = 0
#    print("----- bit = {} START -----".format(bit))
    G = copy.deepcopy(Gorg)
    turnList = list()
    for shift in range(0,H):
        if( ((bit >> shift) & 1) == 1):
            turnList.append(shift)
#    xdebug("bit = {} -> turnList={}".format(bit,turnList))
    h_pos_len = len(turnList)
    # print("bit = {} の時→ひっくり返す行の数 {}".format(bit,h_pos_len))
    for h in range(0,h_pos_len):
        h2 = turnList[h]
        # print("{} 行目をひっくり返します".format(h2))
        for w in range(0,W):
            G[h2][w] = (G[h2][w]+1)%2
#    print("bit = {}の時のせんべい焼き器は".format(bit))
#    pp.pprint(G)
#    xdebug("bit {} の時の行のひっくり返し終了")
#    xdebug("列を個々に見ていく")
    for w in range(W):
        one = 0
        zero = 0
        for h in range(H):
            if G[h][w] == 1:
                one = one + 1
            else:
                zero = zero + 1
        if one < zero:
            nowok = nowok+zero
        else:
            nowok = nowok + one
#    print("bit = {} の最終結果枚数は {}".format(bit,nowok))
#    pp.pprint(G)
    if maxok < nowok:
        maxok = nowok
#    print("----- bit = {} END -----".format(bit))
print(maxok)
