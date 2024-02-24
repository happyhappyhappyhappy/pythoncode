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
def SI(): return sys.stdin.readline().strip()
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




def solver(S,T):
    result = 0
    N=len(S)
    M=len(T)
    Tsuf=T[:N]
    Tpre=T[M-N:]
    SufQ=(S==Tsuf)
    PreQ=(S==Tpre)
    # xdebug(f"S={S},Tが接頭か{Tsuf},Tが接尾か{Tpre}")
    if SufQ and PreQ:
        result=0
    elif SufQ:
        result=1
    elif PreQ:
        result=2
    else:
        result=3
    # algorithm
    return result


if __name__ == "__main__":
    N,M=MI()
    S=SI()
    T=SI()
    print("{}".format(solver(S,T)))
