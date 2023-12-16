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

INF=10**20
N,M,K,S=MI()
print(f"町の数{N}つ,道の数{M}つ,ゾンビの町{K}つ,ゾンビの影響する道{S}本")
P,Q=MI()
print(f"安全な街の宿{P}円,危険な街{Q}円")
ZON=[]
for _ in range(0,K):
    a = II()
    ZON.append(a-1)
print(f"ゾンビ街{ZON}")
LINKS=[[] for _ in range(N)]

for _ in range(0,M):
    a,b=MI()
    LINKS[a-1].append(b-1)
    LINKS[b-1].append(a-1)
print(f"ルート{LINKS}")
dist=[INF]*N
q=deque(ZON)
for v in ZON:
    dist[v]=0
while 0 < len(q):
    node = q.popleft()
    for next_city in LINKS[node]:
        if dist[next_city]!=INF:
            continue
        dist[next_city]=dist[node]+1
        q.append(next_city)
print(f"ゾンビとの距離={dist}")
cost = [P]*N
for n in range(0,N):
    if dist[n]<=S:
        print(f"町 {n+1}は危険なので泊まるコスト{Q}")
        cost[n]=Q
    if n in ZON:
        print(f"町 {n+1}はさらにゾンビにやられている。コスト最大")
        cost[n]=INF
    if n==0 or n == N-1:
        cost[n]=0
for j in range(0,N):
    print(f"町{j+1} コスト{cost[j]}")
def dijkstra(s,g):
    dists=[INF for j in range(0,N)]
    dists[s]=0
    pq=[(0,s)]
    while 0 < len(pq):
        d,node=heapq.heappop(pq)
        if node == g:
            print(f"ゴールに着いたので抜けます")
            return d
        if dists[node] < d:
            continue
        for next_city in LINKS[node]:
            c = cost[next_city]
            nextcost=d+c
            if nextcost < dists[next_city]:
                dists[next_city]=nextcost
                heapq.heappush(pq,(nextcost,next_city))
print(dijkstra(0,N-1))
