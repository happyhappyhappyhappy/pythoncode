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
INF = 1000000000

def BellmanFord(edges,V,r):
    d = [INF] * V
    d[r]=0
    cycled=False

    for _ in range(0,V-1):
        for e in edges:
#            xdebug(e)
            u = e[0]
            v = e[1]
            w = e[2]
            x = d[u]+w
            if d[u] != INF and x < d[v]:
                d[v]=x
    # 後1回見てみる
    for e in edges:
        u = e[0]
        v = e[1]
        w = e[2]
        x = d[u]+w
        if d[u]!=INF and x < d[v]:
            cycled=True
            break
    return cycled,d
V,E,r=MI()
Edges=[]
for _ in range(0,E):
    s0,t0,d=MI()
    Edges.append([s0,t0,d])

cycled,d=BellmanFord(Edges,V,r)
# ansStr=""
# for j in range(0,V):
#     x = d[j]
#     if x == INF:
#         ansStr=ansStr+"INF "
#     else:
#         ansStr=ansStr+str(x)+" "
# xdebug(f"結果 : {ansStr}")
if cycled :
    print("NEGATIVE CYCLE")
else:
    for j in range(0,V):
        x = d[j]
        if x == INF:
            print("INF")
        else:
            print(d[j])
