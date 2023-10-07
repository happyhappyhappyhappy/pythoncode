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

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents=[-1]*n
    def find(self,x):
        # str2=" ".join(f"{self.parents[j]}" for j in range(0,self.n))
        # xdebug(f"今の親セット {str2}")
        if self.parents[x]<0:
            return x
        else:
            # xdebug(f"self.parents[{x}]={self.parents[x]}>0よりこれの親を取ってきます")
            self.parents[x]=self.find(self.parents[x])
    # def union(self,x,y):
    #     # xdebug(f"{a}と{b}を結合します")
    #     x = self.find(x)
    #     y = self.find(y)
    #     if x == y:
    #         return
    #     str2=" ".join(f"{self.parents[j]}" for j in range(0,self.n))
    #     xdebug(f"今の親セット {str2}")
    #     if self.parents[y] < self.parents[x]:
    #         x,y=y,x
    #     # self.parents[x]=self.parents[x]+self.parents[y]
    #     # self.parents[y]=x
    #     self.parents[x] += self.parents[y]
    #     self.parents[y] = x
    #     return
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self,x):
        res = (-1)*self.parents[self.find(x)]
        return res
    def same(self,x,y):
        xroot  = self.find(x)
        yroot = self.find(y)
        res = (xroot==yroot)
        return res
    def members(self,x):
        xroot = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j) == xroot]
        return res
    def roots(self):
        res = [j for j , x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        res_bef=self.roots()
        return len(res_bef)
    def all_group_members(self):
        group_members = defaultdict(list)
        for j in range(0,self.n):
            jroot = self.find(j)
            group_members[jroot].append(j)
        return group_members
    def __str__(self):
        res = "\n".join(f" {root} : {mem}" for root,mem in self.all_group_members().items() )
        return res
def solver():
    result = 0
    CCL=[]
    uf = UnionFind(N)
    # xdebug("初期状態")
    xdebug(uf)
    for j in range(0,N):
        CCL.append(Counter([CL[j]]))
    for _ in range(0,Q):
        a,b,c = MI()
        xdebug(f"a={a},b={b},c={c}")
        if a == 1:
            b = b-1
            c = c-1
            if not uf.same(b,c):
                uf.union(b,c)
                xdebug(uf)
        #     else:
        #         xdebug(f"{b}と{c}は同じグループのため接続しない")
        # algorithm
    return result

if __name__ == "__main__":
    global N,Q
    N,Q = MI()
    global CL
    CL = LI()
    solver()
