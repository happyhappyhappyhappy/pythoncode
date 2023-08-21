# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import defaultdict
# pypy3用
import pypyjit
# 再帰制御解放
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
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
# xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

# UnionFindクラス

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
        ok = (x == y)
        if ok:
            return
        if self.parents[y]<self.parents[x]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        return -self.parents[self.find(x)]
    def same(self,x,y):
        ok = (self.find(x)==self.find(y))
        return ok
    def members(self,x):
        root = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j) == root]
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
            group_members[self.find(m)].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{root} : {members}" for root,members in self.all_group_members().items())
        return res

N,M = MI()
L = [[0,0] for j in range(0,M)]
# xdebug(f"N={N},M={M}")
# xdebug(f"L={L}")
for j in range(0,M):
    x,y = MI()
    L[j][0]=x-1
    L[j][1]=y-1
# for j in reversed(range(0,M)):
#    xdebug(f"({L[j][0]},{L[j][1]})")
# 試しに逆順にUnionFindした結果を並べてみる
uf = UnionFind(N)
answer = [0 for _ in range(0,M)]
fuben = (N*(N-1))//2
# for j in reversed(range(0,M)):
#     x,y = L[j]
#     uf.union(x,y)
#     xdebug(f"{j+1}番目の橋が復帰した")
#     xdebug(uf)
for j in reversed(range(0,M)):
    answer[j]=fuben
    x,y = L[j]
# TODO: python atcoderはこのコードのコメントにして提出
# 2023-08-21 19:16:53
    if not uf.same(x,y) :
        xdebug(f"{x}と{y}は行き来できないので橋 {j}をつなげる必要あり")
        xdebug(f"{x} 島のグループ数 {uf.size(x)} , {y} 島のグループ数 {uf.size(y)}")
        fuben = fuben - uf.size(x)*uf.size(y)
        xdebug(f"これで不便度 {fuben} になった")
        uf.union(x,y)
    else:
        xdebug(f"{x}と{y}は行き来できるので橋 {j}をつなげる必要無い")

for j in range(0,M):
    print(answer[j])
