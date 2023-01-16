import sys
# from collections import defaultdict
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
    for y in range(G[x]):
        G[x][y] = G[x][y]-1
# TODO: 次はここから
