n,m=map(int,input().split())

s=[[]for i in range(m)]

for i in range(m):
    s[i]=list(map(int,input().split()))[1:]

p=list(map(int,input().split()))
ans=0
for i in range(2**n):
    on=0
    for j in range(m):
        count=0
        for k in range(len(s[j])):
            if (1<<s[j][k]-1) & i:
                count+=1
        if count%2==p[j]:
            on+=1
    if on==m:
        ans+=1

print(ans)
