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
        if self.parents[x] < 0:
            return x
        else :
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            y,x = x,y
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        find_x = self.find(x)
        res = (-1)*(self.parents[find_x])
        return res
    def same(self,x,y):
        return self.find(x)==self.find(y)
    def members(self,x):
        root = self.find(x)
        resL=[j for j in range(self.n) if root==self.find(j)]
        return resL
    def roots(self):
        resL = [j for j,x in enumurate(self.parents) if x < 0]
        return resL
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for mem in range(self.n):
            group_members[self.find(mem)].append(mem)
        return group_members
    def __str__(self):
        resStr = '\n'.join(f'{r} : {m}' for r,m in self.all_group_members().items())
        return resStr

# Answer code
N,M = MI()
uf = UnionFind(N)
for j in range(0,M):
    x,y = MI()
    uf.union(x-1,y-1)
xdebug(uf)
xdebug(uf.parents)
ans = 0
for j in range(0,N):
    x = uf.size(j)
    if ans < x:
        ans = x
print(ans)
# TODO: これのデバッグを消して提出2023-08-03 19:25:41
