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




def solver(Count,Glass,Mag):
    result = "0"
    xdebug(f"全 {Count} 回作業,グラス最大 {Glass},マグ最大 {Mag}")
    # algorithm
    g=0
    m=0
    for _ in range(0,Count):
        if g==Glass:
            g=0
        elif m == 0:
            m=Mag
        else:
            cp = min(G-g,m)
            g=g+cp
            m=m-cp
    result=f"{g} {m}"
    return result


if __name__ == "__main__":
    K,G,M=MI()
    print("{}".format(solver(K,G,M)))
