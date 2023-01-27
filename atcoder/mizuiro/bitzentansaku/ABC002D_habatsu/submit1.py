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
# xdebug("N={} M={}".format(N,M))
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
# pppp(G)
# bit全探索

ans = 1
for bit_p in range(1,1<<N):
    chainList=list()
    for j in range(N):
        if ((bit_p>>j) & 1) == 1:
            chainList.append(j)
    # xdebug("派閥リスト: {}".format(chainList))
    is_ok=True
    if len(chainList) == 1:
        # xdebug("\t一人では派閥は作れません") # 一人で派閥は作れない -> 即時に次のループへ
        continue
    chainLen = len(chainList)
    for f in range(chainLen):
        for t in range(f+1,chainLen):
            f_pos = chainList[f]
            t_pos = chainList[t]
            if not ( G[f_pos][t_pos] or G[t_pos][f_pos] ):
                # xdebug("\t{} と {} が知り合いではありません" \
                    # .format(f_pos,t_pos))
                is_ok = False
    if is_ok :
        # xdebug("\t{}は全部揃いました".format(chainList))
        if ans < chainLen:
            # xdebug("\t\t現在の回答より長いので置き換えます")
            ans = chainLen

print("{}".format(ans))
