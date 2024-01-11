import itertools
N,Q = map(int, input().split())
TABLE = [0]*(N+1)
for i in range(Q):
    l,r = map(int, input().split())
    l-=1
    r-=1
    TABLE[l]+=1
    TABLE[r+1]-=1
AC = list(itertools.accumulate(TABLE))
OSERO = []
for i in range(N):
    OSERO.append(AC[i]%2)
print(''.join(map(str, OSERO)))
