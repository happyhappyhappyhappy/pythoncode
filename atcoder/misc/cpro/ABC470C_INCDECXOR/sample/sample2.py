#ABC470_20260808_C
N,Q=map(int,input().split())
L=[0]*N
XOR=0
S=set()
for _ in range(Q):
    x=list(map(int,input().split()))
    if(x[0]==1):
        x[1]-=1
        A=L[x[1]]
        L[x[1]]+=1
        XOR^=A
        XOR^=A+1
        S.add(x[1])
    else:
        delL=[]
        for x in S:
            A=L[x]
            if(A==1):
                delL.append(x)
            XOR^=A
            XOR^=A-1
            L[x]-=1
        for x in delL:
            S.remove(x)
    print(XOR)
