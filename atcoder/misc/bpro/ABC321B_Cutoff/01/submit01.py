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

def solver(N:int,X:int,A:list):
    result = 0
    xdebug(f"N={N},X={X},A={A}")
    flug=False
    for j in range(101):
        LastA = A[:]
        LastA.append(j)
        LastA.sort()
        total=sum(LastA[1:N-1])
        if X <= total:
            result=j
            flug=True
            break
    # algorithm
    if flug is False:
        result = -1
    return result

if __name__ == "__main__":
    N,X=MI()
    A=LI()
    print(f"{solver(N,X,A)}")
