# Problem: https://atcoder.jp/contests/arc004/tasks/arc004_1
# Python 1st Try

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
# def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(point, xs, ys):
    result = 0.0000000
    # algorithm
    for j in range(0,point):
        for k in range(0,point):
            nowx = xs[j] - xs[k]
            nowy = ys[j] - ys[k]
            nowselect = math.sqrt(nowx*nowx+nowy*nowy)
#             print("{:6}".format(nowselect))
            if result < nowselect:
                result = nowselect
    return result


if __name__ == "__main__":
    N = II()
    X = []
    Y = []
    for j in range(0,N):
        nowx , nowy =  MI()
        X.append(nowx)
        Y.append(nowy)
    print("{:6f}".format(solver(N, X, Y)))
#    pprint.pprint(X)
#    pprint.pprint(Y)
