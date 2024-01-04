import itertools

class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)]
                  for i in range(N)]  # d[u][v] : 辺uvのコスト(存在しないときはinf)

    def add(self, u, v, c, directed=False):
        """
        0-indexedであることに注意
        u = from, v = to, c = cost
        directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.d[u][v] = c
            self.d[v][u] = c
        else:
            self.d[u][v] = c

    def WarshallFloyd_search_result(self):
        #不要であればFalseとする
        USE = [[True] * N for i in range(N)]

        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):

                    #矛盾
                    if self.d[i][j] > self.d[i][k] + self.d[k][j]:
                        return -1
                    #不要となるコストを引く
                    if self.d[i][j] == self.d[i][k] + self.d[k][j] and i!=k and k!=j:
                        USE[i][j]=False
        #総コスト
        ans = 0
        for i in range(self.N):
            for j in range(self.N):
                if USE[i][j]:
                    ans+=self.d[i][j]
        #行き来で2回カウントしているため、半分にして返却
        return ans//2

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
graph = WarshallFloyd(N)
for i in range(N):
    for j in range(N):
        graph.add(i, j, A[i][j], True)#Trueにする必要はないけれど気持ち的に
print(graph.WarshallFloyd_search_result())
