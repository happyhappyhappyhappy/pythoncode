import sys
from collections import Counter
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def TI(): return tuple(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1


def solver(figI,figL,realI,realL):
    result = 0
    diffList = []
    for j in range(figI):
        for k in range(realI):
            (figx,figy) = figL[j]
            (realx,realy) = realL[k]
            diffx = realx-figx
            diffy = realy-figy
            tuplediff = (diffx,diffy)
            diffList.append(tuplediff)
    diffCounter = Counter(diffList)
    for x,y in diffCounter.items():
        if y == figI:
            result = x
            break
    return result


if __name__ == "__main__":
    figureInt = II()
    figureList = []
    for j in range(figureInt):
        tuple1 = TI()
        figureList.append(tuple1)
    realInt = II()
    realList = []
    for j in range(realInt):
        tuple1 = TI()
        realList.append(tuple1)
    (x,y)=solver(figureInt,figureList,realInt,realList)
    print("{} {}".format(x,y))
