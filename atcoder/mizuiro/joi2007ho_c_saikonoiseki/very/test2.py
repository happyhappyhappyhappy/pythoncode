N = int(input())
XY=[]
for j in range(N):
    X = list(int(x) for x in input().split())
    XY.append(X)
print(XY)
XY.sort()
print(XY)
