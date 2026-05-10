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

def sgn(x):
    if x <= -1:
        return -1
    elif 1 <= x:
            return 1
    else:
        return 0

def solver():
    res = 0
    N=II()
    L=LI()
    for j in range(N):
        L[j]*=2
    xdebug(L)
    best=0
    for j in range(1<<N):
        xdebug(f"{j}の時")
        pos=1
        current=0
        for k in range(N):
            nowPos=pos
            bit = 1 & (j>>k)
            if bit == 1:
                xdebug(f"{k} is right")
                nowPos=nowPos+L[k]
            else:
                xdebug(f"{k} is left")
                nowPos=nowPos-L[k]
            if sgn(nowPos)*sgn(pos)<0:
                xdebug(f"{k}の時交差")
                current+=1
            pos=nowPos
        best=max(best,current)

    xdebug(f"best {best}")
    return res


if __name__ == "__main__":
    res=solver()
