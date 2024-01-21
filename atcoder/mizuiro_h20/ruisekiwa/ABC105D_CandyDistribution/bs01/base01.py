import itertools
import collections

N,M = map(int, input().split())
A =  list(map(int, input().split()))
#間に合わない可能性もあるので、modとりながら累積和とる方が安全です
AC = list(itertools.accumulate(A))+[0]
for i in range(N+1):
    AC[i]=AC[i]%M
ACC = collections.Counter(AC)
ans = 0
for v in ACC.values():
    ans+=v*(v-1)//2
print(ans)
