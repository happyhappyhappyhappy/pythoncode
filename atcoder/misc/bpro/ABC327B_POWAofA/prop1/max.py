# ライブラリのインポート
import sys
from printecream import print
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
def mypow(p,n):
    x=1
    while n!=0:
        if n & 1 == 1:
            x = x * p
        n = n >> 1
        p = p * p
    return x
if __name__ == "__main__":

    mnum=mypow(10,18)
    print(mnum)
    maxa = 1
    j = 1
    while mypow(j,j) < mnum:
        print(mypow(j,j))
        maxa = j
        j=j+1
    print(maxa)
