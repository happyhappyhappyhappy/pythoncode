# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

from itertools import permutations
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
    flg = False
    res=[]
    N=II()
    A=LI()
    P=permutations([j+1 for j in range(N)])
    for p_tuple in P:
        res=list(p_tuple)
        flg=True
        for j in range(N):
            if not (flg and (A[j]==-1 or A[j]==res[j])):
                flg = False
                break
        if flg:
            break
    return flg,res


if __name__ == "__main__":
    flg,res=solver()
    if flg:
        print("Yes")
        print(*res)
    else:
        print("No")
