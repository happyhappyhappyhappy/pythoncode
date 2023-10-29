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

class LazySegmentTree():
    def __init__(self,A):
        self.sz   = len(A)
        self.n = 1
        while self.n < self.sz:
            self.n = self.n*2
        self.node = [(1<<31)-1]*(self.n*2-1)
        self.lazy = [(1<<31)-1]*(self.n*2-1)
        self.lazyFlag = [False]*(self.n*2-1)
        for j in range(0,self.sz):
            self.node[((self.n-1)+j)]=A[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=min(self.node[2*j+1],self.node[2*j+2])
    def lazyEvaluate(self,k,l,r):
        if self.lazyFlag[k]==True:
            self.node[k]=self.lazy[k]
            if(1 < r - l):
                self.lazy[k*2+1]=self.lazy[k]
                self.lazy[k*2+2]=self.lazy[k]
                self.lazyFlag[k*2+1]=True
                self.lazyFlag[k*2+2]=True
            self.lazyFlag[k]=False
    def update(self,a,b,x,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.lazyEvaluate(k,l,r)
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.lazy[k]=x
            self.lazyFlag[k]=True
            self.lazyEvaluate(k,l,r)
        else:
            self.update(a,b,x,2*k+1,l,(l+r)//2)
            self.update(a,b,x,2*k+2,(l+r)//2,r)
            self.node[k]=min(self.node[2*k+1],self.node[2*k+2])
    def find(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.lazyEvaluate(k,l,r)
        if b <= l or r <= a:
            return (1<<31)-1
        if a <= l and r <= b:
            return self.node[k]
        else:
            vl=self.find(a,b,2*k+1,l,(l+r)//2)
            vr=self.find(a,b,2*k+2,(l+r)//2,r)
            return min(vl,vr)
    def __str__(self):
        ansL = []
        for j in range(0,2*self.n-1):
            if self.node[j] != ((1<<31)-1):
                ansL.append(self.node[j])
            else:
                ansL.append('E')
        return str(ansL)
    def strlazy(self):
        ansL = []
        for j in range(0,2*self.n-1):
            if self.lazy[j] != ((1<<31)-1):
                ansL.append(self.lazy[j])
            else:
                ansL.append('E')
        return str(ansL)

N,Q = MI()
A = [(1<<31)-1]*N
G = LazySegmentTree(A)
# print(G.str2())
for j in range(0,Q):
    query = tuple(MI())
    if query[0]==0:
        dummy,s,t,x=query
        G.update(s,t+1,x)
    else:
        dummy,s,t=query
        x = G.find(s,t+1)
        print(x)
