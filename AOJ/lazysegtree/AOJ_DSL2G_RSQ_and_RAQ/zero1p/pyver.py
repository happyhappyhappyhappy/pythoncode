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
    n = 0
    node = []
    lazy = []
    def __init__(self,V):
        sz = len(V)
        self.n=1
        while self.n < sz:
            self.n=self.n*2
        self.node = [0]*(2*self.n-1)
        self.lazy= [0]*(2*self.n-1)
        for j in range(0,sz):
           self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.node[2*j+1]+self.node[2*j+2]
    def eval(self,k,l,r):
        if self.lazy[k]!=0:
            self.node[k]=self.node[k]+self.lazy[k]
            if 1 < r-l:
                self.lazy[2*k+1]=self.lazy[2*k+1]+(self.lazy[k])//2
                self.lazy[2*k+2]=self.lazy[2*k+2]+(self.lazy[k])//2
            self.lazy[k]=0
    def add(self,a,b,x,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.lazy[k]=self.lazy[k]+(r-l)*x
            self.eval(k,l,r)
        else:
            self.add(a,b,x,2*k+1,l,(l+r)//2)
            self.add(a,b,x,2*k+2,(l+r)//2,r)
            self.node[k]=self.node[2*k+1]+self.node[2*k+2]
    def getsum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if b <= l or r <= a:
            return 0
        if a <= l and r <= b:
            return self.node[k]
        vl = self.getsum(a,b,2*k+1,l,(l+r)//2)
        vr = self.getsum(a,b,2*k+2,(l+r)//2,r)
        return vl+vr
    def __str__(self):
        ANSL=[]
        for j in range(0,self.n*2-1):
            if self.node[j] == 0:
               ANSL.append('E')
            else:
                ANSL.append(self.node[j])
        return str(ANSL)
N,Q=MI()
A = [0]*N
G = LazySegmentTree(A)
ANS=[]
for _ in range(0,Q):
    qes=tuple(MI())
    if qes[0] == 0:
        dum,s,t,x = qes
        G.add(s-1,t,x)
    else:
        dum,s,t=qes
        x = G.getsum(s-1,t)
        ANS.append(x)
for line in ANS:
    print(line)
