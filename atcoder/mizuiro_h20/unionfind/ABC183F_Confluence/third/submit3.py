# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import Counter,defaultdict
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

class UnionFind:
    n = 0
    parents = []
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
    def find(self,x):
        if self.parents[x]<0:
            return x
        self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.parents[yroot] < self.parents[xroot]:
            xroot,yroot = yroot,xroot
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        xroot = self.find(x)
        ret = (-1)*self.parents[xroot]
        return ret
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        check = (xroot == yroot)
        if check == True:
            return True
        else:
            return False
    def members(self,x):
        xroot = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j) == xroot]
        return res
    def roots(self):
        res = [ j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        cnt = len(self.roots())
        return cnt
    def all_group_members(self):
        group_members=defaultdict(list)
        for j in range(0,self.n):
            jroot = self.find(j)
            group_members[jroot].append(j)
        return group_members
    def __str__(self):
        gm = self.all_group_members()
        ret = "\n".join(f" {r} : {m}" for r,m in gm.items())
        return ret

N,Q=MI()
CL=LI()
CLL=[]
uf = UnionFind(N)
for j in range(0,N):
    c = Counter([CL[j]])
    CLL.append(c)
# xdebug(f"CLL={CLL}")
for j in range(0,Q):
    t,x,y = MI()
    if t == 1:
        a = x-1
        b = y-1
        if uf.same(a,b) == False:
            aroot = uf.find(a)
            broot = uf.find(b)
            if uf.parents[broot] < uf.parents[aroot]:
                aroot,broot = broot,aroot
            CLL[aroot].update(CLL[broot])
            uf.union(aroot,broot)
            # xdebug(f"Q {j+1}-> CLL={CLL}")
            # xdebug(uf)
    else :
        x = x-1
        xleader = uf.find(x)
        print(CLL[xleader][y])
