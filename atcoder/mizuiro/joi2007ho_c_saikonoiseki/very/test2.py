N = int(input())
XY=[]
for j in range(N):
    X = list(int(x) for x in input().split())
    XY.append(X)
print(XY)
XY.sort()
print(XY)
[x1,y1]=XY[3]
print(x1)
print(y1)