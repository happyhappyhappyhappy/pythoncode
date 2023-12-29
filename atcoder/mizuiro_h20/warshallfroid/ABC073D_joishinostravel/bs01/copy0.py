import itertools
class WarshallFloyd():
    def __init__(self,N):
        self.N=N
        self.d=[[float("inf") for j in range(N)]
        for k in range(N)]
    def add(self,u,v,c,directed=False):
        if directed is False:
            self.d[u][v]=c
            self.d[v][u]=c
        else:
            self.d[u][v]=c
    def WarshallFloyd_search(self):
        for k in range(0,self.N):
            for i in range(0,self.N):
                for j in range(0,self.N):
                    x = self.d[i][k]+self.d[k][j]
                    self.d[i][j]=min(self.d[i][j],x)
        hasNegativeCycle=False
        for j in range(0,self.N):
            if self.d[j][j]<0:
                hasNegativeCycle=True
                break
        for j in range(0,self.N):
            self.d[j][j]=0
        return hasNegativeCycle,self.d

N,M,R = map(int,input().split())
RL = list(map(int,input().split()))
ABC = [list(map(int,input().split())) for j in range(0,M)]
graph = WarshallFloyd(N+1)
for a,b,c in ABC:
    graph.add(a,b,c,False)

hasNegativeCycle,d=graph.WarshallFloyd_search()
ans=float('inf')
for r in list(itertools.permutations(RL)):
    cost = 0
    for j in range(R-1):
        cost=cost+d[r[j]][r[j+1]]
    ans = min(cost,ans)
print(ans)
