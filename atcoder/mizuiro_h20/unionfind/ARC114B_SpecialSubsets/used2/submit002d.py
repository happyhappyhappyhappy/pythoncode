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
MOD = 998244353

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
        if self.parents[yroot]<self.parents[xroot]:
            xroot,yroot=yroot,xroot
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        res = (-1)*self.parents[x]
        return res
    def same(self,x,y):
        ok = (self.find(x) == self.find(y))
        return ok
    def members(self,x):
        xroot=self.find(x)
        res = [ j for j in range(0,self.n) if self.find(j) == xroot]
        return res
    def roots(self):
        res = [j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        allgroup=self.roots()
        return len(allgroup)
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            mroot = self.find(m)
            group_members[mroot].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{root} : {member}" for root,member in self.all_group_members().items())
        return res

def pow2(p,n):
    result = 1
    while n > 0:
        if (n & 1) == 1:
            result = (result*p)%MOD
        n = n >> 1
        p = (p*p)%MOD
    return result

N = II()
uf = UnionFind(N)
FL = LI()
# xdebug(FL)
for j in range(0,N):
    uf.union(j,FL[j]-1)
# xdebug(uf)
gc = uf.group_count()
# print(f"グループの数は {gc}です")
x = pow2(2,gc)-1
# print(f"answer={x}")
print(x)
