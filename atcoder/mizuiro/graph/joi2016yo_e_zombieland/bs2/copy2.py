# ライブラリのインポート
import sys
import heapq,copy
import pprint as pp
from collections import deque
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
INF=10**20
N,M,K,S=MI()
P,Q=MI()
zombie=[]
for k in range(0,K):
    z = II()
    zombie.append(z)
LINKS=[[] for _ in range(N)]
for _ in range(0,M):
    a,b=MI()
    LINKS[a-1].append(b-1)
    LINKS[b-1].append(a-1)
dist=[INF]*N
deq=deque(zombie)
for j in zombie:
    dist[j]=0
while len(deq)!=0:
    node=deq.popleft()
    for next_city in LINKS[node]:
        if dist[next_city]!=INF:
            continue
        dist[next_city]=dist[node]+1
        deq.append(next_city)
for j in range(0,N):
    xdebug(f"{j+1}->{dist[j]}")
