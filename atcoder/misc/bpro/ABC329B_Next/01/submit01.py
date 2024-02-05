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

def qsort_r(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lessList= [ x for x in arr[1:] if x <= pivot]
        greaterList = [ x for x in arr[1:] if pivot < x]
        return qsort_r(greaterList) + [pivot] + qsort_r(lessList)

def solver(Q):
    result = 0
    setL = list(set(Q))
    setLSort = qsort_r(setL)
    result = setLSort[1]
    return result

if __name__ == "__main__":
    N=II()
    Q=LI()
    print("{}".format(solver(Q)))
