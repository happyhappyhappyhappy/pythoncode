import sys
# from collections import defaultdict
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

N,M = MI() # N->スイッチ M->ランプ
G = list()
for x in range(M):
    G.append(LI())
ODDCHECK = LI()

# 加工
# 各行先頭を削る
for x in range(M):
    G[x]=G[x][1:]
    # 他に G[x].pop(0)
    # del G[x][0]
print(G)
for x in range(M):
    x_Length = len(G[x])
    for y in range(x_Length):
        G[x][y] = G[x][y]-1
