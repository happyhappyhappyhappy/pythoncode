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

DTurn=[[0,-1],[1,0],[0,1],[-1,0]]

def solver(H:int,W:int,N:int):
    G=[["."] * W for _ in range(H)]
    # algorithm
    x = 0
    y = 0
    m = 0
    for _ in range(N):
        if G[y][x]==".":
            G[y][x]="#"
            m=m+1 # 時計回り90度
        elif G[y][x]=="#":
            G[y][x]="."
            m=m+3 # 反時計回り90度=時計回り270度
        m = m % 4 # ここではみ出した分を戻す
        dx,dy=DTurn[m]
        x = x + dx
        y = y + dy
        if x < 0:
            x=W-1
        elif W <= x:
            x=0
        if y < 0:
            y = H-1
        elif H <= y:
            y = 0
    return G
if __name__ == "__main__":
    H,W,N=MI()
    GList=solver(H,W,N)
    for j in range(H):
        lineStr="".join(GList[j])
        print(lineStr)
