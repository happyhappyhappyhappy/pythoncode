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
    M=II()
    L=LI()
    yeardays=0
    for j in range(M):
        yeardays=yeardays+L[j]
    xdebug(f"一年 {yeardays=}")
    middled=(yeardays+1)//2
    xdebug(f"中日 {middled=}")
    ansM=0
    ansD=0
    calcMiddle=middled
    for j in range(M):
        if calcMiddle <= L[j]:
            ansM=j
            ansD=calcMiddle
            break
        calcMiddle=calcMiddle-L[j]
    xdebug(f"中日は {ansM+1=} 月 {ansD=} 日です。")

    return result


if __name__ == "__main__":
    print(solver())
