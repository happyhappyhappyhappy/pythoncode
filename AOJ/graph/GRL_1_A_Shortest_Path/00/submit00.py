# ライブラリのインポート
import sys
import heapq
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

def now_pq(lst):
    ln=len(lst)
    xdebug("今の優先度キューの中身")
    for j in range(0,ln):
        d , pos = lst[j]
        xdebug(f" {j+1}: 方向{pos} へ コスト{d}")
class Dijkstra():
    def __init__(self):
        self.e=defaultdict(list)
    def add(self,u,v,d,directed=False):
        if directed==False:
            self.e[u].append([v,d])
            self.e[v].append([u,d])
        else:
            self.e[u].append([v,d])
    def delete(self,u,v):
        self.e[u]=[_ for _ in self.e[u] if _[0] != v]
        self.e[v]=[_ for _ in self.e[v] if _[0] != u]
    def Dijkstra_search(self,s):
        d = defaultdict(lambda: MAXSIZE)
        prev = defaultdict(lambda: None)
        d[s]=0
        pq= []
        heapq.heappush(pq,(0,s))
        v = defaultdict(bool)
        while len(pq)!=0:
#            now_pq(pq)
            k,u = heapq.heappop(pq)
            if v[u] == True:
 #               xdebug(f" pos = {u} は フラグがついているため飛びます")
                continue
            v[u]=True
            for uv,ud in self.e[u]:
                if v[uv] == True:
#                    xdebug(f" pos = {uv} は フラグがついているため飛びます")
                    continue
                vd = k + ud
                if (k + ud) < d[uv]:
                    d[uv]=k+ud
                    prev[uv]=u
                    heapq.heappush(pq,(vd,uv))
                # else:
                #     xdebug(f"{u}->{v}へは最短の距離が見つからないためキュー処理は無し")
        return d,prev
    def getDijkstraShortestPath(self,start,goal):
        _,prev = self.Dijkstra_search(start)
        shortestPath = []
        node = goal
        while node != None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]

V,E,r = MI()
G=Dijkstra()
for j in range(0,E):
    s,t,d=MI()
    G.add(s,t,d,True)
d,prev=G.Dijkstra_search(r)
for j in range(0,V):
    x = d[j]
    if x == MAXSIZE:
        print("INF")
    else:
        print(x)
# for j in range(0,V):
#     sp = G.getDijkstraShortestPath(r,j)
#     xdebug(f"{r} -> {j} への パス {sp}")
