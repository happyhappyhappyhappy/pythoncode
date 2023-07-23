# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
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

# 大域変数設定+データ入力
N = II()
# xdebug("N={}".format(N))
tmp = LI()
# xdebug("tmp = {}".format(tmp))
C = [0]+tmp
# xdebug("C={}".format(C))
# Yes No 式は無理があった
# G = [[ False  for _ in range(0,N+1)] for _ in range(0,N+1)]
# for _ in range(0,N-1):
#     x,y = MI()
#     G[x][y] = True
#     G[y][x] = True
G = [[] for _ in range(0,N+1)]
for _ in range(0,N-1):
    x,y = MI()
    G[x].append(y)
    G[y].append(x)

# xdebug(G)

# 他内部使用のグローバル変数

# 正しい数になっているか否か
ANS =  [True] * (N+1)
ANS[0] = False # 0番は訪問しないし答えにならない

# 訪問完了
VISITED = [ False ] *  (N+1)
VISITED[0] = True # 0番はもう訪問したことにする

# 指定色 の 色利用カウント
# もし 1以上あった状態でさらに色が見つかったらこれは回答では無くなる
ColorCnt = [ 0 ] * (max(C)+1)

def dfs(P):
    pColor = C[P]
    # xdebug("確認前:ColorCnt = {}".format(ColorCnt))
    if 0 < ColorCnt[pColor]:
        # xdebug("もう色 {} は利用済みです")
        ANS[P]=False
    ColorCnt[pColor]=ColorCnt[pColor]+1
    # xdebug("確認後:ColorCnt = {}".format(ColorCnt))
    VISITED[P]=True
#    nextList = G[P]
    # 次の頂点を決める。もしつながっていて、まだ訪問していなかったら進む
    for j in range(0,len(G[P])):
        nextP = G[P][j]
        if VISITED[nextP] == False:
            # xdebug("次は {} へ行きます".format(nextP))
            dfs(nextP)

    # 最後に一旦追加した色数を減らして終わり
    ColorCnt[pColor]=ColorCnt[pColor]-1

dfs(1)
for j in range(1,len(ANS)):
    if ANS[j] == True:
        print(j)
