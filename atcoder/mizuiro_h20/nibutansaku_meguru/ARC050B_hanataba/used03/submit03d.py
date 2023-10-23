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
        oddn = n & 1
        if oddn ==1:
            res=res*p
        n = n >> 1
        p = p * p
    return res
def isOK(arg):
    R_=R-arg
    B_=B-arg
    if R_ < 0 or B_ < 0:
#        xdebug(f"{arg}束作るには花束が足りません")
        return False
    total = ((R_)//(x-1))+((B_)//(y-1))
    if arg <= total:
#        xdebug(f"残った花で作成{total}束->{arg}束作成OK")
        return True
    else:
#        xdebug(f"残った花で作成{total}束->{arg}束作成NG")
        return False
def m_bisect(okd,ngd):
    while 1 < abs(okd-ngd):
        mid = (okd+ngd)>>1
        if isOK(mid)==True:
            okd = mid
        else:
            ngd = mid
#    xdebug(f"OK値 {okd} と NG値 {ngd}の間隔が1に狭まりました")
    return okd

def solver(in1,in2):
    result = 0
    global R,B,x,y
    R=in1[0]
    B=in1[1]
    x=in2[0]
    y=in2[1]
    result = m_bisect(0,pow2(10,18)+1)
    # algorithm
    return result


if __name__ == "__main__":
    in1 = tuple(MI())
    in2 = tuple(MI())
    print("{}".format(solver(in1,in2)))
