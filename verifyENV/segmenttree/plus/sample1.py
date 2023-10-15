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

class segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for j in range(0,2*self.size)]
        for j in range(0,self.n):
            self.d[self.size+j]=V[j]
        for j in range(self.size-1,0,-1):
            self.update(j)
    def set(self,p,x):
        assert 0 <= p and p < self.n
        p = p + self.size
        self.d[p]=x
        xdebug(f"位置 p = {p-self.size} を {x} に変更しました ")
        for j in range(1,self.log+1):
            pos = p >> j
            xdebug(f"変更に伴い{pos}へアップデートします")
            self.update(p>>j)
    def get(self,p):
        assert 0 <= p and p < self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        assert 0 <= l and l <= r and r <= self.n
        sml=self.e
        smr=self.e
        l=self.size+l
        r=r+self.size
        while(l<r):
            oddl=l&1
            if oddl == 1:
                sml = self.op(sml,self.d[l])
                l=l+1
            oddr = r & 1
            if oddr == 1:
                smr = self.op(self.d[r-1],smr)
                r = r -1
            l = l >> 1
            r = r >> 1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def max_right(self,l,f):
        assert 0 <= l and l <= self.n
        assert f(self.e)
        if l == self.n:
            return self.n
        l=l+self.size
        sm=self.e
        while True:
            while(l%2==0):
                l = l >> 1
            if f(self.op(sm,self.d[l])) == False:
                while(l<self.size):
                    l=l*2
                    if f(self.op(sm,self.d[l])) == True:
                        sm = self.op(sm,self.d[l])
                return l-self.size
            sm=self.op(sm,self.d[l])
            l=l+1
            andl = l & -l
            if andl == l:
                break
        return self.n
    def min_left(self,r,f):
        assert 0 <= r and r <= self.e
        assert f(self.e)
        if r == 0:
            return 0
        r=r+self.size
        sm=self.e
        while True:
            r=r-1
            while( 1 < r and ((r % 2)==1)):
                r = r >> 1
            if f(self.op(self.d[r],sm)) == False:
                while r<self.size:
                    r=(r*2+1)
                    if self.op(self.d[r],sm)== True:
                        sm=self.op(self.d[r],sm)
                        r=r-1
                return r+1-self.size
            sm = self.op(self.d[r],sm)
            allr= r & (-r)
            if allr == r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])

    def __str__(self):
        ret = str([self.get(j) for j in range(self.n)])
        return ret

def add(x,y):
    return x+y

N,Q = MI()
A=LI()
G=segtree(A,add,0)
for _ in range(0,Q):
    t,a,b = MI()
    if t==1:
        xdebug(f"差し替え前 G:{G}")
        x=a
        v=b
        x=x-1
        G.set(x,v)
        xdebug(f"差し替え後 G:{G}")
    elif t==2:
        l = a
        r = b
        l = l-1
        r = r-1
        x = G.prod(l,r+1)
        print(f"{l+1}から{r+1}までの和は{x}です")
    else:
        x = G.all_prod()
        print(f"全部の和は{x}です")
