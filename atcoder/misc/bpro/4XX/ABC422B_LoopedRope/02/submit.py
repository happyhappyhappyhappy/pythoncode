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
    H,W=MI()
    rawGrid=[input() for _ in range(H)]
    banGrid=[]
    banGrid.append("."*(W+2))
    for row in rawGrid:
        banGrid.append("."+row+".")
    banGrid.append("."*(W+2))
    analyzeGrid=[list(row) for row in banGrid]
    for j in range(1,H+1):
        for k in range(1,W+1):
            if analyzeGrid[j][k]=="#":
                cnt=0
                if analyzeGrid[j-1][k]=="#":
                    cnt+=1
                if analyzeGrid[j+1][k]=="#":
                    cnt+=1
                if analyzeGrid[j][k-1]=="#":
                    cnt+=1
                if analyzeGrid[j][k+1]=="#":
                    cnt+=1
                if cnt not in {2,4}:
                    return "No"
    return "Yes"


if __name__ == "__main__":
    res=solver()
    print(res)

