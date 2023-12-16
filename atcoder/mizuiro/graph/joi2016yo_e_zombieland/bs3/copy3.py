# ライブラリのインポート
import sys
import heapq
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
INF = 10**20
N,M,K,S=MI()
P,Q=MI()
zombie = []
for _ in range(0,K):
    zombie.append(II()-1)
LINKS=[[] for _ in range(N)]
for _ in range(0,M):
    a,b=MI()
    LINKS[a-1].append(b-1)
    LINKS[b-1].append(a-1)

z_dist=[INF]*N
q = deque(zombie)
for j in zombie:
    z_dist[j]=0
while len(q)!=0:
    node=q.popleft()
    for next_city in LINKS[node]:
        if z_dist[next_city]!=INF:
            continue
        z_dist[next_city]=z_dist[node]+1
        q.append(next_city)
print(z_dist)
