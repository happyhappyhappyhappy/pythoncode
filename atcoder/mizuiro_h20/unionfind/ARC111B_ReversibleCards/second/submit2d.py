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

# UnionFind Class
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
        if xroot == yroot:
            return
        if self.parents[yroot] < self.parents[xroot]:
            xroot,yroot=yroot,xroot
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        xroot = self.find(x)
        res = (-1)*self.parents[xroot]
        return res
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return True
        else:
            return False
    def members(self,x):
        xroot = self.find(x)
        res = [ j for j in range(0,self.n) if self.find(j) == xroot ]
        return res
    def roots(self):
        res = [ j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        root_cnt = self.roots()
        return len(root_cnt)
    def all_group_members(self):
        group_members=defaultdict(list)
        for j in range(0,self.n):
            jroot = self.find(j)
            group_members[jroot].append(j)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r}:{m}" for r,m in self.all_group_members().items())
        return res

# Edge Count
# MAXCOLOR=200
MAXCOLOR=400001
ECNT=[0 for _ in range(0,MAXCOLOR)]

N = II()
uf = UnionFind(MAXCOLOR)
for _ in range(0,N):
    at,bt = MI()
    a = at-1
    b = bt-1
    ECNT[a]=ECNT[a]+1
    ECNT[b]=ECNT[b]+1
    uf.union(a,b)
# xdebug(uf)
counter = 1
ans = 0
for groups in uf.all_group_members().values():
#    xdebug(f"{counter}->{groups}")
    counter=counter+1
    edge = 0
    gplen = len(groups)
    for gp in groups:
        edge=edge+ECNT[gp]
    checkEdge = 2*(gplen-1)
    if edge == checkEdge:
        # xdebug(f"{groups}は木になっている {gplen-1}個点灯する")
        ans = ans + (gplen-1)
    else:
        # xdebug(f"{groups}は木になっていない {gplen}個点灯する")
        ans = ans + gplen
print(ans)
