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




def solver(N:int,A:list):
    dp=[[0 for _ in range(21)] for _ in range(N-1)]
    dp[0][A[0]]=1
    for j in range(N-1):
        aj=A[j]
        for k in range(21):
            if 0 <= k+aj <= 20:
                dp[j][k+aj]=dp[j][k+aj]+dp[j-1][k]
            if 0 <= k-aj <= 20:
                dp[j][k-aj]=dp[j][k-aj]+dp[j-1][k]
    result = dp[N-2][A[N-1]]
    # algorithm
    return result


if __name__ == "__main__":

    N = II()
    A = LI()
    print("{}".format(solver(N,A)))
