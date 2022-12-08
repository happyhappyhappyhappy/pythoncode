import sys
input2 = sys.stdin.readline
from collections import deque

N = int(input2())
GRAPH= [ deque([]) for _ in range(N+1) ]
# print(len(GRAPH))
# print(GRAPH)
for _ in range(N):
    u, k, * v = [int(x) for x in input().split()]
    # u,k,*v = [int(x) for x in input2().split()]
    v.sort()
    
    for j in v:
        print("j={} u={}".format(j,u))
        GRAPH[u].append(j)
time = 0

print(GRAPH)

time=0
arrive_time=[-1]*(N+1)
finish_time=[-1]*(N+1)

def dfs(v):
    global time # dfs関数内でtime関数を使いたい
    time = time+1
    stack = [v]
    # print("stack={}".format(stack))
    arrive_time[v] = 1 # time->1
    # arrive_time[v]=time
    while stack:
        v = stack[-1]
        # print("now stack={}".format(stack))
        if GRAPH[v]:
            w = GRAPH[v].popleft()
            if arrive_time[w] < 0:
                # time = time+1
                arrive_time[w] = 1
                stack.append(w)
        else:
            time=time+1
            finish_time[v]=time
            stack.pop()
    return arrive_time

for i in range(N):
    if arrive_time[i+1] < 0:
        ans = dfs(i+1)

for j in range(N):
    temp = [j+1,ans[j+1]]
    print(*temp)
