# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

# デバッグ出力の作成
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# クラス+メソッドを一関数
xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1
INF = (1<<60)

def BellmanFord(edges,V,start):
    dist=[INF]*V
    dist[start]=0
    for _ in range(0,V):
        changed=False
        for e in edges:
            fm,to,cost=e
            if dist[fm]==INF:
                continue
            x = dist[fm]+cost
            if x < dist[to]:
                dist[to]=x
                changed=True
        if changed == False:
            return dist
    for _ in range(0,V):
        for e in edges:
            fm,to,cost=e
            if dist[fm]==INF:
                continue
            x = dist[fm]+cost
            if x < dist[to]:
                dist[to]=(-1)*INF
    return dist

V,E=MI()
edges=[]
for _ in range(0,E):
    a,b,c=MI()
    edges.append([a-1,b-1,c*(-1)])
dist = BellmanFord(edges,V,0)
ans = dist[V-1]*(-1)
if ans == INF:
    print("inf")
else:
    print(ans)
