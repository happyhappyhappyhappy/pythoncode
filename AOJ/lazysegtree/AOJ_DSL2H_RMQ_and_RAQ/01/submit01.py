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
E = MAXSIZE
class LazySegment():
    n = 0
    node = []
    lazy = []
    lazyFlag = []
    def __init__(self,V):
        sv = len(V)
        self.n=1
        while self.n < sv:
            self.n=self.n*2
        self.node=[E]*(self.n*2-1)
        self.lazy=[0]*(self.n*2-1)
        self.lazyFlag=[False]*(self.n*2-1)
        for j in range(0,sv):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=min(self.node[2*j+1],self.node[2*j+2])
    def eval(self,k,l,r):
        if self.lazyFlag[k]==True:
                self.node[k]=self.node[k]+self.lazy[k]
                if 1 < (r-l):
                    self.lazy[k*2+1]=self.lazy[k*2+1]+(self.lazy[k]>>1)
                    self.lazy[k*2+2]=self.lazy[k*2+2]+(self.lazy[k]>>1)
                    self.lazyFlag[k*2+1]=True
                    self.lazyFlag[k*2+2]=True
                self.lazy[k]=0
                self.lazyFlag[k]=False
    def add(self,a,b,val,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.lazy[k]=self.lazy[k]+(r-l)*val
            self.lazyFlag[k]=True
            self.eval(k,l,r)
        else:
            mid = (r+l)>>1
            self.add(a,b,val,k*2+1,l,mid)
            self.add(a,b,val,k*2+2,mid,r)
            self.node[k]=min(self.node[k*2+1],self.node[k*2+2])
    def find(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            return E
        self.eval(k,l,r)
        if a <= l and r <= b:
            return self.node[k]
        mid = (l+r)>>1
        vl = self.find(a,b,k*2+1,l,mid)
        vr = self.find(a,b,k*2+2,mid,r)
        return min(vl,vr)
    def __str__(self):
        ans=["node:"]
        for j in range(0,self.n*2-1):
            if self.node[j]==E:
                ans.append("E")
            else:
                ans.append(self.node[j])
        return str(ans)
    def strL(self):
        ans=["lazy:"]
        for j in range(0,self.n*2-1):
            if self.lazy[j]==E:
                ans.append("E")
            else:
                ans.append(self.lazy[j])
        return str(ans)


N,Q = MI()
V = [0]*N
G = LazySegment(V)
ans = []
for q in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dmy,s,t,x=query
        G.add(s,t+1,x)
    else:
        dmy,s,t=query
        # xdebug(f"In {q+1} GNode->{G}")
        # xdebug(f"In {q+1} GLazy->{G.strL()}")
        x = G.find(s,t+1)
        # xdebug(f"In {q+1} GNode事後->{G}")
        # xdebug(f"In {q+1} GLazy事後->{G.strL()}")
        ans.append(x)
for line in ans:
    print(line)
