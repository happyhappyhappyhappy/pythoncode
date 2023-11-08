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
E = MAXSIZE
class LazySegment():
    n = 0
    node = []
    lazy = []
    lazyFlag = []
    def __init__(self,V):
        sv = len(V)
        self.n=1
        while self.n < sv:
            self.n=self.n*2
        self.node=[E]*(self.n*2-1)
        self.lazy=[0]*(self.n*2-1)
        self.lazyFlag=[False]*(self.n*2-1)
        for j in range(0,sv):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=min(self.node[2*j+1],self.node[2*j+2])
    def eval(self,k,l,r):
        if self.lazyFlag[k]==True:
                self.node[k]=self.node[k]+self.lazy[k]
                if 1 < (r-l):
                    self.lazy[k*2+1]=self.lazy[k*2+1]+(self.lazy[k]>>1)
                    self.lazy[k*2+2]=self.lazy[k*2+2]+(self.lazy[k]>>1)
                self.lazy[k]=0
                self.lazyFlag[k]=False
    def add(self,a,b,val,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.lazy[k]=self.lazy[k]+(r-l)*val
            self.lazyFlag[k]=True
            self.eval(k,l,r)
        else:
            mid = (r+l)>>1
            self.add(a,b,val,k*2+1,l,mid)
            self.add(a,b,val,k*2+2,mid,r)
            self.node[k]=min(self.node[k*2+1],self.node[k*2+2])
    def getMin(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
    # TODO 2023-11-08 19:32:57
    # TODO 最小値を求める所から続き
