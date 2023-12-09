import collections
import heapq


class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d, k, directed=False):
        """
        #0-indexedでなくてもよいことに注意
        #u = from, v = to, d = cost
        #directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.e[u].append([v, d, k])
            self.e[v].append([u, d, k])
        else:
            self.e[u].append([v, d, k])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):
        """
        #0-indexedでなくてもよいことに注意
        #:param s: 始点
        #:return: 始点から各点までの最短経路と最短経路を求めるのに必要なprev
        """
        d = collections.defaultdict(lambda: float('inf'))
        prev = collections.defaultdict(lambda: None)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud, uk in self.e[u]:
                k = d[u]#たどり着いた時間
                k = -(-k//uk)*uk#次の出発時刻に変換
                vd = k+ud#到達時間
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    v[u] = False #行先の時刻が更新され、再チェックしたいのでFalseに戻す
                    heapq.heappush(q, (vd, uv))

        return d, prev

    def getDijkstraShortestPath(self, start, goal):
        _, prev = self.Dijkstra_search(start)
        shortestPath = []
        node = goal
        while node is not None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]

N,M,X,Y = map(int, input().split())
ABTK = [list(map(int, input().split())) for i in range(M)]
d = Dijkstra()
for a, b, t, k in ABTK:
    d.add(a, b, t, k)
dx,_ = d.Dijkstra_search(X)
if dx[Y]==float('inf'):
    print(-1)
else:
    print(dx[Y])
