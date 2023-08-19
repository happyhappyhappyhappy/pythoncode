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

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents=[-1]*n
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    ## TODO: ここからスタート 2023-08-19 19:29:49
    ## https://note.nkmk.me/python-union-find/
