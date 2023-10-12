# ABC174E_logs
# https://atcoder.jp/contests/abc174/tasks/abc174_e
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
    result=True
    cnt = 0
    for a in A:
        cnt=cnt+(((a+t-1)//t)-1)
        # Point1 (X+t-1)//t でXをtで割った時の切り上げを求めている
        # Point2 最後の-1はとりあえずは一旦刃を下ろす->必要が無いときがあることを考慮
    # xdebug(f"長さ[{t}] 条件の回数{K}を、求まった{cnt}で下回るか?")
    result = (cnt <= K)
    # if result==True:
    #     xdebug("OK")
    # else:
    #     xdebug("NG")
    return result

def m_bisect(ngd,okd):
    while 1 < abs(okd-ngd):
        mid=(okd+ngd)>>1
        if is_ok(mid):
            # xdebug(f"{mid}は条件を満たす、okd={okd}から値を下げてみる")
            okd = mid
        else:
            # xdebug(f"{mid}は条件を満たさない、ngd={ngd}から値を上げてみる")
            ngd = mid
    # xdebug(f"OK値{okd} と NG値{ngd}の差が1以下になりました")
    return okd

def solver():
    result = 0
    # algorithm
    result = m_bisect(0,pow(10,10)+1)
    return result


if __name__ == "__main__":
    global N,K
    N,K = MI()
    A = LI()
    print("{}".format(solver()))
