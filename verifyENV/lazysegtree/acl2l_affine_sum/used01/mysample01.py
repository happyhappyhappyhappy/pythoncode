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
        for j in range(0,self.n):
            self.d[self.size+j]=V[j]
        for j in range(self.size-1,0,-1):
            self.update(j)
    def set(self,p,x):
        assert 0 <= p and p < self.n
        p = p + self.size
        for j in range(self.log,0,-1):
            self.push(p>>j)
        self.d[p]=x
        for j in range(1,self.log+1):
            a = p >> j
            self.update(a)
    def get(self,p):
        assert 0 <= p and p < self.n
        p=p+self.size
        for j in range(self.log,0,-1):
            self.push(p>>j)
        return self.d[p]
    def prod(self,l,r):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return self.e
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
            if oddr==1:
                r=r-1
                smr=self.op(self.d[r],smr)
            l = l >> 1
            r = r >> 1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def apply(self,l,r,f):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
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
            if oddl == 1:
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
        if l == self.n:
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
                    l=l*2
                    if g(self.op(sm,self.d[l])) == True:
                        sm=self.op(sm,self.d[l])
                        l=l+1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l=l+1
            twoPow=l&(-l)
            if twoPow == l:
                break
        return self.n
    def min_left(self,r,g):
        assert 0 <= r and r <= self.n
        assert g(self.e)
        if r == 0:
            return 0
        r = r+self.size
        for j in range(self.log,0,-1):
            x = (r-1)>>j
            self.push(x)
        sm=self.e
        while(True):
            while(1<r and ((r%2)==1)):
                r = r >> 1
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
                ansL.append("E")
            else:
                ansL.append(self.d[j])
        return "内部詳細 : "+str(ansL)
    def str3(self):
        ansL=[]
        for j in range(1,self.size):
            ansL.append(self.lz[j])
        return "遅延 : "+str(ansL)

N,Q=MI()
a=LI()
ans=[]
mod=998243353
def operate(a,b):
    x = (a[0]+b[0])%mod
    y = a[1]+b[1]
    return (x,y)
def mapping(f,x):
    a = (f[0]*x[0]+x[1]*f[1])%mod
    b = x[1]
    return (a,b)
def composition(f,g):
    x = (f[0]*g[0])%mod
    y = (g[1]*f[0]+f[1])%mod
    return (x,y)

G=lazy_segtree([(j,1) for j in a],operate,(0,0),mapping,composition,(1,0))
for j in range(0,Q):
    seq=tuple(MI())
    if seq[0]==0:
        dummy,l,r,b,c=seq
        G.apply(l,r,(b,c))
        xdebug(f"{l}から{r-1}までのapply({b}x+{c})の後")
        xdebug(G)
        xdebug(G.str2())
        xdebug(G.str3())
    else:
        dummy,l,r=seq
        x = G.prod(l,r)
        xdebug(f"{l}から{r-1}までのprod全部足しの後")
        xdebug(G)
        xdebug(G.str2())
        xdebug(G.str3())
        ans.append(x[0])

for line in ans:
    print(line)
