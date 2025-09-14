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

def right90(S):
    T=zip(*S)
    R=[list(row[::-1]) for row in T]
    return R

def diffGrid(S,T,N):
    res=0
    for j in range(N):
        for k in range(N):
            if S[j][k]!=T[j][k]:
                res+=1
    return res

def solver():
    res = 0
    N = II()
    S0=[list(input()) for _ in range(N)]
    T=[list(input()) for _ in range(N)]
    S1=right90(S0)
    S2=right90(S1)
    S3=right90(S2)
    diff0=diffGrid(S0,T,N)
    diff1=diffGrid(S1,T,N)+1
    diff2=diffGrid(S2,T,N)+2
    diff3=diffGrid(S3,T,N)+3
    res=min(diff0,diff1,diff2,diff3)
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
