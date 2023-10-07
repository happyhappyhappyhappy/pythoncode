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
        if (xroot == yroot) == True:
            return
        if self.parents[yroot]<self.parents[xroot]:
            tmp = xroot
            xroot = yroot
            yroot = tmp
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        xroot = self.find(x)
        res = (-1)*self.parents[xroot]
        return res
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
        res = len(self.roots())
        return res
    def all_group_members(self):
        group_members=defaultdict(list)
        for x in range(0,self.n):
            xroot = self.find(x)
            group_members[xroot].append(x)
        return group_members
    def __str__(self):
        gm = self.all_group_members()
        res = "\n".join(f"{r}: {m}" for r,m in gm.items())
        return res

def solver():
    CCL=[]
    uf = UnionFind(N)
    # xdebug("初期状態")
    # xdebug(uf)
    for j in range(0,N):
        CCL.append(Counter([CL[j]]))
    for _ in range(0,Q):
        a,b,c = MI()
        # xdebug(f"a={a},b={b},c={c}")
        if a == 1:
            b = b-1
            c = c-1
            if not uf.same(b,c):
                bleader = uf.find(b)
                cleader = uf.find(c)
                if uf.parents[cleader] < uf.parents[bleader]:
                    bleader,cleader = cleader,bleader
                CCL[bleader].update(CCL[cleader])
                uf.union(bleader,cleader)
        else:
            b=b-1
            bleader=uf.find(b)
            print(CCL[bleader][c])
if __name__ == "__main__":
    global N,Q
    N,Q = MI()
    global CL
    CL = LI()
    solver()
