# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from itertools import permutations,accumulate
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
INF=1000000000
class WarshallFloyd():
    def __init__(self,N):
        self.N = N
        self.d = [[INF for _ in range(0,self.N)] for _ in range(0,self.N)]
        for j in range(0,self.N):
            self.d[j][j]=0
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
        return self.d,hasNegativeCycle
    def __str__(self):
        str_all=""
        for j in range(0,self.N):
            str_p=""
            for k in range(0,self.N):
                str_p=str_p+str(self.d[j][k])+" "
            str_all=str_all+str_p+"\n"
        return str_all
N,M,R=MI()
Ru = LI()
G=WarshallFloyd(N+1)
for _ in range(0,M):
    a,b,c=MI()
    G.add(a,b,c)
# xdebug(G)
d,cycled=G.WarshallFloyd_search()
# for j in range(1,N+1):
#     p_str=""
#     for k in range(1,N+1):
#         x = d[j][k]
#         if x == INF:
#             p_str=p_str+"INF "
#         else:
#             p_str=p_str+str(x)+" "
# #    xdebug(p_str)
ans=INF
for x in permutations(Ru):
#    xdebug(f"組み合わせ {x}")
    cost=0
    for j in range(0,len(Ru)-1):
#        xdebug(f"{x[j]}->{x[j+1]}")
        cost=cost+d[x[j]][x[j+1]]
    if cost < ans:
        ans=cost
print(ans)
