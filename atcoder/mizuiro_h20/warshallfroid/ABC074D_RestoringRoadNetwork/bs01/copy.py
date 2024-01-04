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
    def WarshallFloyd_search_result(self):
        USE = [[True]*self.N for _ in range(0,self.N)]
        for p in range(0,self.N):
            for j in range(0,self.N):
                for k in range(0,self.N):
                    x = self.d[j][p]+self.d[p][k]
                    if x < self.d[j][k]:
                        xdebug(f"{j}->{p}->{k} < {j}->{k} は矛盾する")
                        return -1
                    if self.d[j][k] == x and p!=j and p!=k:
                        xdebug(f"{j}->{k} と {j}->{p}->{k}は同じなので消す")
                        USE[j][k]=False
        ans=0
        for j in range(0,self.N):
            for k in range(0,self.N):
                if USE[j][k]==True:
                    ans=ans+self.d[j][k]
        return ans//2

MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1
N=II()
A=[]
G=WarshallFloyd(N)
for _ in range(0,N):
    x = LI()
    A.append(x)
for j in range(0,N):
    for k in range(0,N):
        G.add(j,k,A[j][k],True)
ans = G.WarshallFloyd_search_result()
print(ans)
