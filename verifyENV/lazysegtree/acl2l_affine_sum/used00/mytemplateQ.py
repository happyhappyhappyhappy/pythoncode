# 遅延セグメント木の速度早めた物。しかし、データが分からない
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

class lazy_segtree():
    def __init__(self,V,OP,E,MAPPING,COMPOSITION,ID):
        self.n=len(V)
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for j in range(2*self.size)]
        self.lz=[ID for j in range(self.size)]
        self.e=E
        self.op=OP
        self.mapping=MAPPING
        self.composition=COMPOSITION
        self.identity=ID
        for j in range(self.n):
            self.d[self.size+j]=V[j]
        for j in range(self.size-1,0,-1):
            self.update(j)
    def set(self,p,x):
        assert 0 <= p and p < self.n
        p=p+self.size
        for j in range(self.log,0,-1):
            self.push(p>>i)
        self.d[p]=x
        for j in range(1,self.log+1):
            self.update(p>>j)
    def get(self,p):
        assert 0 <= p and p < self.n
        p=p+self.size
        for j in range(self.log,0,-1):
            self.push(p>>j)
        return self.d[p]
    def prod(self,l,r):
        assert 0 <= l and l <= r and r<=self.n
        if l==r:return self.e
        l=l+self.size
        r=r+self.size
        for j in range(self.log,0,-1):
            x = (l>>j)<<j
            if x != l:
                self.push(l>>j)
            x = (r>>j)<<j
            if x != r:
                self.push(r>>j)
        sml=self.e
        smr=self.e
        while(l<r):
            oddl=l&1
            if oddl==1:
                sml=self.op(sml,self.d[l])
                l=l+1
            oddr=r&1
            if oddr == 1:
                r=r-1
                smr=self.op(self.d[r],smr)
            l=l>>1
            r=r>>1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def apply(self,l,r,f):
        assert 0<= l and l <= r and r <= self.n
        if l==r:
            return
        l=l+self.size
        r=r+self.size
        for j in range(self.log,0,-1):
            x = (l>>j)<<j
            if x != l:
                self.push(l>>j)
            x = (r>>j)<<j
            if x != r:
                self.push((r-1)>>j)
        l2,r2=l,r
        while(l<r):
            oddl=l&1
            if oddl==1:
                self.all_apply(l,f)
                l=l+1
            oddr=r&1
            if oddr == 1:
                r=r-1
                self.all_apply(r,f)
            l=l>>1
            r=r>>1
        l=l2
        r=r2
        for j in range(1,self.log+1):
            x = (l>>j)<<j
            if x != l:
                self.update(l>>j)
            x = (r>>j)<<j
            if x != r:
                self.update((r-1)>>j)
    def max_right(self,l,g):
        assert 0 <= l and l <= self.n
        assert g(self.e)
        if l==self.n:
            return self.n
        l=l+self.size
        for j in range(self.log,0,-1):
            self.push(l>>j)
        sm=self.e
        while(True):
            while(l%2==0):
                l=l>>1
            if g(self.op(sm,self.d[l])) == False:
                while(l<self.size):
                    self.push(l)
                    l=2*l
                    if (g(self.op(sm,self.d[l]))) == True:
                        sm=self.op(sm,self.d[l])
                        l=l+1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l=l+1
            twoPow=l%(-l)
            if twoPow == l:
                break
        return self.n
    def min_left(self,r,g):
        assert 0 <= r and r <= self.n
        assert g(self.e)
        if r==0:
            return 0
        r=r+self.size
        for j in range(self.log,0,-1):
            x = (r-1)>>j
            self.push(x)
        sm=self.e
        while(True):
            while(1<r and ((r%2)==1)):
                r = r>>1
            if g(self.op(self.d[r],sm))==False:
                while(r<self.size):
                    self.push(r)
                    r=r*2+1
                    if g(self.op(self.d[r],sm))==True:
                        sm=self.op(self.d[r],sm)
                        r=r-1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            twoPow=r&(-r)
            if twoPow == r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def all_apply(self,k,f):
        self.d[k]=self.mapping(f,self.d[k])
        if(k<self.size):
            self.lz[k]=self.composition(f,self.lz[k])
    def push(self,k):
        self.all_apply(2*k,self.lz[k])
        self.all_apply(2*k+1,self.lz[k])
        self.lz[k]=self.identity
    def __str__(self):
        ret = [self.get(j) for j in range(0,self.n)]
        return str(ret)
    def str2(self):
        ansL=[]
        for j in range(1,self.size*2):
            if self.d[j] == self.e:
                ansL.append("e")
            else :
                ansL.append(self.d[j])
        return "内部詳細 : "+str(ansL)
N,Q = MI()
a=LI()
ans=[]
mod=998243353
def operate(a,b):
    a0=a>>32
    a1=a%(1<<32)
    b0=b>>32
    b1=b%(1<<32)
    return (((a0+b0)%mod)<<32)+a1+b1
def mapping(f,x):
    f0=f>>32
    f1=f%(1<<32)
    x0=x>>32
    x1=x%(1<<32)
    return (((f0*x0)%mod)<<32)+x1
def composition(f,g):
    f0=f>>32
    f1=f%(1<<32)
    g0=g>>32
    g1=g%(1<<32)
    return (((f0*g0)%mod)<<32)+((g1*f0+f1)%mod)
def mapping(f,x):
    f0=f>>32
    f1=f%(1<<32)
    x0=x>>32
    x1=x%(1<<32)
    return (((f0*x0+x1*f1)%mod)<<32)+x1

G=lazy_segtree([(j<<32)+1 for j in a],operate,0,mapping,composition,1<<32)
xdebug(G)
xdebug(G.str2())
for j in range(0,Q):
    seq=tuple(MI())
    if seq[0]==0:
        dummy,l,r,b,c=seq
        G.apply(l,r,(b<<32)+c)
    else:
        dummy,l,r=seq
        ans.append(G.prod(l,r)>>32)

for line in ans:
    print(line)
