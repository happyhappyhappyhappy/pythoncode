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
        if oddn==1:
            res=res*p
        n=n>>1
        p=p*p
    return res

def isOK(arg):
    # arg本作るとなれば少なくとも赤,青1本ずつの消費をする
    R_r=R-arg
    B_r=B-arg
    if (R_r < 0) or (B_r < 0):
        xdebug(f"{arg}束は明らかに作れないNG")
        return False
    total = (R_r // (x-1)) + (B_r // (y-1))
    if arg <= total:
        xdebug(f"何とか 目標{arg}に対して 多い{total}が作れる OK")
        return True
    else:
        xdebug(f"目標{arg}に対して 少ない{total}しか作れない NG")
        return False

def m_bisect(okd,ngd):
    while 1 < abs(okd-ngd):
        mid = (okd+ngd)>>1
        if isOK(mid):
            xdebug(f"{mid}束作れそうなので この値を{okd}から{mid}まで引き上げる")
            okd=mid
        else:
            xdebug(f"{mid}束作るのは無理なので {ngd}を{mid}に下げる")
            ngd=mid
    xdebug(f"OK数 {okd} , NG数 {ngd}の差が1になり境ができました")
    return okd

def solver(in1,in2):
    result = 0
    global R,B,x,y
    R,B=in1[0],in1[1]
    x,y=in2[0],in2[1]
    result = m_bisect(0,pow2(10,18)+1)
    # algorithm
    return result


if __name__ == "__main__":
    input1=tuple(MI())
    input2=tuple(MI())
    print("{}".format(solver(input1,input2)))
