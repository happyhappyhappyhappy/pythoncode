N, C = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]

days = set()
for a, b, c in ABC:
    if a not in days:
        days.add(a)
    if b + 1 not in days:
        days.add(b + 1)
days = sorted(list(days))

dict = {x:i for i, x in enumerate(days)}

acc = [0] * (len(days))
for a, b, c in ABC:
    acc[dict[a]] += c
    acc[dict[b + 1]] -= c

for i in range(len(days) - 1):
    acc[i + 1] += acc[i]

ans = 0
for i in range(len(days) - 1):
    ans += min(C, acc[i]) * (days[i + 1] - days[i])

print(ans)
