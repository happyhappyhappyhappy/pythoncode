import sys
input2 = sys.stdin.readline
from collections import deque

N = int(input2())
GRAPH= [ deque([]) for _ in range(N+1) ]
# print(len(GRAPH))
# print(GRAPH)
for _ in range(N):
    u,k,*v = [int(x) for x in input2().split()]
    v.sort()
    for i in v:
        GRAPH[u].append(i)
time = 0

print(GRAPH)

time=0
arrive=[False]*(N+1) # 付いたか否か
finish_time=[-1]*(N+1)

def dfs(v):
    global time # dfs関数内でtime関数を使いたい
    # time = time+1
    stack = [v]
    # print("stack={}".format(stack))
    arrive[v] = True # time->1
    # arrive_time[v]=time
    while stack:
        v = stack[-1]
        # print("now stack={}".format(stack))
        if GRAPH[v]:
            w = GRAPH[v].popleft()
            if not arrive[w]:
                arrive[w]=True
                stack.append(w)
        else:
            time=time+1
            finish_time[v]=time
            stack.pop()
    return finish_time

for i in range(N):
    if not arrive[i]:
        ans = dfs(i+1)

for j in range(N):
    temp = [j+1,ans[j+1]]
    print(*temp)
