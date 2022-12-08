import sys
input2 = sys.stdin.readline
from collections import deque
# TODO: ハンドコピペをもう一回見ながら行う
N = int(input2())
graph = [deque([]) for _ in range(N+1)]
for _ in range(N):
    u,k,*v = [int(x) for x in input2().split()]
    v.sort()
    # print("v = {}".format(v))
    for j in v:
        # print("j={} u={}".format(j,u))
        graph[u].append(j)

time=0
arrive_time = [-1] * (N+1)
finish_time = [-1] * (N+1)

def dfs(x):
    global time
    time = time+1
    stack = [x]
    arrive_time[x] = time
    while stack:
        y = stack[-1]
        if graph[y]:
            w = graph[y].popleft()
            if arrive_time[y] < 0:
                time = time+1
                arrive_time[y] = time
                stack.append(w)
        else:
            time=time+1
            finish_time[y] = time
            stack.pop()
    return [arrive_time,finish_time]

for j in range(N):
    if arrive_time[j+1]<0:
        ans=dfs(j+1)

for j in range(N):
    temp = [j+1,ans[0][j+1],ans[1][j+1]]
    print(*temp)
