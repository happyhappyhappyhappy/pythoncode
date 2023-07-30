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




def dfs(n,N,mA,mB,mC,lengList,ANSList):
    if n == N:
        # それぞれ割り当てた竹から長さ魔法の量を求める
        # A の base長さ

    result = 0
    # algorithm
    return result


if __name__ == "__main__":
    N,A,B,C = MI()
    ANSList = [A,B,C]
    BubList = list()
    for _ in range(0,N):
        LNGS = II()
        BubList.append(LNGS)
    mA = list()
    mB = list()
    mC = list()
    print("{}".format(dfs(0,N,mA,mB,mC,BubList,ANSList)))
