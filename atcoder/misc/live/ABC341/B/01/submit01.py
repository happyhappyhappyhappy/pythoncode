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

def solver(N,A,S,T):
    result = 0
    for j in range(0,N-1):
        s=S[j]
        t=T[j]
    for j in range(0,N-1):
        a = (A[j]//S[j])
        b = a*T[j]
        A[j+1]=A[j+1]+b
        A[j]=A[j]-(a*S[j])
    # algorithm
    result=A[N-1]
    return result


if __name__ == "__main__":
    N = II()
    A = LI()
    S = [0]*(N-1)
    T = [0]*(N-1)
    for j in range(0,N-1):
        S[j],T[j]=MI()
    print("{}".format(solver(N,A,S,T)))
