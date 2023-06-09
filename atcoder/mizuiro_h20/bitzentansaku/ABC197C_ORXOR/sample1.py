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

# https://atcoder.jp/contests/abc197/submissions/21295839
# そのまま-> mainを用いない物 TODO:続き
# 2023-06-08 19:33:07

N = int(input())
A=list(map(int,input().split()))
ANS = MAXSIZE
def f(m1,m2,i):
    global ANS
    if i==N:
        ANS=min(ANS,c^x)
    else:
        xdebug("A[{}]")
        f(A[i],c^x,i+1)
        f(c|A[i],x,i+1)

# ここにあれこれ書く
f(0,0,0)
print(ANS)
