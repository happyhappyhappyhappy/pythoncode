from collections import deque
import heapq
INF = 10**20

N,M,K,S = map(int,input().split())
P,Q = map(int,input().split())

zombie = []
for k in range(K):
    zombie.append(int(input())-1)

link = [ [] for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    link[a-1].append(b-1)
    link[b-1].append(a-1)

dist = [INF] * N
q = deque(zombie)
for v in zombie:
    dist[v] = 0
while q:
    node = q.popleft()
    for next in link[node]:
        if dist[next] != INF: # 探索済みの場合はパスされる。、
            continue          # distは小さい順にqに格納されるので、ゾンビからの最小距離を求めることがd系る
        dist[next] = dist[node] + 1
        q.append(next)

cost = [P] * N
for n in range(N):
    if dist[n] <= S:
        cost[n] = Q
    if n in zombie:
        cost[n] = INF
    if n==0 or n==N-1:
        cost[n] = 0

def dijkstra(s, g):
    dists  = [INF for i in range(N)]
    dists[s] = 0
    pq = [(0, s)] # 優先度付きキューのオブジェクトそのものはただのリスト
    while(pq[0][1]!=g):
        d, node = heapq.heappop(pq)
        if (d > dists[node]): # 探索の対象にする必要があるか確認
            continue
        for next in link[node]:
            c = cost[next]
            if d + c < dists[next]: # 探索の対象にする必要があるか確認
                dists[next] = d + c
                heapq.heappush(pq, (dists[next],next))
    return pq[0][0]
print (dijkstra(0,N-1))
