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

N,C = MI()
ABC=[]
for _ in range(0,N):
    ABC.append(LI())
# for x in ABC:
#     xdebug(f"{x}")
days=set()
for a,b,c in ABC:
    if a not in days:
        days.add(a)
    if b+1 not in days:
        days.add(b+1)
days2 = sorted(list(days))
# for j,x in enumerate(days2):
#     xdebug(f"x={x} j={j}")
dict = {x:j for j,x in enumerate(days2)}
xdebug(f"{dict}")
acc = [0] * (len(days2))
for a,b,c in ABC:
    # xdebug(dict[a])
    f = bisect_left(days2,a)
    t = bisect_left(days2,b+1)
#    acc[dict[a]] = acc[dict[a]]+c
#    acc[dict[b+1]] = acc[dict[b+1]]-c
    acc[f]=acc[f]+c
    acc[t]=acc[t]-c
for j in range(0,(len(days2)-1)):
    acc[j+1]=acc[j+1]+acc[j]
for j in range(0,len(days2)):
    xdebug(f"ラベル {j} 日 -> {acc[j]} 円")
