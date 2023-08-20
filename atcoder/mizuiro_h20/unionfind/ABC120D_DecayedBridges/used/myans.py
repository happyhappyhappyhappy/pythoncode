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
xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1 for _ in range(0,n)]
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        res = (-1)*(self.parents[x])
        return res
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        ok = (xroot==yroot)
        return ok
    def members(self,x):
        root = self.find(x)
        res = [j for j in range(0,n) if self.find(j)==root]
        return res
    def roots(self):
        res= [j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            group_members[self.find(m)].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{root}: {member}" for root,member in group_members.items())
N,M = map(int,input().split())
print(f"N={N}")
uf = UnionFind(N)
fuben = (N*(N-1))/2 # どの互いの島も行き来できない状態
L = [[0,0] for _ in range(0,M)]
for j in range(0,M):

    # x,y = MI()
    X=sys.stdin.readline()
    xdebug(f"貰った文字列 {X} ")
    x,y = map(int,X.split())
    L[j][0]=x-1
    L[j][1]=y-1
ans = [0 for _ in range(0,N)]
for j in reversed(range(0,M)):
    ans[j] = fuben
    x,y = L[j]
    samePos = uf.same(x,y)
    if samePos == False:
        xc = uf.size(x)
        yc = uf.size(y)
        xdebug(f"{j}番目:{x}<->{y}が落ちていなければ {xc*yc}通りの組み合わせの交流があった")
        fuben = fuben - uf.size(x)*uf.size(y)
        uf.union(x,y)
        xdebug(f"----{j}番目崩落前----")
        xdebug(uf)
        xdebug(f"----{j}番目崩落前----")
    else:
        xdebug(f"{j}番目:{x}<->{y}が落ちても影響は無かった")
for j in range(0,M):
    print(f"{ans[j]}")
