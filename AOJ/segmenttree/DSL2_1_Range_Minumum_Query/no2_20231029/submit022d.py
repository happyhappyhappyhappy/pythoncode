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
    n = 1
    e = ((1<<31)-1)
    sz = 0
    node = []
    def __init__(self,V):
        self.sz = len(V)
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
            self.node[x]=min(self.node[2*x+1],self.node[2*x+2])
    def getmin(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            xdebug(f"結果 (r={r} <= a={a} or b={b} <= l={l})")
            xdebug(f"もう a={a} <= l={l} and r={r} <= b={b}からかけ離れる")
            if r <= a:
                xdebug(f"検索の左側aが、調査の右側rに引っかかる")
            if b <= l:
                xdebug(f"検索の左側bが、調査の左側lに引っかかる")
            xdebug(f"単位元を返す")
            return self.e
        if a <= l and r <= b:
            xdebug(f"完全にlとrは被覆されている(a={a} <= l={l} and r={r} <= b={b})")
            xdebug(f"ノード {k} の設定済み {self.node[k]}を返す")
            return self.node[k]
        xdebug(f"??a={a} <= l={l} and r={r} <= b={b}??")
        xdebug(f"Node {k} では まだ {a} と {b} との関係に不安が残る被覆かどうかまだ不明")
        xdebug(f"そこでNode {2*k+1}に下って 左{l} と 右{(l+r)//2}を見ていく")
        vl=self.getmin(a,b,2*k+1,l,(l+r)//2)
        xdebug(f"Node {2*k+2}に下って 左{(l+r)//2} と右 {r} を見ていく")
        vr=self.getmin(a,b,2*k+2,(l+r)//2,r)
        return min(vl,vr)
    def __str__(self):
        ansl=[]
        for j in range(0,2*self.n-1):
            if self.node[j] != self.e:
                ansl.append(self.node[j])
            else:
                ansl.append('E')
        return str(ansl)

N,Q = MI()
A = [((1<<31)-1)]*N
G = SegmentTree(A)
for j in range(0,Q):
    query=tuple(MI())
    if query[0] == 0:
        dum,x,val=query
        G.update(x,val)
        xdebug(f"Gのノード:{G}")
    else:
        dum,s,t=query
        ans=G.getmin(s,t+1)
        print(ans)
