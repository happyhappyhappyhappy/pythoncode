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




def solver(M,Dates):
    result = 0
    for j in range(0,M):
        x=Dates[j]
        for k in range(1,x+1):
            dateStr=str(j+1)+str(k)
            stLen=len(dateStr)
            dateSet=set()
            for m in range(0,stLen):
                dateSet.add(dateStr[m])
            if len(dateSet) == 1:
                result=result+1
    # algorithm\
    return result


if __name__ == "__main__":
    M=II()
    Dates=LI()
    print("{}".format(solver(M,Dates)))
