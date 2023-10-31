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
    n = 1
    size = 1
    log = 2
    d = [0]
    op = None
    e = 10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
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
        # テンプレート setと異なるところは、ここがself.d[p]=xになるところが
        # self.d[p]=self.d[p]+xに加算に回していること
        self.d[p]=self.d[p]+x
        for j in range(1,self.log+1):
            y = p >> j
            xdebug(f"配列要素{p-self.size}の操作に伴い、中身{y}をアップデートします")
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
            if oddr == 1:
                smr=self.op(self.d[r-1],smr)
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
                            l=l+1
                    return l-self.size
            sm=self.op(sm,self.d[l])
            l=l+1
            lpow2=l&(-l)
            if lpow2==l:
                break
        return self.n
    def min_self(self,r,f):
        assert 0 <= r and r <= self.n
        assert self.f(e)
        if r==0:
            return 0
        r = r + self.size
        sm=self.e
        while True:
            r=r-1
            while(1<r and ((r%2==1)==True)):
                r=r>>1
                if f(self.op(self.d[r],sm))==False:
                    while(r<self.size):
                        r=r*2+1
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
        xdebug(f"update({k})の場面 要素{k*2}と{k*2+1}のopつまり和を 要素{k}に反映")
        self.d[k]=self.op(self.d[k*2],self.d[2*k+1])
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

def add(x,y):
    z = x+y
    return z

N,Q=MI()
A = [0]*N
G=SegTree(A,add,0)
ANSL=[]
for _ in range(0,Q):
    que=tuple(MI())
    if que[0]==0:
        com,j,x=que
        j=j-1
#        xdebug(f"j={j},x={x}")
        G.set(j,x)
        xdebug(f"SegTreeの中身1: {G}")
        xdebug(G.str2())
    else :
        com,l,r=que
        x = G.prod(l-1,r)
        ANSL.append(x)

for line in ANSL:
    print(line)
