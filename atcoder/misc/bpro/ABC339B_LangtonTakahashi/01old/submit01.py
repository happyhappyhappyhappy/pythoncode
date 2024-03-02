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

H,W,N=MI()
print(f"高さ= {H},幅= {W},移動回数 = {N}")
G=[["."]*W for _ in range(H)]
x=0
y=-1
py = 0
px = 0
for _ in range(N):
    xdebug(f"座標 ({px},{py})")
    pinfo = G[py][px]
    turn=0
    if pinfo == ".":
        turn = 0
    elif pinfo == "#":
        turn = 1
    ny,nx=turnMove(y,x,turn)
    if turn==0:
        G[py][px]="#"
    elif turn==1:
        G[py][px]="."
    py = py + ny
    px = px + nx
    if py == -1:
        py = H-1
    if py == H:
        py=0
    if px == -1:
        px = W-1
    if px == W:
        px = 0
    y = ny
    x = nx
for y in range(H):
    out="".join(G[y])
    print(out)
