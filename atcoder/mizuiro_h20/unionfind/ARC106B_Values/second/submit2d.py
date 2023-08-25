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
        if x == y:
            return
        if self.parents[y]<self.parents[x]:
            x,y=y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
        return
    def size(self,x):
        res = (-1)*self.parents[self.find(x)]
        return res
    def same(self,x,y):
        ok = (self.find(x)==self.find(y))
        return ok
    def members(self,x):
        root = self.find(x)
        res = [j for j in range(0,self.n) if self.parents[j] == root]
        return res
    def roots(self):
        res = [j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for member in range(0,self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        res='\n'.join(f'{r} : {m}' for r,m in self.all_group_members().items())
        return res

def dataView(N,M,A,B,C,D):
    xdebug(f"N={N},M={M}")
    xdebug(f"A={A}")
    xdebug(f"B={B}")
    for j in range(0,M):
        xdebug(f"{C[j]} <-> {D[j]}")

N,M=MI()
A=LI()
B=LI()
C=[]
D=[]
uf=UnionFind(N)
for j in range(0,M):
    x,y=MI()
    x=x-1
    y=y-1
    # この行そのものは利用しない。すぐにUnionFindに入れる
    C.append(x)
    D.append(y)
    uf.union(x,y)
    xdebug(f"---{j+1}---")
    xdebug(uf)

dataView(N,M,A,B,C,D)
# TODO: root毎diffの和を求める配列作成2023-08-25 19:36:04
