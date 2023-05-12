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




def solver(N,AI):
    target = AI[N-1]
    dp=[[0 for _ in range(20+1)] for _ in range(0,N-1)]
    dp[0][AI[0]]=1
    for p in range(1,N-1):
        for s in range(0,21):
            plus = dp[s][p]+AI[p]
            minus = dp[s][p]-AI[p]
            if plus <= 21:
                dp[s+1]
    # algorithm
    return dp[N-2][target]


if __name__ == "__main__":
    N = II()
    AI = LI()
    print("{}".format(solver(N,AI)))
