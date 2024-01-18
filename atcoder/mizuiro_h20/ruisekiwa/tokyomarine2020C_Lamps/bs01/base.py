import itertools
N,K = map(int, input().split())
LAMP = list(map(int, input().split()))
for i in range(K):
    TABLE = [0]*(N+1)
    for j in range(N):
        TABLE[max(0,j-LAMP[j])]+=1
        TABLE[min(N,j+LAMP[j]+1)]-=1
    print(f"TABLE->{TABLE}")
    LAMP = list(itertools.accumulate(TABLE))
    #K回まで全て頼むとTLEすることがあるため、最大の強さになった場合は打ち切る
    if LAMP[0]==N and LAMP[N-1]==N:
        break
print(*LAMP[:N])
