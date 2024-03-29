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
            xparent=self.parents[x]
            self.parents[x]=self.find(xparent)
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
        res = (-1)*(self.parents[self.find(x)])
        return res
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        ok_or_ng = (xroot==yroot)
        return ok_or_ng
    def members(self,x):
        root = self.find(x)
        res = [ j for j in range(0,self.n) if self.find(j)==root]
        return res
    def roots(self):
        res = [ x for x,y in enumerate(self.parents) if y < 0 ]
        return res
    def group_count(self):
        roots = self.roots()
        return len(roots)
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            group_members[self.find(m)].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
        return res

def solver(N,M,K,UF,R,B):
    # xdebug(f"N={N},M={M},K={K}")
    # xdebug(UF)
    # xdebug(f"R={R}")
    # xdebug(f"B={B}")
    ansList = []
    for j in range(0,N):
        X = uf.size(j)
#        xdebug(f" {j+1} 氏の 初期値 {X}")
        X = X-1 # 自分自身
#        xdebug(f"自分をのぞく {X}")
        X = X-R[j] # 実際の友人関係
#        xdebug(f"リアル友人をのぞく {X}")
        X = X-B[j] # グループ内ブロック関係
#        xdebug(f"ブロック関係を除く 完了形 {X}")
        ansList.append(str(X))
    # algorithm
    result = " ".join(ansList)
    # xdebug(f"多分答えは {ansSug}")
    return result


if __name__ == "__main__":
    N,M,K=MI()
    uf = UnionFind(N)
    RealL=[0]*N
    BlockL=[0]*N
    for _ in range(0,M):
        a,b = MI()
        a = a-1
        b = b-1
        uf.union(a,b)
        RealL[a]=RealL[a]+1
        RealL[b]=RealL[b]+1
    for _ in range(0,K):
        c,d = MI()
        c = c-1
        d = d-1
        if uf.same(c,d)==True:
            BlockL[c]=BlockL[c]+1
            BlockL[d]=BlockL[d]+1
    print("{}".format(solver(N,M,K,uf,RealL,BlockL)))
