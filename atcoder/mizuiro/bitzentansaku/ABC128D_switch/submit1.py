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
logger.debug(G)

# Gの内容を0-indexへ
for x in range(M):
    for y in range(len(G[x])):
        G[x][y] = G[x][y]-1

# 全検索開始
logger.debug(G)
result = 0
for pat in range(2**N):
    # logger.debug("{} -> {}".format(pat,bin(pat)))
    all_lamp_on=True
    for j in range(M):
        tso_list = list()
        for pos in range(len(G[j])):
            total_switch_ok=0
            logger.debug("\tpat = {},checkpos ={}".format(pat,bin(pat>>G[j][pos])))
            if ((pat>>G[j][pos]) & 1) == 1:
                logger.debug("この時付く")
                total_switch_ok=total_switch_ok+1
                tso_list.append(True)
            else:
                tso_list.append(False)
        x = Counter(tso_list)
        logger.debug("\tランプ {} のスイッチ一致状況は {}".format(j,x))
        logger.debug("奇遇数: {}".format(Odd))
        if Odd[j] != (total_switch_ok%2):
            logger.debug("ランプ {} は 奇遇数が一致しないので付かない".format(j))
            all_lamp_on = False
        else:
            logger.debug("ランプ {} は問題なく付く".format(j))
    if all_lamp_on == True:
        result = result + 1
print(result)
