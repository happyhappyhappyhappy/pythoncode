import sys

input = sys.stdin.readline
n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x - 1, y - 1))
xy.sort()
min_val = n
ans = 0
for x, y in xy:
    min_val = min(min_val, y)
    ans += min_val == y
print(ans)
