import itertools
import collections

N = int(input())
A = list(map(int, input().split()))
AC = [0]+list(itertools.accumulate(A))
C = collections.Counter(AC)
ans = 0
for v in C.values():
    ans += v*(v-1)//2
print(ans)
