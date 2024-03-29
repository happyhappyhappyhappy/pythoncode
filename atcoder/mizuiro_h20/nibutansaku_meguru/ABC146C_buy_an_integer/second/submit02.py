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
    res=1
    while 0 < n:
        oddn=n&1
        if oddn == 1:
            res=p*res
        n=n>>1
        p=p*p
    return res

def isOK(N):
    nleng=len(str(N))
    total = A*N+B*nleng
#    xdebug(f"手持ちのお金 {X} と {N}を買うのに必要なお金 {total} を照合します")
    if total <= X:
#        xdebug(f"\t結果->OK")
        return True
    else:
#        xdebug(f"\t結果->NG")
        return False

def m_bisect(okd,ngd):
    while 1 < abs(ngd-okd):
        mid = (ngd+okd)>>1
        if isOK(mid)==True:
            okd = mid
        else:
            ngd=mid
#    xdebug(f"OK値 {okd} と NG値 {ngd}の差が1になりました。終了")
    return okd

def solver(dat):
    result = 0
    global A,B,X
    A = dat[0]
    B = dat[1]
    X = dat[2]
    result = m_bisect(0,pow2(10,9)+1)
    # algorithm
    return result


if __name__ == "__main__":
    inpt=tuple(MI())
    print("{}".format(solver(inpt)))
