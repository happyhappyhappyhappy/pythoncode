import sys
sys.setrecursionlimit(10 ** 9) #再帰回数の限界を変更

def dfs(A):
    global ans
    # 数列の長さが N に達したら計算

    if len(A) == N:
        score = 0
        for i in range(Q):
            if A[L[i][1]-1]-A[L[i][0]-1]==L[i][2]:
                score += L[i][3]
        ans = max(ans,score)
        return
    for v in range(A[-1],M+1):
        dfs(A+[v])

N,M,Q = map(int, input().split())
L = []
for i in range(Q):
    L.append(list(map(int, input().split())))
ans = 0
dfs([1])
print(ans)
