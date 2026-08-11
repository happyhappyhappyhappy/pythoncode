N = int(input())
S = input()
ans = 0
k = 0
for i in range(N):
    if S[i] == "x":
        k += 1
        ans += 1
        print(ans)
    else:
        ans += 1
if k < N:
    for _ in range(N - k):
        print(N)
