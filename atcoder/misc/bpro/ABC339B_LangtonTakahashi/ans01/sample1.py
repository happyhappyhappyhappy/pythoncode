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

# 方向 ↑,→,↓,←, [dy,dx] ここだけ方眼紙に準じる
DX = [0,1,0,-1]
DY = [-1,0,1,0]
H,W,N=MI()

G = [["."]*W for _ in range(H)]
for j in range(H):
    xdebug(G[j])
x = 0
y = 0
m = 0
for _ in range(N):
    if G[x][y] == ".":
        G[x][y] = "#"
        m = m + 1 # 時計回り
    elif G[x][y] == "#":
        G[x][y] = "."
        m = m + 3 # 反時計回り = 時計回り 3回と同じ なるほど
    m = m % 4
    dx=DX[m]
    dy=DY[m]
    x = x + dx
    y = y + dy
    if x < 0:
        x = H-1
    if H <= x:
        x = 0
    if y < 0:
        y = W-1
    if W <= y:
        y = 0
for j in range(H):
    pstr="".join(G[j])
    print(pstr)
