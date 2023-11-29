# ライブラリのインポート
import sys
# import heapq,copy
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
        self.e=defaultdict(list)
    def add(self,u,v,d,directed=False):
        if directed == False:
            self.e[u].append([v,d])
            self.e[v].append([u,d])
        else:
            self.e[u].append([v,d])
    def delete(self,u,v):
        self.e[u]=[_ for _ in self.e[u] if _[0] != v]
        self.e[v]=[_ for _ in self.e[v] if _[0] != u]
    # def Dijkstra_search(self,s):
    #     d = defaultdict(lambda: float('inf'))
    #     prev = defaultdict(lambda: None)
    #     d[s]=0
    #     q = []
    #     heapq.heappush(q,(0,s))
    #     v = defaultdict(bool)
    #     while len(q)!=0:
    #         k,u = heapq.heappop(q)
    #         if v[u] == True:
    #             continue
    #         v[u]=True
    #         for uv,ud in self.e[u]:
    #             if v[uv]==True:
    #                 continue
    #             vd = k + ud
    #             if vd < d[uv]:
    #                 d[uv]=vd
    #                 prev[uv]=u
    #                 heapq.heappush(q,(ud,uv))
    #     return d,prev
    def Dijkstra_search(self, s):
        """
        #0-indexedでなくてもよいことに注意
        #:param s: 始点
        #:return: 始点から各点までの最短経路と最短経路を求めるのに必要なprev
        """
        d = defaultdict(lambda: float('inf'))
        prev = defaultdict(lambda: None)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    heapq.heappush(q, (vd, uv))

        return d, prev
    def getDijkstraShortestPath(self,start,goal):
        _,prev=self.Dijkstra_search(start)
        shortestPath=[]
        node=goal
        while node != None:
            shortestPath.append(node)
            node=prev[node]
        return shortestPath[::-1]
    def __str__(self):
        ret = "\n".join(f" {r} : {m}" for r,m in self.e.items())
        return ret

V,E,r=MI()
G=Dijkstra()
for _ in range(0,E):
    a,b,c = MI()
    G.add(a,b,c,True)
print(G)
d,prev=G.Dijkstra_search(r)
print("---- d value -----")
for k,v in d.items():
    print(f"{k}: {v}")
print("---- prev value -----")
for k,v in prev.items():
    print(f"{k}:{v}")
for j in range(0,V):
    x = G.getDijkstraShortestPath(r,j)
    print(f"{r}->{j}->{x}")
