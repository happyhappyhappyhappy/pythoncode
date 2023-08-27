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
            xvalue = self.parents[x]
            xroot = self.find(xvalue)
            self.parents[x]=xroot
            return xroot
    def union(self,x,y):
        # x->xroot,y->yrootに替えてある
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.parents[yroot]<self.parents[xroot]:
            xroot,yroot = yroot,xroot
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
    def size(self,x):
        root = self.find(x)
        res = (-1)*self.parents[root]
        return res
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        ok = (xroot == yroot)
        return ok
    def members(self,x):
        root = self.find(x)
        res = [ j for j in range(0,self.n) if self.find(j) == root ]
        return res
    def roots(self):
        res = [ x for x,p in enumerate(self.parents) if p < 0]
        return res
    def group_count(self):
        x = self.roots()
        return len(x)
    def all_group_members(self):
        group_members=defaultdict(list)
        for member in range(0,self.n):
            mroot = self.find(member)
            group_members[mroot].append(member)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
        return res
# 確認用
uf = UnionFind(7)
xdebug("-----")
xdebug(uf)
uf.union(2,3)
xdebug("-----")
xdebug(uf)
uf.union(2,4)
xdebug("-----")
xdebug(uf)
uf.union(3,4)
xdebug("-----")
xdebug(uf)
x=3
xdebug(f"uf.find({x})={uf.find(x)}")
