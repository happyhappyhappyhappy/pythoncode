# Problem: https://atcoder.jp/contests/abc051/tasks/abc051_b
# Python 1st Try
# CalcTime O^3 Edition(NG)

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


def solver(K, S):
    result = 0
    # algorithm
    for x in range(0, K+1):
        for y in range(0, K+1):
            for z in range(0, K+1):
                if x+y+z == S:
                    result = result + 1
    return result


if __name__ == "__main__":
    K, S = MI()
#    print("K={} S={}".format(K, S))
    print("{}".format(solver(K, S)))
