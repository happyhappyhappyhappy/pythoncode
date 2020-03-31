# Problem: https://atcoder.jp/contests/arc004/tasks/arc004_1
# Python 3rd Try

import sys
import math
# from collections import defaultdict
# import heapq,copy
# from collections import deque
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(num, Points):
    result = 0.00000
    # algorithm
    for j in range(num):
        for k in range(num):
            x1, y1 = Points[j]
            x2, y2 = Points[k]
            xdiff = x2 - x1
            ydiff = y2 - y1
            destant = math.sqrt(xdiff**2 + ydiff**2)
            if result < destant:
                result = destant
    return result


if __name__ == "__main__":
    N = II()
    XS=[]
    YS=[]
    for _ in range(N):
        x, y = MI()
        XS.append(x)
        YS.append(y)
    Point = list(zip(XS, YS))
#    print(Point)
#    x2, y2 = Point[1]
# print("{},{}".format(x2,y2))
print("{:6f}".format(solver(N, Point)))
