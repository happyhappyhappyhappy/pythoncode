# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import DEBUG, StreamHandler, getLogger

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number:int): return [LI() for _ in range(rows_number)]

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

def pow2(P:int,N:int)->int:
    res=1
    while 0 < N:
        nand1=N & 1
        if nand1 == 1:
            res=res*P
        P=P*P
        N=N>>1
    return res

def solver():
    res = 0
    # algorithm
    N,M=MI()
    THISMAX=pow2(10,9)
    for j in range(M+1):
        x=pow2(N,j)
        res=res+x
        if THISMAX < res:
            return "inf"
    return res


if __name__ == "__main__":
    print(solver())
