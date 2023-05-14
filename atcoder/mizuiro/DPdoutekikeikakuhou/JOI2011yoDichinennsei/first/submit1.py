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

# def showDP(DP):
#     for k in range(len(DP)):
#         xdebug(DP[k])
#     xdebug("\n")

def solver(RAN,LA,RES):
    dp = [[ 0 for _ in range(0,21)] for _ in range(RAN)]
    dp[0][LA[0]]=1
    for j in range(0,RAN-1):
        for k in range(0,21):
            if 0 <= k-LA[j+1]:
                dp[j+1][k-LA[j+1]]=dp[j+1][k-LA[j+1]]+dp[j][k]
            if k+LA[j+1] <= 20:
                dp[j+1][k+LA[j+1]]=dp[j+1][k+LA[j+1]]+dp[j][k]
#        showDP(dp)
    return dp[RAN-1][RES]


if __name__ == "__main__":
    N = II()
    AI = LI()
    ANS = AI[N-1]
    RAN=N-1
    AI = AI[:-1]
    print("{}".format(solver(RAN,AI,ANS)))
