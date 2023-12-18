# ライブラリのインポート
import sys
import heapq
import pprint as pp
from collections import deque,defaultdict
import queue
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
        if directed is False:
            self.e[u].append([v,d])
            self.e[v].append([u,d])
        else:
            self.e[u].append([v,d])
    def delete(self,u,v):
        self.e[u]=[_ for _ in self.e[u] if _[0]!=v]
        self.e[v]=[_ for _ in self.e[v] if _[0]!=u]
    def Dijkstra_search(self,s):
        d=defaultdict(lambda: float('inf'))
        prev=defaultdict(lambda: None)
        v=defaultdict(bool)
        d[s]=0
        q=[]
        heapq.heappush(q, (0,s))
        while len(q)!=0:
            k,u=heapq.heappop(q)
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
                    heapq.heappush(q,(vd,uv))
        return d,prev
    def getDijkstraShortestPath(self,start,goal):
        _,prev=self.Dijkstra_search(start)
        shortestPath=[]
        node=goal
        while node is not None:
            shortestPath.append(node)
            node=prev[node]
        return shortestPath[::-1]

# N 都市の数,M 道路,K ゾンビの数,S ゾンビから危険な範囲
N,M,K,S=MI()
# P 安全都市の宿泊 Q 危険都市の宿泊
P,Q=MI()
LINKS=[[] for _ in range(0,N+1)]
q=queue.Queue()
ZOMBIE=[False]*(N+1)
for j in range(0,K):
    x = II()
    q.put(x)
    ZOMBIE[x]=True
danger=[False]*(N+1)
for j in range(0,M):
    a,b=MI()
    LINKS[a].append(b)
    LINKS[b].append(a)
# for j in range(1,N+1):
#     xdebug(f"都市{j}->{LINKS[j]}")
for j1 in range(0,S+1):
#    xdebug(f"ゾンビの範囲 {j1} で検索する")
    if q.empty()==True:
        break
    qsize=q.qsize()
#    xdebug(f"ゾンビ存在queueの中身は {qsize} です")
    for j in range(qsize-1,-1,-1):
        f = q.get()
        if danger[f]==True:
#            xdebug(f"都市 {f} はすでに危険対象都市です")
            continue
#        xdebug(f"都市 {f} を危険としてマークしました")
        danger[f]=True
        for t in LINKS[f]:
            q.put(t)
# xdebug("----危険確認-----")
# for j in range(1,N+1):
#     if danger[j]==True:
#         xdebug(f"都市 {j} -> 危険")
#     else:
#         xdebug(f"都市 {j} -> 安全")
G=Dijkstra()
for j in range(1,N+1):
    for x in LINKS[j]:
        cost=0
        if x == 1 or x ==N:
            cost=0
        elif danger[x] == True:
            cost=Q
        else:
            cost=P
#        xdebug(f"{j}->{x}へ行くのに{x}に止まるコスト{cost}")
        # LINKS変数は最初の取得時に往復させている。有向グラフの集まりと見て処理をする。
        G.add(j,x,cost,True)
# for j in range(1,N+1):
#     for x in G.e[j]:
#         xdebug(f"都市 {j} の接続先と宿泊費-> {x}")

d,_=G.Dijkstra_search(1)
print(d[N])
