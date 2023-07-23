# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
# pypy3用
import pypyjit
# 再帰制御解放
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**9)
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

N = II()
Ca = LI()
C = [0]+Ca
L = [[] for j in range(N+1)]
for _ in range(0,N-1):
    f,t = MI()
    L[f].append(t)
    L[t].append(f)

xdebug("N = {}".format(N))
xdebug("C = {}".format(C))
xdebug(L)

# 正しいか間違っているか確認するリスト
ANS = [True]*(N+1)
# ただし、0番目は検索しないのでNG
ANS[0] = False
# ある色(整数)が使っているかどうかのチェックに使うDColor
ColorD = [0]*(max(C)+1)
# VISITED 到着済みか否か
VISITED = [False]*(N+1)

def dfs(POS):
    posCol=C[POS]
    if 0 < ColorD[posCol]:
        ANS[POS]=False
    ColorD[posCol]=ColorD[posCol]+1
    xdebug("現在の {} の到着段階 {}".format(POS,VISITED[POS]))
    VISITED[POS] = True
    nextPosL=L[POS]
    xdebug("{} -> {} ".format(POS,nextPosL))
    for j in range(0,len(nextPosL)):
        nextPos = L[POS][j]
        if VISITED[nextPos] == False:
            dfs(nextPos)
        else:
            xdebug("もう {} は行っているので行かない".format(nextPos))
    ColorD[posCol]=ColorD[posCol]-1

dfs(1)
for j in range(1,len(ANS)):
    if ANS[j] == True:
        print(j)
