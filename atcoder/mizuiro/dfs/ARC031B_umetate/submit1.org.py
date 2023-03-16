# ライブラリのインポート
import sys
# from collections import defaultdict
# import heapq,copy
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
        xdebug("( {} , {} ) はエリア外になるので無効".format(posh,posw))
        return True
    pos_status = G[posh][posw]
    if pos_status == 'v' or pos_status == 'x':
        xdebug("( {} , {} ) は {} なのでこれ以上無理".format(posh,posw,pos_status))
        return True

    xdebug("( {} , {} ) は陸なのでOK".format(posh,posw))
    return False

def showM(M):
    xdebug("現在の島の地図の状態")
    for h in range(0,10):
        xdebug(M[h])

def dfs(M,nh,nw):
    xdebug("----( {} , {} )に入りました----".format(nh,nw))
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
            # 問題なかった場合
            # xdebug("次は( {} , {} )に行きます".format(nexth,nextw))
            myStack.append([nexth,nextw])
            M[nexth][nextw] = 'v'
    has_x = True
    for h in range(0,10):
        for w in range(0,10):
            if M[h][w] == 'o': # 陸地が残っている
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
            # showM(G)
    # algorithm
    return result

if __name__ == "__main__":
    G = list()
    # rowG=[list(input()) for _ in range(10)]
    for line in range(10):
        tmpG=list(input())
        del tmpG[-1]
        G.append(tmpG) # 最後の特殊文字を消す
    print("{}".format(solver(G)))
