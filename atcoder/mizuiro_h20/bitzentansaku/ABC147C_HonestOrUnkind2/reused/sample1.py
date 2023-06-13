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
N = int(input())
L = [[] for _ in range(0,N)]
# xdebug(L)
for j in range(0,N):
    A = int(input())
    for _ in range(0,A):
        x,y = MI()
        L[j].append([x-1,y])
xdebug("L={}".format(L))
ans = 0
for j in range(0,2**N):
    T = []
    cnt = 0
    for k in range(0,N):
        shiftJ = j >> k
        if((shiftJ & 1)==1):
            T.append(1)
            cnt = cnt+1
        else:
            T.append(0)
    xdebug("T={}".format(T))
    f = True
    for k in range(0,N):
        if T[k]==1:
            xdebug("{}さんが正直とすれば…".format(k))
            for x,y in L[k]:
                if T[x] != y:
                    xdebug("{} の {}が一致しないNG".format(x,y))
                    f = False
                else:
                    xdebug("{}さんは{}という条件に一致".format(x,y))
    if f:
        xdebug("{} の評価が「正直」と一致しました".format(k))
        ans = max(ans,cnt)
print(ans)
