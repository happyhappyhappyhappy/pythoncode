# Problem: https://atcoder.jp/contests/agc027/tasks/agc027_a
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(haveManyPiaceOFCandy, AI):
    result = 0
    AI.sort()
    for j in range(len(AI)):
        haveManyPiaceOFCandy = haveManyPiaceOFCandy - AI[j]
        if haveManyPiaceOFCandy < 0:
            return result
        else:
            result = result + 1
    # algorithm
    if 0 < haveManyPiaceOFCandy:
        result = result - 1
    return result


if __name__ == "__main__":
    _, X = MI()
    AI = LI()
    print("{}".format(solver(X, AI)))
