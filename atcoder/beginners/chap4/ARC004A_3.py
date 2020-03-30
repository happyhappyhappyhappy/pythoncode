# Problem: https://atcoder.jp/contests/arc004/tasks/arc004_1
# Python 3rd Try

import sys
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


def solver():
    result = 0
    # algorithm
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
    print(Point)
#    x2, y2 = Point[1]
# print("{},{}".format(x2,y2))
#    print("{}".format(solver()))
