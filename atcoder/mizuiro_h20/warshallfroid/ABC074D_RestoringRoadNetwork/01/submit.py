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
        self.d=[[float('inf')]*self.N for _ in range(0,self.N)]
    def add(self,u,v,c,Directed=False):
        if Directed is False:
            self.d[u][v]=c
            self.d[v][u]=c
        else:
            self.d[u][v]=c
    def WarshallFloyd_Search(self):
        used=[[True]*self.N for _ in range(0,self.N)]
        for p in range(0,self.N):
            for j in range(0,self.N):
                for k in range(0,self.N):
                    x = self.d[j][p]+self.d[p][k]
                    if x < self.d[j][k]:
#                              判定結果,used(放棄する)
                        return False,used
                    if x == self.d[j][k] and j != p and p!=k:
                            # j->kの直接道路は無かったことにする
                        used[j][k]=False
        return True,used
N=II()
A=[]
for _ in range(0,N):
    A.append(LI())
G=WarshallFloyd(N)
for j in range(0,N):
    for k in range(0,N):
        G.add(j,k,A[j][k],True)
Judge,used=G.WarshallFloyd_Search()
if Judge is False:
    print("-1")
else:
    ans=0
    for j in range(0,N):
        # strLine=""
        for k in range(0,N):
            if used[j][k] is True:
                # strLine=strLine+str(A[j][k])
                ans=ans+A[j][k]
            # else:
            #     strLine=strLine+"x"
            # if k != N-1:
            #     strLine=strLine+" "
        # print(strLine)
    print(ans//2)
