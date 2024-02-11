# ライブラリのインポート
import sys
import heapq
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

def myfloor(a,b):
    return (a+(b-1))//b

def solver(N):
    result = 0
    arr=[]
    heapq.heappush(arr,N)
    while 0 < len(arr):
        x = heapq.heappop(arr)
        result=result+x
        fl = myfloor(x,2)
        if 1 < fl:
            # xdebug(f"queに{fl}をセットします")
            heapq.heappush(arr,fl)
        ce = x // 2
        if 1 < ce:
            heapq.heappush(arr,ce)
    # algorithm
    return result


if __name__ == "__main__":
    N=II()
    print("{}".format(solver(N)))
