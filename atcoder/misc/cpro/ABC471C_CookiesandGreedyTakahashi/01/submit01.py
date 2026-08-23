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
    res = 0
    N=II()
    N+=1
    A=LI()
    A.extend([0])
    A.sort()
    pos=0
    P=A.index(0)
    L=P-1
    R=P+1
    for _ in range(N-1):
        # xdebug("")
        # xdebug(f"---- Term No,{j} ----")
        if L == -1:
            # xdebug(f"{pos}は左隅です 右の{A[R]}に移動します")
            res+=(A[R]-pos)
            pos=A[R]
            R+=1
        elif R == N:
            # xdebug(f"{pos}は右隅です 左の {A[L]}へ移動します")
            res+=(pos-A[L])
            pos=A[L]
            L-=1
        else:
            LEFT=pos-A[L]
            RIGHT=A[R]-pos
            if LEFT <= RIGHT:
                # xdebug(f"左が短いです {pos}->{A[L]}と移動します")
                res+=LEFT
                pos=A[L]
                L-=1
            else:
                # xdebug(f"右が短いです {pos}->{A[R]}へと移動します")
                res+=RIGHT
                pos=A[R]
                R+=1
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
