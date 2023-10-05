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

A,B,X=MI()
def isOK(arg):
    # 整数argの値段求める->X以下か
    arg_keta=len(str(arg))
    price=A*arg+B*arg_keta
    if price <= X:
        xdebug(f"整数{arg}の値段{price}は 高橋君が持っている{X}円より安いOK")
        return True
    else:
        xdebug(f"整数{arg}の値段{price}は 高橋君が持っている{X}円より高いNG")
        return False

def m_bisect(okd,ngd):
    while 1 < abs(okd-ngd):
        mid=(okd+ngd)//2
        check=isOK(mid)
        if check==True:
            xdebug(f"今のOK={okd}を{mid}に上昇させてみます")
            okd=mid
        else:
            xdebug(f"今のNG={ngd}を{mid}に下げてみます")
            ngd=mid
    xdebug(f"ループから抜けて NG {ngd},OK {okd}に区別できました")
    return okd

ans=m_bisect(0,10**9+1)
print(ans)
