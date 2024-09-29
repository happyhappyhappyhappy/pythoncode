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
    # algorithm
    N=II()
    A=LI()
    res+=N
    n=len(A)
    B=[]
    for j in range(n-1):
        x=A[j+1]-A[j]
        B.append(x)
    SM=[]
    key=0
    m=len(B)
    while key < m:
        j=key
        num=B[key]
        while j < m and B[key]==B[j]:
            j+=1
        x=j-key
        SM.append((num,x))
        key=j
    for _,m in SM:
        x=((m+1)*m)//2
        res+=x
    return res


if __name__ == "__main__":
    print(solver())
