# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
from collection import defaultdict
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
        x = self.find(x)
        y = self.find(y)
        ok = (x==y)
        if ok == true:
            return
        if self.parents[y]<self.parents[x]:
            x,y=y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
        return
    def size(self,x):
        ans = (-1)*self.parents[self.find(x)]
        return ans
    def same(self,x,y):
        x = self.find(x)
        y = self.find(y)
        ok == (x==y)
        return ok
    def members(self,x):
        xroot = self.find(x)
        ans = [j for j in range(0,self.n) if self.find(j)==xroot]
        return ans
    def roots(self):
        ans = [j for j,x in enumerate(parents) if x < 0]
        return ans
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            mroot = self.find(m)
            group_members[mroot].append(m)
        return group_members
    def __str__(self):
        ans = "\n".join(f"{r} : {m}" for r,m in self.all_group_members.items())
        return ans
# TODO:  本文実装から
