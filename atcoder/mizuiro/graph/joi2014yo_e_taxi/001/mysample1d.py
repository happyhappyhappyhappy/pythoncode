# ライブラリのインポート
import sys
from heapq import heappop,heappush
import pprint as pp
from collections import deque,defaultdict
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
INF=float('inf')

class Dijkstra():
    def __init__(self):
        self.e=defaultdict(list)
    def add(self,u,v,d,directed=False):
        if directed is False:
            self.e[u].append([v,d])
            self.e[v].append([u,d])
        else:
            self.e[u].append([v,d])
    def delete(self,u,v):
        self.e[u]=[x for x in self.e[u] if x[0]!=v]
        self.e[v]=[x for x in self.e[v] if x[0]!=u]
    def Dijkstra_search(self,s):
        d=defaultdict(lambda: float('inf'))
        prev=defaultdict(lambda: None)
        d[s]=0
        q=[]
        heappush(q,(0,s))
        v = defaultdict(bool)
        while len(q)!=0:
            k,u = heappop(q)
            if v[u]==True:
                continue
            v[u]=True
            for uv,ud in self.e[u]:
                if v[uv]==True:
                    continue
                vd=k+ud
                if vd < d[uv]:
                    d[uv]=vd
                    prev[uv]=u
                    heappush(q, (vd,uv))
        return d,prev
    def getDijkstraShortestPath(self,start,goal):
        _,prev = self.Dijkstra_search(start)
        shortestPath=[]
        node=goal
        while node != None:
            shortestPath.append(node)
            node=prev[node]
        return shortestPath[::-1]
# N: 町の数 K: 辺の数
N,K=MI()
# C: 各町のタクシーの運賃 R: タクシーで行ける辺の数
C=[INF]*(N+1)
R=[0]*(N+1)
for j in range(1,N+1):
    C[j],R[j]=MI()
# K この町とこの町との関係
Edge=[[] for _ in range(0,N+1)]
for j in range(0,K):
    a,b=MI()
    Edge[a].append(b)
    Edge[b].append(a)
# タクシー運賃と行ける町の数
for j in range(1,N+1):
    xdebug(f"町 {j}-> コスト{C[j]} -> 行ける数{R[j]}")
# 各町ごとの関係
for j in range(1,N+1):
    xdebug(f"町 {j} の関係 {Edge[j]}")

# 各町からの距離を求める->深さ優先探索
def bfs(start):
    q=deque([start])
    dist=[INF]*(N+1)
    dist[start]=0
    while len(q)!=0:
        v = q.popleft()
        for w in Edge[v]:
            if dist[w]!=INF:
                continue
            dist[w]=dist[v]+1
            q.append(w)
    return dist
dist_mat=[[INF]*(N+1)]
for j in range(1,N+1):
    d = bfs(j)
    dist_mat.append(d)
    xdebug(f"町 {j} の距離関係 {d}")
G=Dijkstra()
xdebug("町との相性を見てみる")
for j in range(0,N+1):
    xdebug(f"{j}->{dist_mat[j]}")
for j in range(1,N+1):
    capa=R[j]
    for k in range(1,N+1):
        realDist=dist_mat[j][k]
        xdebug(f"Check {j}の広さ{capa},{k}の位置{realDist}")
        if realDist <= capa:
            xdebug(f"町 {j} -> 町 {k} は行ける")
            G.add(j,k,C[j],True)
        else:
            xdebug(f"町 {j} -> 町 {k} は行けない")
            G.add(j,k,INF,True)
for j in range(1,N+1):
    xdebug(f"G.e[{j}]={G.e[j]}")
d,_=G.Dijkstra_search(1)
print(d[N])
shortestPath=G.getDijkstraShortestPath(1,N)
print(f"最短パス->{shortestPath}")
