# Problem:
# Python  Try

import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

# COOD : 座標 出力しないこと
COOD=[[False for j in range(5000)] for k in range(5000)]

def solver():
    result = 0
    # algorithm
    return result


if __name__ == "__main__":

    PointCnt = II()
    Point = LLI(PointCnt)
    print(Point)
    [x,y] = Point[1]
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("{}".format(solver()))
