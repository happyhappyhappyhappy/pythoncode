# Problem: https://atcoder.jp/contests/agc012/tasks/agc012_a
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(eachPoints):
    result = 0
    group = len(eachPoints) // 3
    grouping = [[0] * 3 for _ in range(group)]
    eachPoints.sort(reverse=False)
#    for mi in range(group):
#        tmpgroup = mi // group
#        tmpposition = mi % 3

    print(grouping)
    # algorithm
    return result


if __name__ == "__main__":
    _ = II()
    AI = LI()
    print("{}".format(solver(AI)))
