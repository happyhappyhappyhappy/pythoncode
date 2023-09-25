# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import Counter,defaultdict
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
        xroot = self.find(x)
        yroot = self.find(y)
        if (xroot == yroot) == True:
            return
        if self.parents[yroot] < self.parents[xroot]:
            xroot,yroot=yroot,xroot
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        xroot = self.find(x)
        res = (-1)*self.parents[xroot]
        return res
    def same(self,x,y):
        ok_ng=(self.find(x)==self.find(y))
        return ok_ng
    def members(self,x):
        xroot = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j)==xroot]
        return res
    def roots(self):
        res = [j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        lis = self.roots()
        return len(lis)
    def all_group_members(self):
        group_members=defaultdict(list)
        for j in range(0,self.n):
            jroot = self.find(j)
            group_members[jroot].append(j)
        return group_members
    def __str__(self):
        res = "\n".join(f"{root} : {members}" for root,members in self.all_group_members().items())
        return res

N,Q = MI()
CList = LI()
CCL=[]
for j in range(0,N):
    c = Counter([CList[j]])
    CCL.append(c)

uf = UnionFind(N)

for j in range(0,Q):
    p,f,s = MI()
    if p == 1:
        f = f-1
        s = s-1
        if uf.same(f,s) == False:
            froot = uf.find(f)
            sroot = uf.find(s)
            if uf.parents[sroot] < uf.parents[froot]:
                froot,sroot = sroot,froot
            CCL[froot].update(CCL[sroot])
            uf.union(froot,sroot)
    else:
        froot = uf.find(f-1)
        print(CCL[froot][s])
