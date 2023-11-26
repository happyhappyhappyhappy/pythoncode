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
INF=(1<<31)-1

class LazySegment():
    def __init__(self,n_,fx,fa,fm,ex,em):
        x = 1
        while x < n_:
            x = x*2
        self.n=x
        self.FX=fx # node同士の演算:最小値
        self.FA=fa # lazyからnodeへのアクセス:加算
        self.FM=fm # lazy内の積み立て:加算
        self.ex=ex # node初期値単位元
        self.em=em # lazy初期値恒等写像
        self.node=[ex]*(self.n*2-1)
        self.lazy=[em]*(self.n*2-1)
    def set(self,p,val):
        self.node[(self.n-1)+p]=val
    def build(self):
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.FX(self.node[2*j+1],self.node[2*j+2])
    def eval(self,k): # lazy->node処理
        # xdebug(f"self.lazy[{k}]={self.lazy[k]}")
        if self.lazy[k]==em:
            return
        if k < self.n-1:
            self.lazy[2*k+1]=self.FM(self.lazy[2*k+1],self.lazy[k])
            self.lazy[2*k+2]=self.FM(self.lazy[2*k+2],self.lazy[k])
        self.node[k]=self.FA(self.node[k],self.lazy[k])
        self.lazy[k]=0
    def add(self,a,b,x,k=0,l=0,r=-1):
        self.eval(k)
        if r < 0:
            r = self.n
        if a <= l and r <= b:
            self.lazy[k]=self.FM(self.lazy[k],x)
            self.eval(k)
        elif a < r and l < b:
            mid=(r+l)>>1
            self.add(a,b,x,2*k+1,l,mid)
            self.add(a,b,x,2*k+2,mid,r)
            self.node[k]=self.FX(self.node[2*k+1],self.node[2*k+2])
    def query(self,a,b,k=0,l=0,r=-1):
        self.eval(k)
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            return self.ex
        elif a <= l and r <= b:
            return self.node[k]
        else:
            mid=(l+r)>>1
            vl = self.query(a,b,2*k+1,l,mid)
            vr = self.query(a,b,2*k+2,mid,r)
            return self.FX(vl,vr)
    def __str__(self):
        ans = []
        for j in range(0,self.n*2-1):
            if self.node[j]==self.ex:
                ans.append("H")
            else:
                ans.append(self.node[j])
        return str(ans)
N,Q=MI()
def fx(x1,x2):
    return min(x1,x2)
def fa(n,l):
    return l+n
def fm(la1,la2):
    return la1+la2
ex=(1<<31)-1
em=0
G=LazySegment(N,fx,fa,fm,ex,em)
for j in range(0,N):
    G.set(j,0)
G.build()
ans=[]
for j in range(0,Q):
    q = tuple(MI())
    if q[0] == 0:
        _,s,t,val=q
        # xdebug(f"from {s} to {t+1}")
        G.add(s,t+1,val)
    else:
        _,s,t=q
        # xdebug(f"{j}->{G}")
        val = G.query(s,t+1)
        ans.append(val)
for line in ans:
    print(line)
