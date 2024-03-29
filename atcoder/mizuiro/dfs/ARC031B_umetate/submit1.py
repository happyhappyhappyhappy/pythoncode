# ライブラリのインポート
import sys
import pprint as pp
import copy
from collections import deque
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split('')))
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

def isnotgo(G,posh,posw):

    if posh < 0 or posw < 0 or 10 <= posh or 10 <= posw:
        return True
    pos_status = G[posh][posw]
    if pos_status == 'v' or pos_status == 'x':
        return True
    return False

def dfs(M,nh,nw):
    M[nh][nw] = 'v' # 探索済みを入れてしまう
    dh = [1,0,-1,0]
    dw = [0,1,0,-1]
    myStack = deque(list())
    myStack.append([nh,nw])
    while len(myStack) != 0:
        nhw = myStack.pop()
        for d in range(0,4):
            nexth = nhw[0]+dh[d]
            nextw = nhw[1]+dw[d]
            if isnotgo(M,nexth,nextw):
                continue
            myStack.append([nexth,nextw])
            M[nexth][nextw] = 'v'
    has_x = True
    for h1 in range(0,10):
        for w1 in range(0,10):
            if M[h1][w1] == 'o': # 陸地が残っている
                has_x = False
    return has_x

def solver(G):
    result = "NO"
    for h in range(0,10):
        for w in range(0,10):
            if G[h][w] == 'x':
                G_c=copy.deepcopy(G)
                allv = dfs(G_c,h,w)
                if(allv):
                    # xdebug(" ({},{})を埋め立て地として探索した結果、全ての陸地が埋め立てられました。".format(h,w))
                    result = "YES"
                    return result
    return result

if __name__ == "__main__":
    G = list()
    # rowG=[list(input()) for _ in range(10)]
    for line in range(10):
        tmpG=list(input())
#        del tmpG[-1]
        G.append(tmpG)
    print("{}".format(solver(G)))
