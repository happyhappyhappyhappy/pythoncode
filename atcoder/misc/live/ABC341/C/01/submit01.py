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

H,W,N = MI()
S = []
WAY = sys.stdin.readline().strip()
for _ in range(0,H):
    s = sys.stdin.readline().strip()
    S.append(s)
PTN=[]
for j in range(0,H):
    for k in range(0,W):
        if S[j][k] == '.':
            PTN.append([j,k])
count = 0
sLen=len(WAY)
for j,k in PTN:
    sj=j
    sk=k
    flug = True
    for m in range(0,sLen):
        nextT=WAY[m]
        if nextT == 'L':
            k=k-1
        elif nextT == 'R':
            k=k+1
        elif nextT == 'U':
            j=j-1
        elif nextT == 'D':
            j=j+1
        if S[j][k] == '#':
            flug=False
            break
    if flug == True:
        count=count+1
print(count)
