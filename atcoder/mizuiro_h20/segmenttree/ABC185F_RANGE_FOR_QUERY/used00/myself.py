# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from operator import xor
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
E=0

class SegmentTree():
    n = 0
    node = []
    def __init__(self,V):
        sv = len(V)
        self.n=1
        while self.n < sv:
            self.n=self.n*2
        self.node=[E]*(self.n*2-1)
        for j in range(0,sv):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=xor(self.node[2*j+1],self.node[2*j+2])
    def update(self,pos,X):
        pos=pos+(self.n-1)
        self.node[pos]=xor(self.node[pos],X)
        while 0 < pos:
            pos = (pos-1)>>1
            self.node[pos]=xor(self.node[2*pos+1],self.node[2*pos+2])
    def getxor(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            return E
        if a <= l and r <= b:
            return self.node[k]
        lr_mid=(l+r)>>1
        vr = self.getxor(a,b,2*k+1,l,lr_mid)
        vl = self.getxor(a,b,2*k+2,lr_mid,r)
        return xor(vr,vl)
    def __str__(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.node[j]==E:
                ansL.append("E")
            else:
                ansL.append(self.node[j])
        return str(ansL)

N,Q=MI()
V=LI()
G=SegmentTree(V)
ANSL=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==1:
        dmy,pos,val=query
        pos=pos-1
        G.update(pos,val)
    else:
        dmy,s,t=query
        s=s-1
        t=t-1
        x = G.getxor(s,t+1)
        ANSL.append(x)
for line in ANSL:
    print(line)
