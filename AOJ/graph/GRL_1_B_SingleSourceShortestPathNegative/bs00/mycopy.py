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
INF=1<<60
def Bellman_ford(G,V,s):
    d = [INF] * V
    cycled=False
    d[s]=0
    cnt = 0
    while cnt < V:
        # xdebug(f"ただいま {cnt+1} 回目の検索")
        ended=True
        for e in G:
            fm,to,cost = e
            x = d[fm]+cost
            if d[fm]!=INF and x < d[to]:
                # xdebug(f"{fm}->{to} にてよりよい経路発見")
                d[to]=x
                ended=False
        if ended == True:
            # xdebug(f"{cnt+1}回目の検索で終わったので抜ける")
            break
        cnt = cnt+1
    if cnt == V:
        cycled=True
    else:
        cycled=False
    return d,cycled

V,E,s=MI()
Graph=[]
for _ in range(0,E):
    f,t,c=MI()
    Graph.append([f,t,c])
D,C=Bellman_ford(Graph,V,s)
# xdebug(Graph)
if C == True:
    print("NEGATIVE CYCLE")
else:
    for j in range(0,V):
        if D[j]==INF:
            print("INF")
        else:
            print(D[j])
