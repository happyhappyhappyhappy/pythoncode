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




def solver(A,M,L,R):
    result = 0
    L=L-A
    R=R-A

    if 0 <= L:
        result=R // M - (L-1) // M
    elif L < 0 and 0 < R:
        result = R // M + (-L)//M + 1
    elif R <= 0 :
        result = (-L)//M - (-R-1)//M
    else:
        xdebug(f"想定外のケース L={L},R={R}")
    # algorithm
    return result

if __name__ == "__main__":
    A,M,L,R=MI()
    print("{}".format(solver(A,M,L,R)))
