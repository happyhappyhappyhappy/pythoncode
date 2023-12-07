import collections
import heapq

class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d, directed=False):
        """
        #0-indexedでなくてもよいことに注意
        #u = from, v = to, d = cost
        #directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.e[u].append([v, d])
            self.e[v].append([u, d])
        else:
            self.e[u].append([v, d])

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

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
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

N,M = map(int, input().split())
ABC = [list(map(int, input().split())) for i in range(M)]
ME = [float('inf')]*N #自身から自身へ直接向かうコスト
graph = Dijkstra()
for a,b,c in ABC:
    if a==b:
        ME[a-1] = min(ME[a-1],c)
    else:
        graph.add(a-1,b-1,c,True)
#それぞれの街のダイクストラの結果を保持
CityD = []
for i in range(N):
    d,_ = graph.Dijkstra_search(i)
    CityD.append(d)
for i in range(N):
    #ansの初期値を自身から自身へ直接向かうコストとする
    #ちなみに、ダイクストラ内のアルゴリズムを少し編集することで、
    #自身に戻る距離を別で計算しなくてもよくなる方法もあります。
    #https://atcoder.jp/contests/abc191/submissions/22189422
    ans = ME[i]
    for j in range(N):
        if i!=j:#自身の距離は0のため、見ない
            ans = min(ans,CityD[i][j]+CityD[j][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
