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

class LazySegment():
    n = 1
    sz = 1
    e = 0
    node = []
    lazy = []
    def __init__(self,V):
        self.sz = len(V)
        while self.n < self.sz:
            self.n = self.n * 2
        self.node=[self.e]*(self.n*2-1)
        self.lazy=[self.e]*(self.n*2-1)
        for j in range(0,self.sz):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.node[2*j+1]+self.node[2*j+2]
    def eval(self,k,l,r):
        if self.lazy[k] != self.e:
            self.node[k]=self.node[k]+self.lazy[k]
            if 1 < (r-l):
                self.lazy[2*k+1]=self.lazy[2*k+1]+(self.lazy[k]//2)
                self.lazy[2*k+2]=self.lazy[2*k+2]+(self.lazy[k]//2)
            self.lazy[k]=self.e
    def add(self,a,b,x,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.lazy[k]=self.lazy[k]+(r-l)*x
            self.eval(k,l,r)
            return
        else:
            self.add(a,b,x,2*k+1,l,(l+r)//2)
            self.add(a,b,x,2*k+2,(l+r)//2,r)
            self.node[k]=self.node[2*k+1]+self.node[2*k+2]
            return
    def oneSum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            return self.e
        self.eval(k,l,r)
        if a <= l and r <= b:
            return self.node[k]
        vl = self.oneSum(a,b,2*k+1,l,(l+r)//2)
        vr = self.oneSum(a,b,2*k+2,(l+r)//2,r)
        return vl+vr
    def __str__(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.node[j] != self.e:
                ansL.append(self.node[j])
            else:
                ansL.append("E")
        return str(ansL)
    def strL(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.node[j] != self.e:
                ansL.append(self.node[j])
            else:
                ansL.append("E")
        return str(ansL)

N,Q = MI()
V = [0]*N
G = LazySegment(V)
ANSL = []
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dmy,s,t,x=query
        s = s-1
        t = t-1
        G.add(s,t+1,x)
    else:
        dmy,j=query
        i = j-1
        x = G.oneSum(i,j)
        ANSL.append(x)
for line in ANSL:
    print(line)
