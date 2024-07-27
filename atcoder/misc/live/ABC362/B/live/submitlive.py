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
    result = "No"
    # algorithm
    ax,ay=MI()
    bx,by=MI()
    cx,cy=MI()
    hen=[0 for _ in range(3)]
    hen[0]=pow(ax-bx,2)+pow(ay-by,2)
    hen[1]=pow(cx-bx,2)+pow(cy-by,2)
    hen[2]=pow(ax-cx,2)+pow(ay-cy,2)
    hen.sort()
#    xdebug(f"{hen}")
    if hen[0]+hen[1]==hen[2]:
        result="Yes"
    return result


if __name__ == "__main__":
    print(solver())
