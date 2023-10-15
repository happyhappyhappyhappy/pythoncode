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

R,B = MI()
x,y = MI()

def pow2(p,n):
    ret = 1
    while 0 < n:
        oddn = n & 1
        if oddn == 1:
            ret=ret*p
        p=p*p
        n = n >> 1
    return ret

def isOK(arg):
    # まず基本的に作ろうとした花の起点となる本数は加味する
    B_remain = B - arg
    R_remain = R - arg
    if B_remain < 0 or R_remain < 0:
        # xdebug(f"そもそも{arg}束作る花の数がありません")
        return False
    sumFl = (R_remain // (x-1)) + (B_remain // (y-1))
    if arg <= sumFl:
        # xdebug(f"花束合計{sumFl}に対して作ろうとした{arg}本は満たす")
        return True
    else:
        # xdebug(f"花束合計{sumFl}に対して作ろうとした{arg}本には行かない")
        return False

def m_bisect(ngd,okd):
    while 1 < abs(ngd-okd):
        mid = (ngd+okd)>>1
        if isOK(mid) == True:
            # xdebug(f"中間点{mid}は当てはまる、{okd}を{mid}に増やす")
            okd = mid
        else:
            # xdebug(f"中間値 {mid}は当てはまらない {ngd}を{mid}に下げてみる")
            ngd = mid
    # xdebug(f"OK値 {okd}と NG値 {ngd}の差が1と明確になりました")
    return okd


ans = m_bisect(pow2(10,19),0)
print(ans)
