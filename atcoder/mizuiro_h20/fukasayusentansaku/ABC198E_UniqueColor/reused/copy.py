# ライブラリのインポート
import sys
# import heapq,copy
# import pprint as pp
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
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

N = II()
C = [0]+LI()
L = [[] for _ in range(0,N+1)]
for _ in range(0,N-1):
    a,b=MI()
    L[a].append(b)
    L[b].append(a)
ANS = [True for _ in range(0,N+1)]
xdebug("N={}".format(N))
xdebug("C={}".format(C))
xdebug("ANS={}".format(ANS))

for x in range(0,N+1):
    xdebug("L[{}] = {}".format(x,L[x]))

ANS[0]=False
DisC = [0 for _ in range(0,max(C)+1)]
xdebug("DisC={}".format(DisC))
REACHE=[False for _ in range(0,N+1)]
def dfs(A):
    xdebug("---- def {} ----".format(A))
    if DisC[C[A]] > 0:
        # xdebug("C[{}] = {} => DisC[C[A]]= {}".format(A,C[A],DisC[C[A]]))
        xdebug("問題発生")
        xdebug("場所 = {},C = {}".format(A,C))
        xdebug("Now DisC={}".format(DisC))
        xdebug("値が0以上なのでFalseを入れます")
        ANS[A]=False
    DisC[C[A]]=DisC[C[A]]+1
    xdebug("ただ今 DisC={}".format(DisC))
    REACHE[A]=True
    xdebug("REACHE={}".format(REACHE))
    for l in L[A]:
        if REACHE[l]==False:
            xdebug("さらに 頂点 {} を検索".format(l))
            dfs(l)
        else:
            xdebug("もう 頂点 {} は検索済みなので進みません".format(l))
    DisC[C[A]]=DisC[C[A]]-1
    xdebug("頂点 {}の 終わり:ただ今 DisC={}".format(A,DisC[C[A]]))

dfs(1)

xdebug("--- 結果 ---\n")
xdebug("C")
for j in range(0,len(C)):
    xdebug("{} -> {}".format(j,C[j]))
xdebug("DisC")
for j in range(0,len(DisC)):
    xdebug("{} -> {}".format(j,DisC[j]))


for j in range(0,N+1):
    if ANS[j]:
        print(j)
