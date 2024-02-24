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
def SI(): return sys.stdin.readline().strip()
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

charVec=[0]*150

S=SI()
for j in range(0,len(S)):
    x=ord(S[j])
    charVec[x]=charVec[x]+1

oneCord=0
for j in range(0,150):
    if charVec[j]==1:
        oneCord=j
        break
# oneC=chr(oneCord)
# print(oneC)
ans=0
for j in range(0,len(S)):
    x = ord(S[j])
    if x == oneCord:
        ans=j+1
        break
print(ans)
