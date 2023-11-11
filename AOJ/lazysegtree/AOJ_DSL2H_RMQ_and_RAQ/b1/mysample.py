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
INF = MAXSIZE
class RMQ():
    def __init__(self,N_):
        self.dat=[INF]*(N_*4)
        self.lazy=[0]*(N_*4)
        x = 1
        while x < N_:
            x = x*2
        self.n=x
    def set(self,j,val):
        self.dat[(self.n-1)+j]=val
    def build(self):
        for j in range(self.n-2,-1,-1):
            self.dat[j]=min(self.dat[j*2+1],self.dat[j*2+2])
    def eval(self,k):
        if self.lazy[k]==0:
            return
        if k < self.n-1:
            self.lazy[k*2+1]=self.lazy[k*2+1]+self.lazy[k]
            self.lazy[k*2+2]=self.lazy[k*2+2]+self.lazy[k]
        self.dat[k]=self.dat[k]+self.dat[k]
        self.lazy[k]=0
    def add_sub(self,a,b,x,k,l,r):
        self.eval(k)
        if a <= l and r <= b:
            self.lazy[k]=self.lazy[k]+x
            self.eval(k)
        elif a < r and l < b:
            mid = (r+l)>>1
            self.add_sub(a,b,x,k*2+1,l,mid)
            self.add_sub(a,b,x,k*2+2,mid,r)
            self.dat[k]=min(self.dat[k*2+1],self.dat[k*2+2])
    def add(self,a,b,x):
        r = self.n
        self.add_sub(a,b,x,0,0,r)
    def query_sub(self,a,b,k,l,r):
        self.eval(k)
        if r <= a or b <= l:
            return INF
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            mid=(l+r)>>1
            vl=self.query_sub(a,b,k*2+1,l,mid)
            vr=self.query_sub(a,b,k*2+2,mid,l)
            return min(vl,vr)
    def query(self,a,b):
        r = self.n
        return self.query_sub(a,b,0,0,r)
    def get(a):
        return self.query(a,a+1)
    def __str__(self):
        ans = ["node:"]
        for j in range(self.n-1,self.n*2-1,1):
            ans.append(self.dat[j])
        return str(ans)

N,Q = MI()
G=RMQ(N)
for j in range(0,N):
    G.set(j,0)
G.build()
ans=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0] == 0:
        _,s,t,val=query
        G.add(s,t+1,val)
    else:
        _,s,t=query
        xdebug(G)
        val = G.query(s,t+1)
        ans.append(val)
for line in ans:
    print(line)
