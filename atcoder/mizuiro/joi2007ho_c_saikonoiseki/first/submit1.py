def isExit(p,cSet):
    return p in cSet

def sqcheck(p1,p2,cSet):
    length=0
    (x1,y1) = p1
    (x2,y2) = p2
    p3 = (x2+y1-y2,y2+x2-x1)
    p4 = (x1+y1-y2,y1+x2-x1)
    if isExit(p3,cSet) and isExit(p4,cSet):
        length = pow(x2-x1,2)+pow(y2-y1,2)
    return length

def solver(n,tuples):
    result = 0
    tuples.sort()
    columnSet = set(tuples)
    for j in range(n):
        for k in range(j+1,n):
            result = max(result,sqcheck(tuples[j],tuples[k],columnSet))
    # algorithm
    return result

if __name__ == "__main__":
    Pnt = int(input())
    columnT = [None for j in range(Pnt)] # 箱を作っておく
    for j in range(Pnt):
        columnT[j] = tuple(map(int,input().split()))
    columnT.sort()
    print("{}".format(solver(Pnt,columnT)))