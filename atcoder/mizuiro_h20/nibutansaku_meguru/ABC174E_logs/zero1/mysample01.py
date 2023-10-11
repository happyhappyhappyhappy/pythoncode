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

def pow2(p,n):
    result=1
    while 0 < n:
        oddCheck=n&1
        if oddCheck == 1:
            result=result*p
        p=p*p
        n = n>>1
    return result

def is_ok(t):
# TODO: 2023-10-11 19:33:33
    result=True

    return result

def m_bisect(ngd,okd):
    while 1 < abs(okd-ngd):
        mid=(okd+ngd)>>1
        if is_ok(mid):
            okd = mid
        else:
            ngd = mid
    return okd

def solver():
    result = 0
    # algorithm
    result = m_bisect(0,pow(10,10)+1)
    return result


if __name__ == "__main__":
    global N,A
    N = II()
    A = LI()
    print("{}".format(solver()))
