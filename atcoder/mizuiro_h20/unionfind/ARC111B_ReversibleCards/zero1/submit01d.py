# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import deque,defaultdict
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
        if xroot==yroot:
            return
        if self.parents[yroot]<self.parents[xroot]:
            xroot,yroot = yroot,xroot
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        xroot = self.find(x)
        res = (-1)*self.parents[xroot]
        return res
    def same(self,x,y):
        ok = ( self.find(x) == self.find(y) )
        return ok
    def members(self,x):
        xroot = self.find(x)
        res = [ j for j in range(0,self.n) if self.parents[j] == xroot ]
        return res
    def roots(self):
        res = [ j for j,x in enumerate(self.parents) if x < 0 ]
        return res
    def group_count(self):
        res = len(self.roots())
        return res
    def all_group_members(self):
        group_members=defaultdict(list)
        for x in range(0,self.n):
            xroot = self.find(x)
            group_members[xroot].append(x)
        return group_members
    def __str__(self):
        res = "\n".join(f"{root} : {edge} " for root,edge in self.all_group_members().items())
        return res

N = II()
MAXCOLOR = 400001
# MAXCOLOR = 11
COLLIST=[0]*MAXCOLOR
uf = UnionFind(MAXCOLOR)
for j in range(0,N):
    a,b=MI()
    uf.union(a,b)
    COLLIST[a]=COLLIST[a]+1
    COLLIST[b]=COLLIST[b]+1
ans=0
for grp in uf.all_group_members().values():
    edge=0
    for eg in grp:
        edge=edge+COLLIST[eg]
    gsize = len(grp)
    if (gsize-1)*2 == edge:
        # xdebug(f"{grp}は純粋な木です。従って見える色は{gsize-1}です")
        ans = ans+(gsize-1)
    else:
        # xdebug(f"{grp}は巡回路があります。従って見える色は{gsize}です")
        ans = ans + gsize
print(ans)
