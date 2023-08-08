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

# UnionFindクラスの作成
class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents=[-1]*n
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            upparents = self.parents[x]
            self.parents[x]=self.find(upparents)
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
        nowRoot = self.find(x)
        res_size = (-1)*(self.parents[nowRoot])
        return res_size
    def same(self,x,y):
        ok = (self.find(x)==self.find(y))
        return ok
    def members(self,x):
        root = self.find(x)
        return [j for j in range(0,self.n) if self.find(j) == root]
    def roots(self):
        return [j for j,x in enumerate(self.parents)]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(0,self.n):
            memspar=self.find(member)
            group_members[memspar].append(member)
        return group_members
    def __str__(self):
        res="\n".join(f"{r}: {m}" for r,m in self.all_group_members().items())
        return res

N,M = MI()
A = LI()
B = LI()
uf = UnionFind(N)
for j in range(0,M):
    cp1,dp1 = MI()
    c = cp1-1
    d = dp1-1
    uf.union(c,d)
# print(uf)
bList = [0]*N
for j in range(0,N):
    x = uf.find(j)
    diff = A[j]-B[j]
#   xdebug(f" {j}  の  A,Bの差は { diff } これを { x } に反映")
    bList[x]=bList[x]+(A[j]-B[j])
#    xdebug(f" 今のbList[ {x} ] は { bList[x] }")
ok = True
for j in range(0,N):
    if bList[j] != 0:
#        xdebug(f"{ j } のグループで0にならない")
        ok = False
        break
if ok :
    print("Yes")
else :
    print("No")
