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

class SegmentTree():
    sz = 0
    n = 1
    e = 0
    node = []
    def __init__(self,V):
        self.sz = len(V)
        while self.n < self.sz:
            self.n=self.n*2
        self.node=[self.e]*(2*self.n-1)
        for j in range(0,self.sz):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.node[2*j+1]+self.node[2*j+2]
    def add(self,pos,x):
        pos = pos+(self.n-1)
        self.node[pos]=self.node[pos]+x
        while 0 < pos:
            pos = (pos-1)//2
            self.node[pos]=self.node[2*pos+1]+self.node[2*pos+2]
    def getsum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            xdebug("getsum初期")
            r = self.n
        if r <= a or b <= l:
            return self.e
        if a <= l and r <= b:
            return self.node[k]
        vl = self.getsum(a,b,2*k+1,l,(l+r)//2)
        vr = self.getsum(a,b,2*k+2,(l+r)//2,r)
        return vl+vr
    def __str__(self):
        retl = []
        for j in range(0,2*self.n-1):
            if self.node[j]==self.e:
                retl.append('E')
            else:
                retl.append(self.node[j])
        return str(retl)

N,Q = MI()
A = [0]*N
G = SegmentTree(A)
ANSL=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dummy,i,x=query
        i= i-1
        # ANSL.append(f"要素 {i} に {x}を加算します")
        G.add(i,x)
        xdebug(G)
    else:
        dummy,s,t=query
        s = s-1
        t = t-1
        # ANSL.append(f"要素 {s}から {t}までの和を求めます")
        # ANSL.append(f"\t SegmentTree.getsum({s},{t+1})")
        x = G.getsum(s,t+1)
        ANSL.append(x)

for line in ANSL:
    print(line)
