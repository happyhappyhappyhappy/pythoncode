# ライブラリのインポート
import sys
import heapq
from collections import defaultdict
import pprint as pp
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
        self.e = defaultdict(list)
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
        heapq.heappush(q, (0,s))
        v=defaultdict(bool)
        while len(q)!=0:
            k,u=heapq.heappop(q)
            if v[u] is True:
                continue
            v[u]=True
            for uv,ud in self.e[u]:
                if v[uv] is True:
                    continue
                vd=k+ud
                if vd < d[uv]:
                    d[uv]=vd
                    prev[uv]=u
                    heapq.heappush(q,(vd,uv))
        return d,prev
    def getDijkstraShortestPath(self,start,goal):
        _,prev=self.Dijkstra_search(start)
        shortestPath=[]
        node = goal
        while node is not None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]
N,M=MI()
G=Dijkstra()
EQ=[float('inf')]*(N+1)
for j in range(0,M):
    a,b,c=MI()
    if a==b:
        EQ[a]=min(EQ[a],c)
    else:
        G.add(a,b,c,True)
TABLE=[[float('inf')]*(N+1) for _ in range(0,N+1)]
for j in range(1,N+1):
    d,_=G.Dijkstra_search(j)
    for k in range(1,N+1):
        TABLE[j][k]=d[k]

ANS=[float('inf')]*(N+1)
for j in range(1,N+1):
    for k in range(1,N+1):
        if j!=k:
            ANS[j]=min(TABLE[j][k]+TABLE[k][j],ANS[j])
        else:
            ANS[j]=min(ANS[j],EQ[j])
for j in range(1,N+1):
    if ANS[j] == float('inf'):
        print("-1")
    else:
        print(ANS[j])
