# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import defaultdict
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
# xdebug=logger.debug
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
            self.parents[x]=self.find(self.find(self.parents[x]))
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[y]<self.parents[x]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        res = (-1)*(self.parents[self.find(x)])
        return res
    def same(self,x,y):
        ok = (self.find(x)==self.find(y))
        return ok
    def members(self,x):
        root = self.find(x)
        reslist=[j for j in range(0,self.n) if self.find(j)==root]
        return reslist
    def roots(self):
        reslist=[j for j,x in enumerate(self.parents) if x < 0]
        return reslist
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            group_members[self.find(m)].append(m)
        return group_members
    def __str__(self):
        resStr="\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
        return resStr


N,M,K=MI()
uf=UnionFind(N)
# 直接の友好関係にある数
FRIEND=[0]*N
for _ in range(0,M):
    araw,braw=MI()
    # 0-index
    a=araw-1
    b=braw-1
    uf.union(a,b)
    FRIEND[a]=FRIEND[a]+1
    FRIEND[b]=FRIEND[b]+1
BLOCK=[0]*N # 直接攻撃態勢をとる人の数
for _ in range(0,K):
    craw,draw=MI()
    c=craw-1
    d=draw-1
    if uf.same(c,d):
        BLOCK[c]=BLOCK[c]+1
        BLOCK[d]=BLOCK[d]+1
    # else:
    #     xdebug(f"{craw}と{draw}は同じグループには無いので処理しない")
ANSLIST=[]
# xdebug("---解法開始---")
for j in range(0,N):
    pat1 = uf.size(j)
#    xdebug(f"{j+1}が関わるグループの構成人数は {pat1} 人")
    pat2 = FRIEND[j]
#    xdebug(f"このうち {j+1}が直接友好関係にある人で {pat2} 人マイナス")
    pat3 = BLOCK[j]
#    xdebug(f"このうち {j+1}が直接攻撃態勢にある人で {pat3} 人マイナス")
#    xdebug(f"あと{j+1}本人そのものは含めない -1 人")
    allpat = pat1-pat2-pat3-1
#    xdebug(f"結果 {j+1}の友達候補になる人は {allpat}人")
    ANSLIST.append(str(allpat))
res=" ".join(ANSLIST)
print(res)
