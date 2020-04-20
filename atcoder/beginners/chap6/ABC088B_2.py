# Problem: https://atcoder.jp/contests/abc088/tasks/abc088_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(allCards, eachCards):
    eachCardSort = sorted(eachCards, reverse=True)
    AlicesTotal = 0
    BobsTotal = 0
    for j in range(0, allCards, +1):
        if j % 2 == 0:
            AlicesTotal = AlicesTotal + eachCardSort[j]
        else:
            BobsTotal = BobsTotal + eachCardSort[j]
    # algorithm
    return AlicesTotal - BobsTotal


if __name__ == "__main__":
    N = II()
    AN = LI()
    print("{}".format(solver(N, AN)))
