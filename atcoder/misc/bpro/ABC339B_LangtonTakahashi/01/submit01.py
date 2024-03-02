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

DTURN = [[0,-1],[1,0],[0,1],[-1,0]]

H,W,N=MI()

G=[["."]*W for _ in range(H)]

x = 0
y = 0
m = 0
for _ in range(N):
    if G[y][x] == ".":
        G[y][x]="#"
        m = m + 1
    elif G[y][x] == "#":
        G[y][x]="."
        m = m + 3
    m = m % 4
    dx,dy = DTURN[m]
    y = y + dy
    x = x + dx
    if H <= y:
#        xdebug(f"xがエリアH-1={H-1}を超えたので0にワープします")
        y = 0
    elif y < 0:
#        xdebug(f"xがエリア0を超えたのでH-1={H-1}にワープします")
        y = H-1
    if W <= x:
#        xdebug(f"xがエリアW-1={W-1}を超えたので0にワープします")
        x = 0
    elif x < 0:
#        xdebug(f"xがエリア0を超えたのでW-1={W-1}にワープします")
        x = W-1
#    xdebug(f"次は({x},{y})に行きます")

for j in range(H):
    prstr="".join(G[j])
    print(prstr)
