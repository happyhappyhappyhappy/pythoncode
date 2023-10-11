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

class SegTree():
    class SegTree():
        n=1
        size = 1
        log = 2
        d=[0]
        op=None
        e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        # self.size=self.log>>1
        self.size=1<<self.log
        self.d=[E for j in range(0,2*self.size)]
        for j in range(0,self.n):
            self.d[self.size+j]=V[j]
        for j in range(self.size-1,0,-1):
            self.update(j)
    def set(self,p,x):
        assert 0 <= p and p < self.n
        p=p+self.size
        self.d[p]=x
        for j in range(1,self.log+1):
            pos = p >> j
            self.update(pos)
    def get(self,p):
        assert 0 <= p and p < self.n
        x = p+self.size
        return self.d[x]
    def prod(self,l,r):
        assert 0 <= l and l <= r and r <= self.n
        sml=self.e
        smr=self.e
        l=l+self.size
        r=r+self.size
        while(l<r):
            oddcheck=l&1
            if oddcheck==1:
                sml=self.op(sml,self.d[l])
                l=l+1
            oddcheck=r&1
            if oddcheck==1:
                smr=self.op(self.d[r-1],smr)
                r=r-1
            l=l>>1
            r=r>>1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def max_right(self,l,f):
        assert 0 <= l and l <= self.n
        assert f(self.e)
        if l==self.n:
            return self.n
        l=l+self.size
        sm=self.e
        while(1):
            while(l%2==0):
                l=l>>1
            if f(self.op(sm,self.d[l]))==False:
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l]))==True:
                        sm=self.op(sm,self.d[l])
                return l-self.size
            sm=self.op(sm,self.d[l])
            l=l+1
            allCheck=l&(-l)
            if allCheck==l:
                break
        return self.n
    def min_left(self,r,f):
        assert 0 <= r and r <= self.n
        assert f(self.e)
        if r==0:
            return 0
        r=r+self.size
        sm=self.e
        while(1):
            r=r-1
            while(1<r and (r%2)):
                r=r>>1
            if f(self.op(self.d[r],sm))==False:
                while(r<self.size):
                    r=2*r+1
                    if f(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r=r-1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            x=r&(-r)
            if x==r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        return str([self.get(j) for j in range(0,self.n)])

def solver():
    result = 0
    # algorithm
    A=LI()
    G=SegTree([j for j in A],max,-1)
    for j in range(0,Q):
        t,a,b=MI()
        if t==1:
            v=b
            x=a-1
            G.set(x,v)
        if t==2:
            l = a-1
            r = b-1
            print(G.prod(l,r+1))
        if t==3:
            x=a-1
            v=b
            def func(arg):
                xdebug(f"関数funcを{arg}で実行されました")
                if v>arg:
                    return True
                else:
                    return False
            print(G.max_right(x,func)+1)

if __name__ == "__main__":
    global N,Q
    N,Q=MI()
    solver()
