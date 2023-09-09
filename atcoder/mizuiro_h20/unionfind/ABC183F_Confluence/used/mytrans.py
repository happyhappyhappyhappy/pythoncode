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
        self.n = n
        self.parents = [-1]*n
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
            x ,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        xroot = self.find(x)
        res = (-1)*self.parents[xroot]
        return res
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        ok = (xroot==yroot)
        return ok
    def members(self,x):
        xroot = self.find(x)
        res = [ j for j in range(0,self.n) if self.find(j) == xroot ]
        return res
    def roots(self):
        res = [ j for j,x in enumerate(self.parents) if x < 0 ]
        return res
    def group_count(self):
        resInf = self.roots()
        return len(resInf)
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            mroot = self.find(m)
            group_members[mroot].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r}:{m} " for r,m in self.all_group_members().items())
        return res

N,Q = MI()
C = LI()
D = []
for j in range(0,N):
    d = defaultdict(int)
    cid=C[j] # クラス名
    d[cid]=1
    D.append(d)
xdebug(f"D=>{D}")
uf = UnionFind(N)
for m in range(0,Q):
    q,a,b = MI()
    if q==1:
        xdebug(f"{a}と{b}合流の為 D[{b-1}]からD[{a-1}]情報移動する")
        a = a-1
        b = b-1
        if uf.same(a,b) == False:
            aroot = uf.find(a)
            broot = uf.find(b)
            if uf.parents[broot] < uf.parents[aroot]:
                aroot,broot = broot,aroot
            for cid,v in D[broot].items():
                D[aroot][cid]=D[aroot][cid]+v
            xdebug(f"D[{aroot}]は{D[aroot]}に変化")
            uf.union(aroot,broot)
            xdebug(f"Q.{m}")
            xdebug(uf)
    else:
        xdebug(f"D[{a-1}]内にあるクラスid{b}の構成人数を出す")
        print(D[a-1][b])
