# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from bisect import bisect_left
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
N,C=MI()
ABC=[]
for _ in range(0,N):
    ABC.append(LI())
dates_org=[]
for a,b,c in ABC:
    dates_org.append(a)
    dates_org.append(b+1)
dates=list(sorted(set(dates_org)))
acc=[0]*(len(dates))
for a,b,c in ABC:
    ap=bisect_left(dates,a)
    bp=bisect_left(dates,b+1)
    acc[ap]=acc[ap]+c
    acc[bp]=acc[bp]-c
for j in range(0,len(dates)-1):
    acc[j+1]=acc[j+1]+acc[j]

ans = 0
for j in range(0,len(dates)-1):
    ans = ans + min(acc[j],C)*(dates[j+1]-dates[j])
#     xdebug(f"{dates[j]}->{dates[j+1]} は {acc[j]}か{C}")
print(ans)
