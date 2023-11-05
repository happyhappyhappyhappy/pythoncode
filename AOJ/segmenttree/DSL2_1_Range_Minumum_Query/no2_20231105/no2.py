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
E = (1<<31)-1
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
            self.node[j]=min(self.node[2*j+1],self.node[2*j+2])
    def update(self,x,val):
        x = x + (self.n-1)
        self.node[x]=val
        while 0 < x:
            x = (x-1)//2
            self.node[x]=min(self.node[2*x+1],self.node[2*x+2])
    def getmin(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            # xdebug(f"枠外突破 : r={r} <= a={a} or b={b} <= l={l}")
            return E
        if a <= l and r <= b:
            # xdebug(f"完全包括 : a={a} <= l={l} and r={r} <= b={b}")
            return self.node[k]
        # xdebug("さらに下をくぐる")
        vl = self.getmin(a,b,2*k+1,l,(r+l)//2)
        vr = self.getmin(a,b,2*k+2,(r+l)//2,r)
        return min(vl,vr)
    def __str__(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.node[j]==E:
                ansL.append("E")
            else:
                ansL.append(self.node[j])
        return str(ansL)
N,Q = MI()
V = [E]*N
G=SegmentTree(V)
ansL=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dmy,j,x=query
        G.update(j,x)
        # xdebug(f"G:{G}")
    else:
        dmy,s,t=query
        x = G.getmin(s,t+1)
        ansL.append(x)
for line in ansL:
    print(line)
