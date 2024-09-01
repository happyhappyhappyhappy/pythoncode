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

def solver():
    result = 0
    # algorithm
    N=II()
    L=[]
    R=[]
    for _ in range(N):
        INL=list(input().rstrip().split(" "))
        V=int(INL[0])
        P=INL[1]
        if P == "L":
            L.append(V)
        else:
            R.append(V)
    lenL=len(L)
    lenR=len(R)
    T=0
    if lenL in (0,1):
        T=T+0
    else:
        for j in range(lenL-1):
            T=T+abs(L[j]-L[j+1])
    if lenR in (0,1):
        T=T+0
    else:
        for j in range(lenR-1):
            T=T+abs(R[j]-R[j+1])
    result=T
    return result


if __name__ == "__main__":
    print(solver())
