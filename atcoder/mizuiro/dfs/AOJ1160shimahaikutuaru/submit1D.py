# ライブラリのインポート
import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
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

# 探索変数:上から時計回り
dh = [-1,-1,0,1,1, 1, 0,-1]
dw = [ 0, 1,1,1,0,-1,-1,-1]

xdebug(sys.getrecursionlimit())

def dfs(M,nh,nw):
    xdebug("({},{})から始まった検索は終了".format(nh,nw))
    M[nh][nw]=3 # 探索済みのマスを3にする
    # 次の探索値を決める
    for j in range(0,8):
        nexth = nh+dh[j]
        nextw = nw+dw[j]
        cont = M[nexth][nextw]
        if cont != 1:
            xdebug("({},{})の 土質は {} なので探索しない".\
                    format(nexth,nextw,cont))
            continue
        else:
            dfs(M,nexth,nextw)
    xdebug("({},{})から始まった検索は終了".format(nh,nw))

def showM(Y,M):
    for h in range(0,Y):
        xdebug(M[h])

while 1:
    W , H = MI()
    if W == 0 and H == 0:
        break
    else: # 壁有りの背景作成
        M = [[2 for _ in range(W+2)] for _ in range(H+2)]
        # 地図情報を得る
        MT = list()
        for _ in range(H):
            MT.append(LI())
        # 重ね合わせる
        for h in range(H):
            for w in range(W):
                M[h+1][w+1]=MT[h][w]
        # チェック
        # for h in range(H+2):
        #    xdebug(M[h])
        land_count=0
        for h in range(0,H+2):
            for w in range(0,W+2):
                if M[h][w] == 1:
                    dfs(M,h,w);
                    land_count=land_count+1
                    showM(H+2,M)
        print(land_count)
