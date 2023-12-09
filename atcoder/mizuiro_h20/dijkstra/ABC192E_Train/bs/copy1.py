# ライブラリのインポート
import sys
import heapq
import pprint as pp
from collections import defaultdict
import os
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

class Dijkstra():
    def __init__(self):
        self.e=defaultdict(list)
    def add(self,u,v,d,k,directed=False):
        if directed is False:
            self.e[u].append([v,d,k])
            self.e[v].append([u,d,k])
        else:
            self.e[u].append([v,d,k])
    def delete(self,u,v):
        self.e[u]=[x for x in self.e[u] if x[0]!=v]
        self.e[v]=[x for x in self.e[v] if x[0]!=u]
    def Dijkstra_search(self,s):
        d = defaultdict(lambda: float('inf'))
        prev = defaultdict(lambda: None)
        d[s]=0
        q = []
        heapq.heappush(q, (0,s))
        v = defaultdict(bool)
        while len(q)!=0:
            k,u = heapq.heappop(q)
            if v[u]==True:
                continue
            v[u]=True
            for uv,ud,uk in self.e[u]:
                k = d[u]
                k = -(-k//uk)*uk
                vd = k + ud
                if vd < d[uv]:
                    d[uv]=vd
                    prev[uv]=u
                    v[u]=False
                    heapq.heappush(q, (vd,uv))
        return d,prev
    def getDijkstraShortestPath(self,start,goal):
        _,prev=self.Dijkstra_search(start)
        shortestPath=[]
        node=goal
        while node is not None:
            shortestPath.append(node)
            node=prev[node]
        return shortestPath[::-1]

N,M,X,Y=MI()
ABTK=[]
for _ in range(0,M):
    ABTK.append(LI())
G = Dijkstra()
for a,b,t,k in ABTK:
    G.add(a,b,t,k)
dx,_=G.Dijkstra_search(X)
if dx[Y]==float('inf'):
    print("-1")
else:
    print(dx[Y])
