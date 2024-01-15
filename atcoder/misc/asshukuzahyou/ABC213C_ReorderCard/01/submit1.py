# ライブラリのインポート
import sys
import pprint as pp
from bisect import bisect_left
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

H,W,N=MI()
H1=[]
W1=[]
for j in range(0,N):
    h,w=MI()
    H1.append(h)
    W1.append(w)
H2=list(sorted(set(H1)))
W2=list(sorted(set(W1)))
for j in range(0,N):
    x = bisect_left(H2,H1[j])+1
    y = bisect_left(W2,W1[j])+1
    print(f"{x} {y}")
