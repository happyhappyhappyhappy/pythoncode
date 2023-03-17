# ライブラリのインポート
# from collections import defaultdict
# import heapq,copy
import copy as cp
import pprint as pp
import sys
from collections import deque
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

def showG(G,R,W):
    for r in range(0,R):
        xdebug(G[r])

def isntGo(G,r,w):
    if r < 0 or w < 0 or 10 <= r or 10 <= w:
        return true
    if G[r][w] != # TODO: ここから 経過時間 18:25

def dfs(G,sea_r,sea_w):
    flug = False
    mystack = deque(list())
    dh = [1,0,-1,0]
    dw = [0,1,0,-1]
    G[sea_r][sea_w] = 'v'
    mystack.append(list(sea_r,sea_w))
    while len(mystack) != 0:
        nowpos = mystack.pop()
        for t in range(0,4):


def solver(G,R,W):
    flug = False
    for r in range(0,R):
        for w in range(0,W):
            if G[r][w] == 'x':
                GD = cp.deepcopy(G)
                flug = dfs(GD,r,w)
    # algorithm
    if flug:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    G=list()
    for _ in range(10):
        ltmp = list(input())
        G.append(ltmp)
    showG(G,10,10)
    print("{}".format(solver(G,len(G),len(G[0]))))
