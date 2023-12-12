# ライブラリのインポート
import sys
import heapq,copy
import pprint as pp
from collections import defaultdict
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
def kiriage_kun(X,d):
    ans = ((X+d-1)//d)*d
    return ans
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
        d=defaultdict(lambda: float('inf'))
        prev=defaultdict(lambda: None)
        d[s]=0
        q=[]
        heapq.heappush(q,(0,s))
        v=defaultdict(bool)
        while len(q)!=0:
            k,u=heapq.heappop(q)
            if v[u] is True:
                continue
            v[u]=True
            for uv,ud,uk in self.e[u]:
                nowstop = d[u]
                nextstart = kiriage_kun(nowstop,uk)
                vd=nextstart+ud
                if vd < d[uv]:
                    # xdebug(f"頂点{u}->頂点{uv}に至るコスト、d[{uv}]に新たな値{vd}をセットします")
                    d[uv]=vd
                    prev[uv]=u
                    # xdebug(f"もう一回頂点{u}にあるフラグ{v[u]}を外します")
                    v[u]=False
                    heapq.heappush(q,(vd,uv))
        return d,prev
    def getDijkstraShortestPath(self,start,goal):
        _,prev=self.Dijkstra_search(self,start)
        shortestPath=[]
        node=goal
        while node is not None:
            shortestPath.append(node)
            node=prev[node]
        return shortestPath[::-1]

N,M,X,Y = MI()
G=Dijkstra()
for _ in range(0,M):
    fm,to,cost,tkeep=MI()
    G.add(fm,to,cost,tkeep)
# for j in range(1,N+1):
#     print(f"{j}->{G.e[j]}")
d,prev=G.Dijkstra_search(X)
ans=d[Y]
if ans == float('inf'):
    print("-1")
else:
    print(ans)
