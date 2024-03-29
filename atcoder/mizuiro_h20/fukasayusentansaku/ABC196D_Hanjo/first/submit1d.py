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

H,W,A,B = MI()

def showG(F):
    xdebug("現在の図を表します")
    h = len(F)
    for j in range(0,h):
        xdebug(F[j])
    xdebug("終了")

def dfs(h,w,a,F):
    xdebug("[{}][{}]に着きました 長方形残り {} 枚 ".format(h,w,a))
    # showG(F)
    if h == H:
        xdebug("最終行まで到着")
        if a == 0:
            xdebug("長方形残り無し->成功 回答に入れる")
            return 1
        else :
            xdebug("長方形 {} 枚残り->失敗".format(a))
            return 0
    if F[h][w] == 1:
        xdebug("使用中: [{}][{}]に移動する".format(h,w+1))
        return dfs(h,w+1,a,F)
    if w == W:
        xdebug("最右列の為、下の行 [{}][{}]に移動する".format(h+1,w))
        return dfs(h+1,0,a,F)
    xdebug("[{}][{}]の探索開始".format(h,w))
    res=0 # 最終回答
    # 横置きにする
    pat1=0
    if (w+1<W) and (F[h][w+1]==0) and (0 < a):
        xdebug("-->[{}][{}]を軸に横置き選択<--".format(h,w))
        F[h][w]=1
        F[h][w+1]=1
        pat1=dfs(h,w+1,a-1,F)
        F[h][w]=0
        F[h][w+1]=0
    # 縦置きにする
    pat2=0
    if (h+1<H) and (F[h+1][w]==0) and (0 < a):
        xdebug("-->[{}][{}]を軸に縦置き選択<--".format(h,w))
        F[h][w]=1
        F[h+1][w]=1
        pat2 = dfs(h,w+1,a-1,F)
        F[h][w]=0
        F[h+1][w]=0
    # 何も置かない
    pat3=0
    xdebug("-->[{}][{}]には置かない<--".format(h,w))
    pat3 = dfs(h,w+1,a,F)
    res=pat1+pat2+pat3
    xdebug("[{}][{}]の探索終了".format(h,w))
    return res

FIG= [[-1 for _ in range(0,W+1)] for _ in range(0,H+1)]
for j in range(0,H):
    for k in range(0,W):
        FIG[j][k]=0

res=dfs(0,0,A,FIG)
print(res)
