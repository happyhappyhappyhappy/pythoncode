# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
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
E = (1<<31)-1
class LazySegment():
    n = 0
    lazy = []
    lazyFlag = []
    node = []
    def __init__(self,V):
        sv = len(V)
        self.n=1
        while self.n < sv:
            self.n=self.n*2
        self.node=[E]*(self.n*2-1)
        self.lazy=[E]*(self.n*2-1)
        self.lazyFlag=[False]*(self.n*2-1)
        for j in range(0,sv):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=min(self.node[j*2+1],self.node[j*2+2])
    def eval(self,k,l,r):
# TODO: ここから AOJ_DSL2F\04\の解答をコピー
# TODO: 2023-11-18 19:31:00
