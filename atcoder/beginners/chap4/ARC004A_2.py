# Problem: https://atcoder.jp/contests/arc004/tasks/arc004_1
# Python 2nd Try

import sys
import math
import pprint
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


def solver(allPoints, pointdata):
    result = 0.000000
    # algorithm
    for j in range(allPoints):
        for k in range(allPoints):
            xdiff = Points[j][0] - Points[k][0]
            ydiff = Points[j][1] - Points[k][1]
            pointdiff = math.sqrt(xdiff**2+ydiff**2)
            if result < pointdiff:
                result = pointdiff
    return result


if __name__ == "__main__":
    N = II()
    Points = [ [0] * 2 for j in range(0, N)]
    for j in range(0, N):
        j1, j2 = MI()
        Points[j][0] = j1
        Points[j][1] = j2
#   pprint.pprint(Points)
    print("{:6f}".format(solver(N, Points)))
