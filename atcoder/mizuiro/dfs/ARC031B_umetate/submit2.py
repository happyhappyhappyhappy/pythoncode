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

def isnotGo(G,r,w):
    c_value=G[r][w]
    if c_value == 'T' or c_value == 'x' or c_value == 'v':
        return 1
    else:
        return 0

def dfs(G,sea_r,sea_w):
    flug = False
    mystack = deque(list())
    dh = [1,0,-1,0]
    dw = [0,1,0,-1]
    G[sea_r][sea_w] = 'v'
    mystack.append([sea_r,sea_w])
    while len(mystack) != 0:
        nowpos = mystack.pop()
        for t in range(0,4):
            nexth = nowpos[0]+dh[t]
            nextw = nowpos[0]+dw[t]
            if isnotGo(G,nexth,nextw) == 1:
                continue
            else:
                G[nexth][nextw]='v'
                mystack.append([nexth,nextw])
    # 一通り'v'付けられるだけ付けてみた'o'がどれだけ付いたか確認
    for r in range(len(G)):
        for w in range(len(G[0])):
            if G[r][w] == 'o':
                # 失敗
                return 0
    # 成功
    return 1

def solver(G,R,W):
    flug = False
    # 周辺の柵を作る
    GS=[[ 'T' for _ in range(W+2)] for _ in range(R+2)]
    for r in range(0,R):
        for w in range(0,W):
            GS[r+1][w+1] = G[r][w]
    for r in range(0,R+2):
        for w in range(0,W+2):
            if GS[r][w] == 'x':
                GD = cp.deepcopy(GS)
                flug = dfs(GD,r,w)
    # algorithm
    if flug == 1:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    G=list()
    for _ in range(10):
        ltmp = list(input())
        G.append(ltmp)
    # showG(G,10,10)
    print("{}".format(solver(G,len(G),len(G[0]))))
