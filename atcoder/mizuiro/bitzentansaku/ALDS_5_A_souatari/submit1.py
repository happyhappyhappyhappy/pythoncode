import sys
# from collections import defaultdict
# import heapq,copy
input2 = sys.stdin.readline
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1


def solver(gList,sList):
    gLen = len(gList)
    sLen = len(sList)
    print("与えられた数")
    for x in range(gLen):
        print("{} -> {}".format(x,gList[x]))
    print("作る数")
    for x in range(sLen):
        print("{} -> {}".format(x,sList[x]))
    result = 0
    # algorithm

    return result


if __name__ == "__main__":
    givenNum = II()
    noList = [ int(x) for x in (input2().split())]
    solveNum = II()
    solveList = [ int(x) for x in (input2().split())]
    # for j in range(givenNum):
    #    print("{} -> {}".format(j,noList[j]))
    print("{}".format(solver(noList,solveList)))
