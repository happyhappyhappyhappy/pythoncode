# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
# pypy3用
import pypyjit
# 再帰制御解放
pypyjit.set_param('max_unroll_recursion=-1')
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
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

H,W,A,B = MI()


def dfs(h,w,a,F):
    # showG(F)
    if h == H:
        if a == 0:
            return 1
        else :
            return 0
    if F[h][w] == 1:
        return dfs(h,w+1,a,F)
    if w == W:
        return dfs(h+1,0,a,F)
    res=0 # 最終回答
    # 横置きにする
    pat1=0
    if (w+1<W) and (F[h][w+1]==0) and (0 < a):
        F[h][w]=1
        F[h][w+1]=1
        pat1=dfs(h,w+1,a-1,F)
        F[h][w]=0
        F[h][w+1]=0
    # 縦置きにする
    pat2=0
    if (h+1<H) and (F[h+1][w]==0) and (0 < a):
        F[h][w]=1
        F[h+1][w]=1
        pat2 = dfs(h,w+1,a-1,F)
        F[h][w]=0
        F[h+1][w]=0
    # 何も置かない
    pat3=0
    pat3 = dfs(h,w+1,a,F)
    res=pat1+pat2+pat3
    return res

FIG= [[-1 for _ in range(0,W+1)] for _ in range(0,H+1)]
for j in range(0,H):
    for k in range(0,W):
        FIG[j][k]=0

res=dfs(0,0,A,FIG)
print(res)
