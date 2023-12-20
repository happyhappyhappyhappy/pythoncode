# ライブラリのインポート
import sys
import heapq
import queue
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
        v=defaultdict(bool)
        d[s]=0
        q=[]
        heapq.heappush(q,(0,s))
        while len(q)!=0:
            k,u = heapq.heappop(q)
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

# N: 町の数
# M: 道路の数
# K: ゾンビの数
# S: ゾンビから危険な範囲
N,M,K,S=MI()
# P: 安全町での宿泊料金
# Q: 危険町での宿泊料金
P,Q = MI()
LINKS=[[] for _ in range(0,N+1)]
q=queue.Queue()
# ZOMBIEPLACE: ゾンビが存在する町 移動できない(コストMAX)
# Dijkstraの設定時に使う
ZOMBIEPLACE=[]
# ZOMBIE: ゾンビ有無を確認するリスト
ZOMBIE=[False]*(N+1)
