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

class WarshallFloyd():
    def __init__(self,N):
        self.N=N
        self.d=[[float('inf')]*N for _ in range(0,N)]
    def add(self,u,v,c,directed=False):
        if directed is False:
            self.d[u][v]=c
            self.d[v][u]=c
        else:
            self.d[u][v]=c
    def WarshallFloyd_search(self):
        for p in range(0,self.N):
            for j in range(0,self.N):
                for k in range(0,self.N):
                    x = self.d[j][p]+self.d[p][k]
                    if x < self.d[j][k]:
                        self.d[j][k]=x
        hasNegativeCycle = False
        for j in range(self.N):
            if self.d[j][j] < 0:
                hasNegativeCycle=True
                break
        return hasNegativeCycle,self.d
V,E = MI()
G=WarshallFloyd(V)
for j in range(0,V):
    G.add(j,j,0,True)
for _ in range(0,E):
    a,b,c=MI()
    G.add(a,b,c,True)
neg,D=G.WarshallFloyd_search()
if neg is True:
    print("NEGATIVE CYCLE")
else:
    for j in range(0,V):
        for k in range(0,V):
            x = D[j][k]
            if x == float('inf'):
                D[j][k] = "INF"
    for j in range(0,V):
        out = " ".join(map(str,D[j]))
        print(out)
