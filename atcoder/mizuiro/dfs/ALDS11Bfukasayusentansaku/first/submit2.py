import sys
input2=sys.stdin.readline
from collections import deque
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1
# 全体の値
N = int(input2())
# グラフのひな形作成
G = [deque([]) for _ in range(N+1)]
# print("G={}".format(G))
# グラフ情報
for _ in range(N):
    u,k,*vs = [int(x) for x in (input2().split())]
    vs.sort()
    for x in vs:
        G[u].append(x)

# 時刻計測初期化
time = 0
arrival_times=[-1]*(N+1)
finish_times=[-1]*(N+1)

# 深さ優先探索
def dfs(x):
    global time
    time = time+1
    stack = [x]
    arrival_times[x] = time
    while not len(stack) > 1: # stack変数に何も残っていなければ終了
        y = stack[len(stack)-1] # 最後の値
        print(G[y])
        if G[y]:
            z = G[y].popleft()
            if arrival_times[z] < 0:
                time = time+1
                arrival_times[z]=time
                stack.append(z)
        else:
            time=time+1
            finish_times[y]=time
            stack.pop()
    return [arrival_times,finish_times]
# TODO:ここから始める 2022年12月8日
