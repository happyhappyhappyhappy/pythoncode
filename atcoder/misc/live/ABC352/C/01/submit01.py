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
    A=[]
    B=[]
    for _ in range(N):
        a,b=MI()
        A.append(a)
        B.append(b)
    maxFace=0
    all_shoulder=0
    for j in range(N):
        shoulder=A[j]
        headtop=B[j]
        all_shoulder=all_shoulder+shoulder
        faceLong=headtop-shoulder
        if maxFace < faceLong:
            maxFace=faceLong
    result=maxFace+all_shoulder
    return result


if __name__ == "__main__":
    print(solver())
