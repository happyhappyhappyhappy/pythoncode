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
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[y]<self.parents[x]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        res = (-1)*self.parents[self.find(x)]
        return res
    def same(self,x,y):
        ok = (self.find(x)==self.find(y))
        return ok
    def members(self,x):
        root = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j) == root ]
        return res
    def roots(self):
        res = [j for j , x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            group_members[self.find(m)].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r}: {m}" for r,m in self.all_group_members().items())
        return res

N,M,K=MI()
F=[0]*N # 友好リスト
B=[0]*N # ブロックリスト
uf = UnionFind(N)
for _ in range(0,M):
    AR,BR = MI()
    a = AR-1
    b = BR-1
    F[a]=F[a]+1
    F[b]=F[b]+1
    uf.union(a,b)
for _ in range(0,K):
    CR,DR = MI()
    c = CR-1
    d = DR-1
    if uf.same(c,d):
        B[c]=B[c]+1
        B[d]=B[d]+1
ANS_L = []
for j in range(0,N):
    xdebug(f"人 {j+1} について")
    xdebug(f"この人の所属するグループの数は {uf.size(j)} 人 ")
    xdebug(f"友好関係にある人は {F[j]} 人")
    xdebug(f"グループは同じだがブロックしている人は {B[j]} 人")
    ans = uf.size(j)-1-F[j]-B[j]
    ANS_L.append(ans)
#    print(ans)
ANS_L_STR=" ".join(list(map(str,ANS_L)))
print(ANS_L_STR)
