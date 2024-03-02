# ライブラリのインポート
# import heapq,copy
import pprint as pp

# import pypyjit
import sys

# from collections import deque
from logging import DEBUG, StreamHandler, getLogger

# pypy3用
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)

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

N = II()
def turnMove(y:int,x:int,t:int):
    ny = 0
    nx = 0
    if t == 0:
        if y == -1:
            ny = 0
            nx = 1
        elif y == 1:
            nx = -1
            ny = 0
        elif x == -1:
            ny = -1
            nx = 0
        else:
            # y=0,x=-1
            ny = 1
            nx = 0
    elif t==1:
        if y == 1:
            nx = 1
            ny = 0
        elif y == -1:
            nx = -1
            ny = 0
        elif x == 1:
            ny = -1
            nx = 0
        elif x == -1:
            ny = 1
            nx = 0
    return ny,nx
for _ in range(N):
    y,x,turn=MI()
    xdebug(f"現在 次の方向は y軸 {y} x軸 {x}です")
    if turn==0:
        xdebug("時計回りに回ります")
    else:
        xdebug("反時計回りに回ります")
    y,x = turnMove(y,x,turn)
    xdebug(f"結果 {y= } {x= }")
