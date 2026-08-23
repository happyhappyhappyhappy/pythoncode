N=int(input())
A=list(map(int,input().split()))

N+=1
A.append(0)
A.sort()
P=A.index(0)
print(A)
print(f"0の座標は {P}")
L=P-1
R=P+1
ans=0

pos=0
for _ in range(N-1):
    if L==-1:
        print("左に行きすぎ L=-1")
        ans=ans+(A[R]-pos)
        pos=A[R]
        R+=1
        print(f"R={R}")
    elif R==N:
        print(f"右に行きすぎ R={N}")
        ans+=pos-A[L]
        pos=A[L]
        L-=1
        print(f"L={L}")
    elif pos-A[L]<=A[R]-pos:
        print("マイナス側が近いよ")
        ans+=pos-A[L]
        pos=A[L]
        L-=1
        print(f"L={L}")
    else:
        print("プラス側が近いよ")
        ans+=A[R]-pos
        pos=A[R]
        R+=1
        print(f"R={R}")
 
print(ans)
