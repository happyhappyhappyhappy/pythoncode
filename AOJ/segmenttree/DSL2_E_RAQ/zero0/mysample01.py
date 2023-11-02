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
    n = 0
    node = []
    def __init__(self,V):
        sz = len(V)
        self.n=1
        while self.n < sz:
            self.n=self.n*2
        self.node=[0]*(self.n*2-1)
        for j in range(0,sz):
            self.node[(self.n-1)+j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.node[2*j+1]+self.node[2*j+2]
    def add(self,k,val):
        k = (self.n-1)+k
        self.node[k]=self.node[k]+val
        while 0 < k:
            k = (k-1)//2
            self.node[k]=self.node[2*k+1]+self.node[2*k+2]
    def get(self,k):
        k = k + (self.n-1)
        return self.node[k]
N,Q = MI()
V = [0]*N
ansL=[]
G = SegmentTree(V)
for j in range(0,Q):
    query=tuple(MI())
    if query[0] == 0:
        dmy,s,t,x=query
        s = s-1
        t = t-1
        for j in range(s,t+1,1):
            G.add(j,x)
    else:
        dmy,j = query
        j = j - 1
        x = G.get(j)
        ansL.append(x)
for line in ansL:
    print(line)
