import sys
from collections import Counter
# import heapq,copy
from logging import getLogger, StreamHandler, DEBUG
# import pprint as pp
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
# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

N,M = MI() # N スイッチ M ランプ
G = list()
# ライトスイッチパターンリストを入れる
for x in range(M):
    G.append(LI())
Odd = LI()

# Gの各行先頭列を削除
for x in range(M):
    G[x].pop(0)
# logger.debug(G)

# Gの内容を0-indexへ
for x in range(M):
    for y in range(len(G[x])):
        G[x][y] = G[x][y]-1

# 全検索開始
logger.debug(G)
result = 0
for pat in range(2**N):
    patlst = list()
    for j in range(N):
        if (pat >> j) == 1:
            patlst.append("入")
        else:
            patlst.append("切")
    logger.debug(patlst)
    # logger.debug("{} -> {}".format(pat,bin(pat)))
    all_lamp_on=True
    for j in range(M):
        tso_list = list()
        for pos in range(len(G[j])):
            if ((pat>>G[j][pos]) & 1) == 1:
                tso_list.append("YES")
            else:
                tso_list.append("NO")
        x = Counter(tso_list)
        logger.debug("\tランプ {} のスイッチ状況は {}".format(j,tso_list))
        logger.debug("\t奇遇数: {} <-> 結果{}".format(Odd[j],x))
        if Odd[j] != (x["YES"]%2):
            logger.debug("\t\tランプ {} は 奇遇数が一致しないので付かない".format(j))
            all_lamp_on = False
        else:
            logger.debug("\t\tランプ {} は問題なく付く".format(j))
    if all_lamp_on == True:
        result = result + 1
print(result)
