import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9) #再帰回数の限界を変更

N = int(input())
C = [0] + list(map(int, input().split()))
L = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

ANS = [True]*(N+1)#全てが良い頂点として初期化、良くない頂点をFalseにしていく
ANS[0] = False#0は添え字のミスが起きないように置いただけなのでFalseに

DC = [0]*(max(C)+1)#現在位置にたどり着くまでにどの色が何回あったか
REACHE = [False]*(N+1)#既に到達したか

def dfs(A):
    if DC[C[A]]>0:
        ANS[A]=False#同じ色が存在する
    DC[C[A]]+=1
    REACHE[A]=True
    for l in L[A]:
        if REACHE[l]==0:
            dfs(l)#到達してない先なので潜る
    DC[C[A]]-=1#一つ上に戻るため現地点の色の数を減らす

dfs(1)
for i in range(N+1):
    if ANS[i]:
        print(i)
