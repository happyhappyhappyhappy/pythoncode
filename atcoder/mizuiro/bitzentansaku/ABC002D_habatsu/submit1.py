import sys
# from collections import defaultdict
# import heapq,copy
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
pppp=pp.pprint
N,M = MI()
xdebug("N={} M={}".format(N,M))
G = [ [False] * N for _ in range(N)]
# pppp(G)
for _ in range(M):
    x,y = MI()
    x = x-1
    y = y-1
    # xdebug("x={},y={}".format(x,y))
    G[x][y]=True
    G[y][x]=True
for x in range(N):
    G[x-1][x-1]=True # 自分自身に対しては一応True
#pppp(G)
# bit全探索
for bit_p in range(1,1<<N):
    chainList=list()
    for j in range(N):
        if ((bit_p>>j) & 1) == 1:
            chainList.append(j)
    # TODO: この情報からチェーンを確認する
    xdebug("{} の時の 派閥リスト: {}".format(bit_p,chainList))
