import sys
import pysnooper
read=sys.stdin.buffer.read
readline=sys.stdin.buffer.readline
readlines=sys.stdin.buffer.readlines

from collections import deque
from heapq import heappop,heappush

N,K=map(int,readline().split())
m=map(int,read().split())
data=list(zip(m,m))
CR=data[:N]
AB=data[N:]
graph = [[] for _ in range(N+1)]
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)
INF=10**10
# @pysnooper.snoop()
def bfs(start):
    q=deque([start])
    dist=[INF]*(N+1)
    dist[start]=0
    while len(q)!=0:
        v=q.popleft()
        for w in graph[v]:
            if dist[w]!=INF:
                continue
            dist[w]=dist[v]+1
            q.append(w)
    return dist

dist_mat=[[INF]*(N+1)]+[bfs(j) for j in range(1,N+1)]
for j1 in range(1,N+1):
    c,r=CR[j1-1]
    for j in range(1,N+1):
        if dist_mat[j1][j]<r:
            dist_mat[j1][j]=c
        else:
            dist_mat[j1][j]=INF

for j in range(1,N+1):
    print(dist_mat[j][1:])
dist=[INF]*(N+1)
q=[(0,1)]
dist[0]=0
while len(q)!=0:
    dv,v=heappop(q)
    if dist[v]<dv:
        continue
    if v==N:
        break
    for w in range(1,N+1):
        dw=dv+dist_mat[v][w]
        if dist[w]<=dw:
            continue
        dist[w]=dw
        heappush(q,(dw,w))

print("---distのリスト---")
print(dist[1:])
answer=dist[N]
print("---解答---")
print(answer)
