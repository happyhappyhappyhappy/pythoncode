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
            sp = self.parents[x]
            self.parents[x] = self.find(sp)
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            xdebug(f" y親 < x親 なので x = { x } と y = { y }交換")
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        res = (-1)*self.parents[x]
        return res
    def same(self,x,y):
        xf = self.find(x)
        yf = self.find(y)
        return xf == yf
    def members(self,x):
        root = self.find(x)
        ml = [j for j in range(0,self.n) if self.find(j)==root]
        return ml
    def roots(self):
        rl = [j for j,x in enumerate(self.parents) if x < 0]
        return rl
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for member in range(0,self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
        return res
N,M = MI()
uf=UnionFind(N)
for _ in range(0,M):
    Q,F,T = MI()
    if Q == 0:
        xdebug(f" { F } と { T } を結合する")
        uf.union(F,T)
        xdebug(uf)
    if Q == 1:
        xdebug(f" { F } と { T } が同じグループか調べる")
        if uf.same(F,T):
            xdebug(f" { F } == { T } OK")
            print("1")
        else:
            xdebug(f" { F } != { T } ")
            print("0")
