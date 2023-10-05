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

N = II()

def pow2(n,p):
    result = 1
    while 0 < p:
        oddCheck=p&1
        if oddCheck==1:
            result=result*n
        n = n*n
        p = p >> 1
    return result

def isOK(Ns):
    result = False
    NsCount = (Ns*(Ns+1))//2
    if NsCount <= N+1:
        result = True
    return result

def m_bisect(ngd,okd):
    while 1 < abs(ngd-okd):
        mid = (ngd+okd)//2
        if isOK(mid):
            xdebug(f"1,2,...{mid}を一本{N+1}で刻んで作ることはO")
            xdebug(f"もうちょっとOK値を大きくしてみる {okd}->{mid}")
            okd = mid
        else:
            xdebug(f"1,2,...{mid}を一本{N+1}で刻んで作ることはX")
            xdebug(f"もうちょっとNG値を下げてみる {ngd}->{mid}")
            ngd = mid
    xdebug(f"OK値{okd}、NG値{ngd}の境目に来ました")
    return okd

def solver():
    okLog = m_bisect(pow2(10,18)+1,0)
    xdebug(f"まず長さ{N+1}の木を買う-> 1,2 ... {okLog}まで作成する")
    result = 1
    xdebug(f"残りは買ってそのまま使う +{N-okLog}本")
    result = result+(N-okLog)
    return result


if __name__ == "__main__":
    print("{}".format(solver()))
