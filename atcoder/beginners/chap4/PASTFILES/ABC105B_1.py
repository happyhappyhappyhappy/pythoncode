# Problem:
# Python  Try

import sys
# from collections import defaultdict
# import heapq
# import copy
# from collections import deque
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(totalsum):
    result = "No"
    for j in range(0, 100//4+1, +1):
        for k in range(0, 100//7+1, +1):
            thiscase = j * 4 + k * 7
            if thiscase == totalsum:
                result = "Yes"
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
