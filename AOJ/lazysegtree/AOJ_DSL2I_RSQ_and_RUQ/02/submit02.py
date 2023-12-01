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
class LazySegment():
    def __init__(self,n_,fx,fa,fm,fp,ex,em):
        x = 1
        while x < n_:
            x = x*2
        self.n=x
        self.FX=fx # Node同士の演算:加算
        self.FA=fa # lazy->nodeへの伝達:上書き
        self.FM=fm # lazy内の積み立て:上書き
        self.FP=fp # lazy->node時の値の修正: 区間の長さをかける
        self.ex=ex # node初期値: 0
        self.em=em # lazy恒等写像:といってもフラグとして利用
                    # em=(1<<31)-1 False,それ以外 True
        self.node=[ex]*(self.n*2-1)
        self.lazy=[em]*(self.n*2-1)
    def set(self,p,val): # 初期セット
        self.node[(self.n-1)+p]=val
    def build(self):
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.FX(self.node[2*j+1],self.node[2*j+2])
    def eval(self,k,length):
        if self.lazy[k]==self.em:
            return
        if k < self.n-1:
            self.lazy[2*k+1]=self.FM(self.lazy[2*k+1],self.lazy[k])
            self.lazy[2*k+2]=self.FM(self.lazy[2*k+1],self.lazy[k])
        self.node[k]=self.FA(self.node[k],self.FP(self.lazy[k],length))
        self.lazy[k]=self.em
    def update(self,a,b,val,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,r-l)
        if a <= l and r <= b:
            self.lazy[k]=self.FM(self.lazy,val)
            self.eval(k,r-l)
        elif a < r and l < b:
            mid=(r+l)>>1
            self.update(a,b,val,2*k+1,r,mid)
            self.update(a,b,val,2*k+2,mid,r)
            self.node[k]=self.FX(self.node[2*k+1],self.node[2*k+2])
    def getSum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,r-l)
        if r <= a or b <= l:
            return self.ex
        elif a <= l and r <= b:
            return self.node[k]
        else:
            mid = (l+r)>>1
            vl=self.getSum(a,b,2*k+1,l,mid)
            vr=self.getSum(a,b,2*k+2,mid,r)
            return vl+vr
    def __str__(self):
        ans=[]
        for j in range(0,self.n*2-1):
            if self.node[j]==self.ex:
                ans.append("E")
            else:
                ans.append(self.node[j])
        return str(ans)
    def strl(self):
        ans = []
        for j in range(0,self.n*2-1):
            if self.lazy[j]==self.em:
                ans.append("NO")
            else:
                ans.append(self.lazy[j])
        return str(ans)
N,Q=MI()
def fx(a,b):
    return a+b
def fa(n,l):
    return l
def fm(laNow,laNext):
    return laNext
def fp(m,n):
    return m*n
ex=0
em=(1<<31)-1
G=LazySegment(N,fx,fa,fm,fp,ex,em)
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        _,s,t,val=query
        G.update(s,t+1,val)
    else:
        _,s,t=query
        xdebug(f"G->{G}")
        x = G.getSum(s,t+1)
        print(x)
# PENDING::2023-12-01 17:52:06
# 値が正しく反映されない
