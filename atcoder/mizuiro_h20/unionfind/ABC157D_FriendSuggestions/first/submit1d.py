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
        xroot = self.find(x)
        yroot = self.find(y)
        ok = (xroot==yroot)
        if ok:
            return

        if self.parents[yroot]<self.parents[xroot]:
            tmp = xroot
            xroot = yroot
            yroot = tmp
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
        return
    def size(self,x):
        res = (-1)*self.parents[x]
        return res
    def same(self,x,y):
        t_or_f = (self.find(x)==self.find(y))
        return t_or_f
    def members(self,x):
        root = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j) == root]
        return res
    def roots(self):
        res = [ j for j,x in enumurate(self.parents) if x < 0]
        return res
    def group_count(self):
        res = self.roots()
        res2 =  len(res)
        return res2
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            root = self.find(m)
            group_members[root].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
        return res

def solver(N,M,K,Real,Block,UF):
    result = 0
    # xdebug(f"N={N},M={M},K={K}")
    # xdebug(Real)
    # xdebug(Block)
    # algorithm
    # xdebug(UF)
    ans=[]

    for j in range(0,N):
        ExcludeSet = set(Real[j]+Block[j])
        # xdebug(f"{j}番目 除外集合 {ExcludeSet}")
        unionlist = UF.members(j)
        eachans = len(unionlist)-1
        for k in range(0,len(unionlist)):
            if unionlist[k] in ExcludeSet:
                # xdebug(f"人:{unionlist[k]} は {j} にとって除外に入るので候補1減らします")
                eachans = eachans - 1
        ans.append(str(eachans))
    res = " ".join(ans)
    # xdebug(f"回答予定 {res}")
    return res


if __name__ == "__main__":
    N,M,K=MI()
    uf = UnionFind(N)
    Real=[[] for _ in range(0,N)]
    Block=[[] for _ in range(0,N)]
    for _ in range(0,M):
        a,b=MI()
        a=a-1
        b=b-1
        Real[a].append(b)
        Real[b].append(a)
        uf.union(a,b)
    for _ in range(0,K):
        c,d=MI()
        c=c-1
        d=d-1
        Block[c].append(d)
        Block[d].append(c)
    print("{}".format(solver(N,M,K,Real,Block,uf)))
