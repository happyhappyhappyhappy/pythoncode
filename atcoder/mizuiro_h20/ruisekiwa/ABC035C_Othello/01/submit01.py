# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from itertools import accumulate
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

N,Q=MI()
P=[0]*(N+1) # 0 indexにする
for _ in range(0,Q):
    f,t = MI()
    f=f-1 # 開始場所(0-index)
    t=(t-1)+1 # 終了場所(0-index)の次に1を加える
    P[f]=P[f]+1
    P[t]=P[t]+1
Acc=list(accumulate(P))
AccList=[]
for j in range(0,N):
    AccList.append(str(Acc[j]%2))
print("".join(AccList))
