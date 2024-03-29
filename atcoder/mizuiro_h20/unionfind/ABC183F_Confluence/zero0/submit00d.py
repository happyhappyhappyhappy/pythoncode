# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import defaultdict,Counter
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
        if x==y:
            return
        if self.parents[y]<self.parents[x]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        res = (-1)*self.parents[self.find(x)]
        return res
    def same(self,x,y):
        t_or_f=(self.find(x)==self.find(y))
        return t_or_f
    def members(self,x):
        xroot = self.find(x)
        res = [ j for j in range(0,self.n) if self.find(j)==xroot]
        return res
    def roots(self):
        res = [ j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            mroot = self.find(m)
            group_members[mroot].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{root}:{member}" for root,member in self.all_group_members().items())
        return res

N,Q = MI()
C = LI()
CCL = []
for j in range(0,N):
    c = Counter([C[j]])
    CCL.append(c)
uf = UnionFind(N)
# xdebug(f"CCL={CCL}")
for _ in range(0,Q):
    q,a,b=MI()
    if q==1:
#        xdebug(f"{a}と{b}を結合する")
        a=a-1
        b=b-1
        if uf.same(a,b)==False:
            a = uf.find(a)
            b = uf.find(b)
            if uf.parents[b]<uf.parents[a]:
                a,b = b,a
            uf.union(a,b)
#            xdebug(f"----{a}と{b}がくっついた時のUnionFind----")
#            xdebug(uf)
#           xdebug(f"{a}と{b}のメンバー情報統合")
            CCL[a].update(CCL[b])
#            xdebug(CCL)
#        else:
#            xdebug("もう結合済みなので何も実行せず")
    else:
        aroot = uf.find(a-1)
#        xdebug(f"人 {a}が中にいる集合でクラス{b}が何人いるか確認する")
#        xdebug(f"答え {CCL[aroot][b]}")
        print(CCL[aroot][b])
