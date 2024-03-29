# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
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

N = II()

def dfs(L):
    if len(L) == N:
        S = ''.join(L)
        print(S)
    else:
        maxChar = max(L)
        for j in range(ord('a'),ord(maxChar)+2):
            xdebug("現在の L->{}".format(L))
            L.append(chr(j))
            xdebug("dfs突入前の L->{}".format(L))
            dfs(L)
            L.pop()
            xdebug("dfs突入後の L->{}".format(L))

dfs(list('a'))
