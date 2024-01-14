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

N,M=MI()
P=[]
Y=[]
for j in range(0,M):
    p,y=MI()
    P.append(p-1)
    Y.append(y)
for j in range(0,M):
    xdebug(f"{P[j]}->{Y[j]}")
Value=[[] for j in range(0,N)]
Bb=[[] for _ in range(0,N)]
for j in range(0,N):
    xdebug(f"{j}->{Value[j]}")
for j in range(0,M):
    Value[P[j]].append(Y[j])
for j in range(0,N):
    Bb1=sorted(set(Value[j]))
    Bb[j].append(Bb1)
for j in range(0,N):
    xdebug(f"{j}->{Bb[j]}")
DICTS=[]*N
for j in range(0,N):
    dp = {v:x for x,v in enumerate(Bb[j])}
    DICTS[j].append(dp)
