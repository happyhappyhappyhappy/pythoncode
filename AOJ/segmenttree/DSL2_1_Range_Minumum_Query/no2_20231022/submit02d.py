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
## Segment Tree Start ##

class SegTree():
    n = 1
    size = 1
    log = 2
    d = [0]
    op = None
    e = 10**15
    def __init__(self,V,OP,E):
        self.n = len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E]*(self.size*2)
        for j in range(0,self.n):
            self.d[self.size+j]=V[j]
        for j in range(self.size-1,0,-1):
            self.update(j)
    def set(self,p,x):
        assert 0 <= p and p < self.n
        p = p + self.size
        self.d[p]=x
        for j in range(1,self.log+1):
            self.update(p>>j)
    def get(self,p):
        assert 0 <= p and p < self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        assert 0 <= l and l <= r and r <= self.n
        sml=self.e
        smr=self.e
        l = l + self.size
        r = r + self.size
        while(l<r):
            oddl=l&1
            if oddl == 1:
                sml=self.op(sml,self.d[l])
                l=l+1
            oddr=r&1
            if oddr==1:
                smr = self.op(self.d[r-1],smr)
                r = r-1
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
                if f(self.op(sm,self.d[l]))==False:
                    while(l<self.size):
                        l=l*2
                        if f(self.op(sm,self.d[l]))==True:
                            sm=self.op(sm,self.d[l])
                            l = l + 1
                    return l-self.size
            sm=self.op(sm,self.d[l])
            l=l+1
            lpow2=l&(-l)
            if lpow2==l:
                break
        return self.n
    def min_left(self,r,f):
        assert 0 <= r and r <= self.n
        assert f(self.e)
        if r==0:
            return 0
        r = r+self.size
        sm=self.e
        while True:
            r=r-1
            while(1<r and ((r%2==1)==1)):
                r=r>>1
                if f(self.op(self.d[r],sm))==False:
                    while(r<self.size):
                        r=2*r+1
                        if f(self.op(self.d[r],sm))==True:
                            sm=self.op(self.d[r],sm)
                            r=r-1
                    return r+1-self.size
            sm=self.op(self.d[r],sm)
            rpow2=r&(-r)
            if rpow2==r:
                break
        return 0
    def update(self,k):
        xdebug(f"d[{2*k}]とd[{2*k+1}]を比較しその結果をd[{k}]に書き込みます")
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        ret = [self.get(j) for j in range(0,self.n)]
        return str(ret)
    def str2(self):
        retl = []
        for j in range(1,2*self.size):
            x=self.d[j]
            if x == self.e:
                retl.append("e")
            else:
                retl.append(x)
        return str(retl)
## Segment Tree End ##

def pow2(p,n):
    res=1
    while 0 < n:
        oddn=n&1
        if oddn == 1:
            res=res*p
        p=p*p
        n=n>>1
    return res

def min2(x,y):
    xdebug(f"{x}と{y}どちらが小さいか比較します")
    if y < x:
        xdebug(f"{y}が小さいです")
        return y
    else:
        xdebug(f"{x}が小さいです")
        return x

def solver(A):
    result = []
    # algorithm
    G=SegTree(A,min2,MAXSIZE)
    for _ in range(0,Q):
        que=tuple(MI())
        if que[0]==0:
            dmy,i,x=que
            G.set(i,x)
        else:
            dmy,s,t=que
            answer=G.prod(s,t+1)
            result.append(answer)
    return result

if __name__ == "__main__":
    global N,Q
    N,Q = MI()
    A = [pow2(2,31)-1]*N
    AList = solver(A)
    for line in AList:
        print(line)
