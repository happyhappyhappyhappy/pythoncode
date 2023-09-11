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
        ok = (x==y)
        if ok:
            return
        if self.parents[y]<self.parents[x]:
            x,y=y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        ans = (-1)*self.parents[self.find(x)]
        return ans
    def same(self,x,y):
        x = self.find(x)
        y = self.find(y)
        t_or_f = (x == y)
        return t_or_f
    def members(self,x):
        xroot = self.find(x)
        ans = [j for j in range(0,self.n) if self.find(j) == xroot]
        return ans
    def roots(self):
        ans = [j for j,x, in enumerate(self.parents) if x < 0]
        return ans
    def group_count(self):
        rootlist = self.roots()
        return len(rootlist)
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            mroot = self.find(m)
            group_members[mroot].append(m)
        return group_members
    def __str__(self):
        ans = "\n".join(f"{root} : {members}" for root,members in self.all_group_members().items())
        return ans

def solver(N,M,BL,ANSL):
    result = 0
    uf = UnionFind(N)
    incon = (N * (N-1))//2
    for j in reversed(range(0,M)):
        x,y=BL[j]
        # 繋がる前に値を与えておく
        ANSL.append(incon)
        if uf.same(x,y)==False:
            incon = incon - uf.size(x)*uf.size(y)
            uf.union(x,y)
            # xdebug(f"{x} と {y}がくっついたときのつながり")
            # xdebug(uf)
            # xdebug(f"不便さは {incon} になりました")

if __name__ == "__main__":
    N,M = MI()
    BL = []
    ANSL=[]
    for _ in range(0,M):
        f,t=MI()
        BL.append([f-1,t-1])
    solver(N,M,BL,ANSL)
#    print(ANSL)
    for x in reversed(ANSL):
        print(x)
