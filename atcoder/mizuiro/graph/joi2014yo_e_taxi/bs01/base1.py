import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import deque
from heapq import heappop, heappush

N,K = map(int,readline().split())
m = map(int,read().split())
data = list(zip(m,m))
CR = data[:N]
AB = data[N:]

graph = [[] for _ in range(N+1)]
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)

INF = 10 ** 10

def bfs(start):
    q = deque([start])
    dist = [INF] * (N+1)
    dist[start] = 0
    while q:
        v = q.popleft()
        for w in graph[v]:
            if dist[w] != INF:
                continue
            dist[w] = dist[v] + 1
            q.append(w)
    return dist

dist_mat = [[INF] * (N+1)] + [bfs(i) for i in range(1,N+1)]

for i in range(1,N+1):
    c,r = CR[i - 1]
    for j in range(1,N+1):
        dist_mat[i][j] = c if dist_mat[i][j] <= r else INF

dist = [INF] * (N+1)
q = [(0,1)]
dist[0] = 0
while q:
    dv,v = heappop(q)
    if dv > dist[v]:
        continue
    if v == N:
        break
    for w in range(1,N+1):
        dw = dv + dist_mat[v][w]
        if dw >= dist[w]:
            continue
        dist[w] = dw
        heappush(q, (dw,w))

answer = dist[N]
print(answer)
