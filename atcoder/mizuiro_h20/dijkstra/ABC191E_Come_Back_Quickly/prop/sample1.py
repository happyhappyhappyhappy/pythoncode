D=[[float('inf')] *3 for j in range(0,2) ]
D[0][1]=3
D[1][2]=2

D1=D[0]

for x in D1:
    print(x)
print(min(D[1]))
