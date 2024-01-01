# ライブラリのインポート
import sys
# import heapq,copy
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

class BellmanFord():
    def __init__(self,N):
        self.N=N
        self.edges=[]
    def add(self,u,v,d,directed=False):
        if directed is False:
            self.edges.append([u,v,d])
            self.edges.append([v,u,d])
        else:
            self.edges.append([u,v,d])
    def BellmanFord_search(self,s):
        d = [float('inf') for _ in range(0,self.N)]
        d[s]=0
        numEdges=len(self.edges)
        while True:
            update=False
            for j in range(0,numEdges):
                e = self.edges[j]
                x = d[e[0]]+e[2]
                if d[e[0]]!=float('inf') and x < d[e[1]]:
                    d[e[1]]=x
                    update=True
            if update is False:
                break
        return d
    def BellmanFord_negative_bool(self,start,numNodes):
        d = [float('inf') for _ in range(0,self.N)]
        d[start]=0
        numEdges = len(self.edges)
        for j in range(0,numNodes):
            for k in range(0,numNodes):
                e = self.edges[k]
                x = d[e[0]]+e[2]
                if x < d[e[1]]:
                    d[e[1]]=x
                    if j == numNodes-1:
                        return True,d
        return False,d
