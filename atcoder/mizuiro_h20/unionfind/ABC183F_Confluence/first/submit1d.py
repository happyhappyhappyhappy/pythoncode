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
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    # TODO:

N,Q = MI()
CList = LI()
CCL=[]
for j in range(0,N):
    c = Counter([CList[j]])
    CCL.append(c)
xdebug(CCL)

for j in range(0,Q):
    p,f,s = MI()
    if p == 1:
        xdebug(f"指示{j+1}-> {f} と {s} の集団に合流しなさい")
    else:
        xdebug(f"指示{j+1}-> {f}のグループ中 クラス {s}の人数を出しなさい")
