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
    N=II()
    A=[]
    B=[]
    for _ in range(N):
        S=SI()
        A.append(S)
    for _ in range(N):
        S=SI()
        B.append(S)
    outj=0
    outk=0
    for j in range(N):
        for k in range(N):
            AS=A[j]
            BS=B[j]
            if AS[k]!=BS[k]:
                outj=j+1
                outk=k+1
                break
    ans=str(outj)+" "+str(outk)
    return ans


if __name__ == "__main__":
    print(solver())
