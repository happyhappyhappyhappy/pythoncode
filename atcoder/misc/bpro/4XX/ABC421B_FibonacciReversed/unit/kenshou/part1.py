A=[0]*10
A[0]=90701
A[1]=90204
for j in range(2,10):
    tmpA=A[j-2]+A[j-1]
    tmpAstr=str(tmpA)
    tmpAstr2=tmpAstr[::-1]
    A[j]=int(tmpAstr2)
    print(f"A[{j}]={A[j]}")
print(A[-1])
