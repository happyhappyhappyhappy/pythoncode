# ライブラリのインポート
import sys
# import heapq,copy
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
zombie = []
for k in range(0,K):
    x = II()
    zombie.append(x)

link = [[] for _ in range(0,N)]
for m in range(0,M):
    a,b=MI()
    a=a-1
    b=b-1
    link[a].append(b)
    link[b].append(a)
for n in range(0,N):
    print(f"{n}->{link[n]}")
dist=[INF]*N
q = deque(zombie)
for v in zombie:
    dist[v]=0
while len(q)!=0:
    node = q.popleft()
    for nextc in link[node]:
        if dist[nextc]!=INF:
            continue
        dist[nextc]=dist[node]+1
        q.append(nextc)
for n in range(0,N):
    print(f"都市 {n} の ゾンビ距離 {dist[n]}")
