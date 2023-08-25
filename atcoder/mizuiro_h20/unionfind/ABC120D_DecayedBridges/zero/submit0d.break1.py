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
xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1
# UnionFindクラス
# class UnionFind():
#     def __init__(self,n):
#         self.n=n
#         self.parents=[-1 for _ in range(0,self.n)]
#     def find(self,x):
#         if self.parents[x]<0:
#             return x
#         else:
#             self.parents[x]=self.find(self.parents[x])
#             return self.parents[x]
#         def union(self,x,y):
#             x = self.find(x)
#             y = self.find(y)
#             ok = (x==y)
#             if ok:
#                 return
#             if self.parents[y] < self.parents[x]:
#                 x,y=y,x
#             self.parents[x]=self.parents[x]+self.parents[y]
#             self.parents[y]=x
#         def size(self,x):
#             res = (-1)*(self.parents[self.find(x)])
#             return res
#         def test(self,x,y):
#             x = self.find(x)
#             y = self.find(y)
#             ok = (x==y)
#             return ok
#         def members(self,x):
#             root = self.find(x)
#             res = [j for j in range(0,self.n) if self.find(j)==root]
#             return res
#         def roots(self):
#             res = [j for j,x in enumerate(self.parents) if x < 0]
#             return res
#         def group_count(self):
#             res = len(self.roots())
#             return res
#         def all_group_members(self):
#             group_members=defaultdict(list)
#             for m in range(0,self.n):
#                 group_members[self.find(m)].append(m)
#             return group_members
#         def __str__(self):
#             res = "\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
#             return res
# 2023-08-24 19:34:18 UnionFindをもう少し丁寧に書写
N,M = MI()
L = [[0,0] for _ in range(0,M)]
for j in range(0,M):
    x,y=MI()
    x=x-1
    y=y-1
    L[j][0]=x
    L[j][1]=y
# xdebug(f"N= { N } , M= { M }")
# for j in reversed(range(0,M)):
#     xdebug(f"{ j }-> [{L[j][0]},{L[j][1]}]")

uf = UnionFind(N)
print(uf)
fuben = (N * (N-1))//2
ans = [0 for _ in range(0,M)]
for j in reversed(range(0,M)):
    ans[j]=fuben
    ok = uf.test(L[j][0],L[j][1])
    if ok == False:
        fsize = uf.size(L[j][0])
        tsize = uf.size(L[j][1])
        fuben=fuben-fsize*tsize
    uf.union(L[j][0],L[j][1])
for x in range(0,M):
    print(f"{ans[x]}\n")
