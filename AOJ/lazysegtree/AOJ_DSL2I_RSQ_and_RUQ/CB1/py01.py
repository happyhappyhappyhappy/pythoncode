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
em=(1<<31)-1
class LazySegment():
    n=0
    dat=[]
    lazy=[]
    def __init__(self,n):
        x = 1
        self.n=1
        while x < n:
            x = x*2
        self.n=x
        self.dat=[0]*(self.n*2-1)
        self.lazy=[em]*(self.n*2-1)
    def eval(self,k,leng):
        if self.lazy[k]==em:
            return
        if k < (self.n-1):
            self.lazy[k*2+1]=self.lazy[k]
            self.lazy[k*2+2]=self.lazy[k]
        self.dat[k]=self.lazy[k]*leng
        self.lazy[k]=em
    def update(self,a,b,x,k=0,l=0,r=-1):
        if r < 0:
            r=self.n
        self.eval(k,r-l)
        if a <= l and r <= b:
            self.lazy[k]=x
            self.eval(k,r-l)
        elif a < r and l < b:
            mid = (r+l)>>1
            self.update(a,b,x,k*2+1,l,mid)
            self.update(a,b,x,k*2+2,mid,r)
            self.dat[k]=self.dat[k*2+1]+self.dat[k*2+2]
    def getSum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,r-l)
        if r <= a or b <= l:
            return 0
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            mid=(l+r)>>1
            vl=self.getSum(a,b,2*k+1,l,mid)
            vr=self.getSum(a,b,2*k+2,mid,r)
            return vl+vr
    def dprint(self):
        ans=["dat"]
        for j in range(0,2*self.n-1):
            ans.append(self.dat[j])
        xdebug(str(ans))
        ans=["lazy"]
        for j in range(0,2*self.n-1):
            if self.lazy[j]==em:
                ans.append("E")
            else:
                ans.append(self.lazy[j])
        xdebug(str(ans))

N,Q=MI()
G=LazySegment(N)
ans=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        _,s,t,val=query
        G.update(s,t+1,val)
#        xdebug(f"{j+1}行目<update>の後")
#        G.dprint()
    elif query[0]==1:
        _,s,t=query
#        xdebug(f"{j+1}行目<getSum>の前")
#        G.dprint()
        val=G.getSum(s,t+1)
        ans.append(val)
for line in ans:
    print(line)
