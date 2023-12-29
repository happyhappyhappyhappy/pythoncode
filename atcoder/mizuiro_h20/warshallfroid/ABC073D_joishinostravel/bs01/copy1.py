# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from itertools import permutations
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
INF=float('inf')
class WarshallFloyd():
    def __init__(self,N):
        self.N=N
        self.d=[[INF]*N for _ in range(N)]
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

        hasNegativeCycle=False
        for j in range(0,self.N):
            if self.d[j][j]<0:
                hasNegativeCycle=True
                break
        for j in range(0,self.N):
            self.d[j][j]=0
        return hasNegativeCycle,self.d

N,M,R=MI()
route=LI()
G=WarshallFloyd(N+1)
for j in range(0,M):
    f,t,cost=MI()
    G.add(f,t,cost,False)
neg,D=G.WarshallFloyd_search()
ans=INF
for r in list(permutations(route)):
    cost=0
    for j in range(0,R-1):
        cost=cost+D[r[j]][r[j+1]]
    if cost < ans:
        ans=cost
print(ans)
