base=["abc","de","fghi"]
M=0
N=len(base)
for j in range(N):
    Slen=len(base[j])
    M=max(M,Slen)
print(f"M={M}")
T=[["*"] * N for _ in range(M)]
T2=[["*"] * N for _ in range(M)]
print(f"T={T}")
for j in range(N):
    baseLen=len(base[j])
    for k in range(baseLen):
        print(f"B[j={j}][k={k}]->T2[k={k}][j={j}]")
        print(f"baseの{j}番目 {k}個目の{base[j][k]}を結果のT2[{k}][{j}]に入れる")
        T2[k][j]=base[j][k]
        print(f"B[j={j}][k={k}]->T[k={k}][N({N})-1-j({j})={N-1-j}]")
        print(f"baseの{j}番目 {k}個目の{base[j][k]}を結果のT[{k}][{N-1-j}]に入れる")
        T[k][N-j-1]=base[j][k]
result=[]
result3=[]
for j in range(M):
    S="".join(T[j])
    result.append(S)
for j in range(M):
    S="".join(T2[j])
    result3.append(S)
print(f"result1:{result}")
ansstr="\n".join(result)
print(f"result2\n{ansstr}")
ans2str="\n".join(result3)
print(f"B_result\n{ans2str}")
