def TI(): return tuple(map(int,input().split()))
def II(): return int(input())

N=II()
XY=[TI() for i in range(N)]
print(XY)
XY.sort()
print(XY)