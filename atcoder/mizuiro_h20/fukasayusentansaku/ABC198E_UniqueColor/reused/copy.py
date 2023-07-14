# ライブラリのインポート
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
# import heapq,copy
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
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

N = int(input())
C = [0] + list(map(int,input().split()))
L = [[] for _ in range(0,N+1)]
for j in range(0,N-1):
    a,b = map(int,input().split())
    L[a].append(b)
    L[b].append(a)

ANS = [True for _ in range(0,N+1)]

for x in range(0,N+1):
    xdebug("{} -> {}".format(x,L[x]))
# TODO: ロジックへ 2023-07-14 19:37:13
