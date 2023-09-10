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
        else :
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if (xroot == yroot) == True:
            return
        if self.parents[yroot]<self.parents[xroot]:
            xroot,yroot = yroot,xroot
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        res = self.parents[self.find(x)]
        return (-1)*res
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        return (xroot == yroot)
    def members(self,x):
        xroot = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j) == xroot]
        return res
    def roots(self):
        res = [j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        roots = self.roots()
        return len(roots)
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            mroot = self.find(m)
            group_members[mroot].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f" {root} : {member} " for root,member in self.all_group_members().items())
        return res
# N:人数 Q:指示された合流処理数＋質問数の和
N,Q = MI()
# 各人の所属クラス
C = LI()
# CCL各人の合流値
CCL = []
# 初期値をセット
for j in range(0,N):
    c=Counter([C[j]])
    CCL.append(c)
uf = UnionFind(N)
for j in range(0,Q):
    q,a,b=MI()
    if q == 1:
        a = a-1
        b = b-1
        if uf.same(a,b) == False:
            aroot = uf.find(a)
            broot = uf.find(b)
            if uf.parents[broot] < uf.parents[aroot]:
                aroot,broot = broot,aroot
            # 結合処理
            CCL[aroot].update(CCL[broot])
            xdebug(f"現在の集合{CCL}")
            uf.union(aroot,broot)
    else:
        xdebug(f"Q={q},A={a},B={b}")
        xdebug(f"{a-1}の属する集団にクラス{b}がある人数")
        xdebug(CCL[a-1])
        print(CCL[a-1][b])
