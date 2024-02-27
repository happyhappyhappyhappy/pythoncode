# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from string import ascii_lowercase
# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import getLogger, StreamHandler, DEBUG


# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
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
xdebug = logger.debug
ppp = pp.pprint
# Const
MAXSIZE = (1 << 59) - 1
MINSIZE = -(1 << 59) + 1


def solver(N, S, Q):
    result = 0
    xdebug(f"{N= },{S= },{Q= }")
    # algorithm
    fromstr = ascii_lowercase
    tostr = ascii_lowercase
    for _ in range(0, Q):
        a, b = input().strip().split()
        tostr = tostr.replace(a, b)
    xdebug(f"{fromstr=},{tostr=}")
    return result


if __name__ == "__main__":
    x = ascii_lowercase
    N = II()
    S = SI()
    Q = II()
    print("{}".format(solver(N, S, Q)))
