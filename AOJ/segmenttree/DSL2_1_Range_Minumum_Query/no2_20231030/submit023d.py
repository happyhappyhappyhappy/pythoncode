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
INF = (1<<31)-1

class SegmentTree():
    n = 1
    e = INF
    sz = 0
    node = []
    def __init__(self,V):
        self.sz=len(V)
        while self.n < self.sz:
            self.n=self.n*2
        self.node = [self.e]*(2*self.n-1)
        for j in range(0,self.sz):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=min(self.node[j*2+1],self.node[j*2+2])
    def update(self,x,val):
        x = x + (self.n-1)
        self.node[x]=val
        while 0 < x:
            x = (x-1)//2
            self.node[x]=min(self.node[x*2+1],self.node[x*2+2])
    def getmin(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
        # pat1. l r<->a b
        # pat2. a b<->l r
            return self.e
        if a <= l and r <= b:
        # pat1. a l r b
            return self.node[k]
        vl = self.getmin(a,b,2*k+1,l,(l+r)//2)
        vr = self.getmin(a,b,2*k+2,(l+r)//2,r)
        return min(vl,vr)
    def __str__(self):
        resultL=[]
        for j in range(0,2*self.n-1):
            if self.node[j]==self.e:
                resultL.append('E')
            else:
                resultL.append(self.node[j])
        return str(resultL)

N,Q=MI()
A = [INF]*N
G=SegmentTree(A)
ANSL = []
for j in range(0,Q):
    query = tuple(MI())
    if query[0]==0:
        dum,pos,x=query
        G.update(pos,x)
    else:
        dum,frm,to=query
        # ANSL.append(f"{frm} から {to}までの最小値を求める")
        x = G.getmin(frm,to+1)
        ANSL.append(x)

for line in ANSL:
    print(line)
