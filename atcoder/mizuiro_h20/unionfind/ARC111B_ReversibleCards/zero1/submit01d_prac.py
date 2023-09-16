# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import defaultdict
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
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if (xroot == yroot):
            return
        if self.parents[yroot]<self.parents[xroot]:
            xroot,yroot = yroot,xroot
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        xroot = self.find(x)
        res = (-1)*(self.parents[xroot])
        return res
    def same(self,x,y):
        ok = (self.find(x)==self.find(y))
        return ok
    def members(self,x):
        xroot = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j)==xroot]
        return res
    def roots(self):
        res = [j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        res = len(self.roots())
        return res
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            mroot = self.find(m)
            group_members[mroot].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
        return res
COLMAX=10
uf = UnionFind(COLMAX)
# TODO: 2023-09-14 19:27:30 ufに設定を保存
Col=[0]*COLMAX
N = II()
for _ in range(0,N):
    a,b = MI()
    a = a-1
    b = b-1
    uf.union(a,b)
    Col[a]=Col[a]+1
    Col[b]=Col[b]+1
xdebug(f"")
xdebug(f"{Col}")
xdebug(uf)
for g in uf.all_group_members().values():
#    xdebug(f"g={g}")
    nowEdge=0
    for k in g:
        nowEdge=nowEdge+Col[k]
    xdebug(f"g={g}->nowEdge={nowEdge}")
    if nowEdge==(len(g)-1):
        x = len(g)-1
        xdebug(f"点灯できるのは{x}個")
    else:
        x = len(g)
        xdebug(f"{g}の時点灯できるのは{x}個")
