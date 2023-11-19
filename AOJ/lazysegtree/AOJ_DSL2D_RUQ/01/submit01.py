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
    lazy = []
    lazyFlag = []
    node = []
    def __init__(self,V):
        sv = len(V)
        self.n=1
        while self.n < sv:
            self.n=self.n*2
        self.node=[E]*(self.n*2-1)
        self.lazy=[E]*(self.n*2-1)
        self.lazyFlag=[False]*(self.n*2-1)
        for j in range(0,sv):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=min(self.node[j*2+1],self.node[j*2+2])
    def eval(self,k,l,r):
        if self.lazyFlag[k]==False:
            return
        self.node[k]=self.lazy[k]
        if 1 < (r-l):
            self.lazy[2*k+1]=self.lazy[k]
            self.lazy[2*k+2]=self.lazy[k]
            self.lazyFlag[2*k+1]=True
            self.lazyFlag[2*k+2]=True
        self.lazy[k]=E
        self.lazyFlag[k]=False
    def update(self,a,b,val,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.lazy[k]=val
            self.lazyFlag[k]=True
            self.eval(k,l,r)
        else:
            mid=(r+l)>>1
            self.update(a,b,val,2*k+1,l,mid)
            self.update(a,b,val,2*k+2,mid,r)
            self.node[k]=min(self.node[2*k+1],self.node[2*k+1])
    def getMin(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            return E
        self.eval(k,l,r)
        if a <= l and r <= b:
            return self.node[k]
        mid = (l+r)>>1
        vl = self.getMin(a,b,k*2+1,l,mid)
        vr = self.getMin(a,b,k*2+2,mid,r)
        return min(vl,vr)
    def find(self,a):
        return self.getMin(a,a+1)
    def __str__(self):
        ans = []
        for j in range(0,self.n*2-1):
            if self.node[j]==E:
                ans.append("E")
            else:
                ans.append(self.node[j])
        return str(ans)

N,Q = MI()
V = [E]*N
G = LazySegment(V)
ans = []
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        _,s,t,val=query
        G.update(s,t+1,val)
    else:
        _,s=query
        val = G.find(s)
        ans.append(val)
for line in ans:
    print(line)
