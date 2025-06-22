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
    res = [[1,2,3],[4,5],[6]]
    N=II()
    D=LI()
    P=[0]*N
    for j in range(1,N):
        P[j]=P[j-1]+D[j-1]
    # xdebug(f"{P}")
    res=[]
    for j in range(N-1):
        subres=[]
        for k in range(j+1,N):
            x=P[k]-P[j]
            subres.append(x)
        # xdebug(f"{j}->{subres}")
        res.append(subres)
    return res

if __name__ == "__main__":
    res=solver()
    for x in res:
        print(*x)
