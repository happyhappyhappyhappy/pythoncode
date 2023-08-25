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
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.parents[x] > self.parents[y]:
            x,y=y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        return -self.parents[self.find(x)]
    def same(self,x,y):
        return self.find(x)==self.find(y)
    def roots(self):
        return [j for j,x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for member in range(0,self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        return '\n'.join(f'{r} : {m}' for r,m in self.all_group_members().items())
N,M = MI()
uf = UnionFind(N)
L = [[0,0] for _ in range(0,M)]
for j in range(0,M):
    a,b=MI()
    a=a-1
    b=b-1
    L[j][0],L[j][1]=a,b
# for j in range(0,M):
#     xdebug(f'{L[j][0]} {L[j][1]}')
# xdebug('---- Start ----')
# xdebug(uf)
# for j in range(0,M):
#     xdebug(f'---- {j+1} bridge connect ----')
#     uf.union(L[j][0],L[j][1])
#     xdebug(uf)
fuben = (N*(N-1))//2
ans = [0]*M
for j in reversed(range(0,M)):
    ans[j]=fuben
    ok = uf.same(L[j][0],L[j][1])
    if ok == False:
        fuben = fuben - uf.size(L[j][0])*uf.size(L[j][1])
    uf.union(L[j][0],L[j][1])
    # xdebug(f"--BridgeNo.{j} is alive--")
    # xdebug(uf)

for j in range(0,M):
    print(ans[j])
