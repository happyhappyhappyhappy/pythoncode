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
E = (1<<31)-1

class LazySegment():
    n = 0
    node = []
    lazy = []
    lazyFlag = []
    def __init__(self,V):
        sz = len(V)
        self.n=1
        while self.n < sz:
            self.n = self.n*2
        self.node=[E]*(self.n*2-1)
        self.lazy=[E]*(self.n*2-1)
        self.lazyFlag=[False]*(self.n*2-1)
        for j in range(0,sz):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=min(self.node[2*j+1],self.node[2*j+2])
    def eval(self,k,l,r):
        if self.lazyFlag[k]:
            self.node[k]=self.lazy[k]
            if 1 < r - l:
                self.lazy[k*2+1]=self.lazy[k]
                self.lazy[k*2+2]=self.lazy[k]
                self.lazyFlag[k*2+1]=True
                self.lazyFlag[k*2+2]=True
            self.lazyFlag[k]=False
    def update(self,a,b,x,k=0,l=0,r=-1):
        if r < 0 :
            r = self.n
        self.eval(k,l,r)
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.lazy[k]=x
            self.lazyFlag[k]=True
            self.eval(k,l,r)
        else:
            self.update(a,b,x,2*k+1,l,(l+r)//2)
            self.update(a,b,x,2*k+2,(l+r)//2,r)
            self.node[k]=min(self.node[2*k+1],self.node[2*k+2])
    def find(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if b <= l or r <= a:
            return E
        if a <= l and r <= b:
            return self.node[k]
        else:
            vl=self.find(a,b,2*k+1,l,(l+r)//2)
            vr=self.find(a,b,2*k+2,(l+r)//2,r)
            return min(vl,vr)
    def __str__(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.node[j]!=E:
                ansL.append(self.node[j])
            else:
                ansL.append("E")
        return str(ansL)
    def strL(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.lazy[j]!=E:
                ansL.append(self.lazy[j])
            else:
                ansL.append("E")
        return str(ansL)
    def strL2(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.lazyFlag[j]==True:
                ansL.append("O")
            else:
                ansL.append("X")
        return str(ansL)
N,Q=MI()
V = [E]*N
G = LazySegment(V)
ansL=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dmy,s,t,x=query
        G.update(s,t+1,x)
    else:
        dmy,s,t=query
        x = G.find(s,t+1)
        ansL.append(x)
for list in ansL:
    print(list)
