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
A,B,X = MI()

def pow2(p,n):
    result = 1
    while 0 < n:
        isodd = n & 1
        if isodd == 1:
            result=result*p
        p=p*p
        n = n >> 1
    return result

def isOK(arg):
    result = False
    arg_len=len(str(arg))
    arg_price=A*arg+B*arg_len
    # xdebug(f"整数「{arg}」の値段は {arg_price}円です")
    if arg_price <= X:
        # xdebug(f"所持金{X}円で買えます")
        result = True
    # else:
    #    xdebug(f"所持金「{X}」では買えません")
    return result

def m_bisect(ngd,okd):
    # 二分探索メインアルゴリズム
    while 1 < abs(ngd-okd):
        mid = (ngd+okd)>>1
        if isOK(mid):
            # xdebug(f"OK値を{okd}->{mid}に上げてみます")
            okd = mid
        else:
            # xdebug(f"NG値を{ngd}->{mid}に下げてみます")
            ngd=mid
    # xdebug(f"OK値 {okd},NG値 {ngd}と境目が決まりました")
    return okd

def solver():
    maxPos = pow2(10,9)+1
    result = m_bisect(pow2(10,9)+1,0)
    return result


if __name__ == "__main__":
    print("{}".format(solver()))
