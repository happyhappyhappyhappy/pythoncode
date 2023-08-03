# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import defaultdict
# from collections import deque
# pypy3用
import pypyjit
# 再帰制御解放
pypyjit.set_param('max_unroll_recursion=-1')
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
        self.parents = [-1]*n
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            # 経路圧縮
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x,y = y,x # swap
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        pos = self.find(x)
        res = (-1)*self.parents[pos]
        return res
    def same(self,x,y):
        ok = (self.parents[x]==self.parents[y])
        return ok
    def members(self,x):
        root = self.find(x)
        resList = [j for j in range(self.n) if find[j] == root]
        return resList
    def roots(self):
        resList = [j for j,x in enumerate(self.parents) if x < 0]
        return resList
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for mem in range(self.n):
            group_members[self.find(mem)].append(mem)
        return group_members
    def __str__(self):
        res_str='\n'.join(f'{r} : {m}' for r,m in self.all_group_members().items())
        return res_str

N,M = MI()
xdebug(f"N = { N },M = {M}")
uf=UnionFind(N)
# xdebug(uf)
for j in range(0,M):
    x,y = MI()
    uf.union(x-1,y-1)
xdebug(uf)
ans = 0
for j in range(0,N):
    x = uf.size(j)
    xdebug(f"{j} の含むグループの大きさ ->{x}")
    if ans < x:
        ans = x
print(f"答え {ans}")
