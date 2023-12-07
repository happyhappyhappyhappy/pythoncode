# ライブラリのインポート
import sys
# import heapq,copy
import heapq
import pprint as pp
from collections import defaultdict
import os
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
    def add(self,u,v,d,directed=False):
        if directed == False:
            self.e[u].append([v,d])
            self.e[v].append([u,d])
        else:
            self.e[u].append([v,d])
    def delete(self,u,v):
        self.e[u]=[_ for _ in self.e[u] if _[0]!=v]
        self.e[v]=[_ for _ in self.e[v] if _[1]!=v]
    def Dijkstra_search(self,s):
        d = defaultdict(lambda: float('inf'))
        prev = defaultdict(lambda: None)
        d[s]=0
        q=[]
        heapq.heappush(q,[0,s])
        v = defaultdict(bool)
        while len(q)!=0:
            k,u = heapq.heappop(q)
            if v[u]==True:
                continue
            v[u]=True
            for uv,ud in self.e[u]:
                if v[uv]==True:
                    continue
                vd = k+ud
                if vd < d[uv]:
                    d[uv]=vd
                    prev[uv]=u
                    heapq.heappush(q,(vd,uv))
        return d,prev

    def getDijkstraShortPath(self,start,goal):
        _,prev=self.Dijkstra_search(start)
        shortestPath=[]
        node=goal
        while node != None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]

N,M = MI()
G = Dijkstra()
ABC=[MI() for j in range(0,N)]
ME=[float('inf')]*N
for a,b,c in ABC:
    if a == b:
        ME[a-1]=c
    else:
        a = a-1
        b = b-1
        G.add(a,b,c,True)
CityD=[]
for j in range(0,N):
    d,_=G.Dijkstra_search(j)
    CityD.append(d)
for j in range(0,N):
    ans = ME[j]
    for k in range(N):
        if j!=k:
            ans = min(ans,CityD[j][k]+CityD[k][j])
    if ans == float('inf'):
        print("inf")
    else:
        print(ans)
