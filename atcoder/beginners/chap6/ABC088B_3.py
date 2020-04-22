# Problem: https://atcoder.jp/contests/abc088/tasks/abc088_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(cardNumberList):
    result = 0
    cardNumberList.sort(reverse=True)

    # algorithm
    # Alices'Turn
    for j in range(0, len(cardNumberList), +2):
        result = result + cardNumberList[j]
    # Bobs'Turn
    for j in range(1, len(cardNumberList), +2):
        result = result - cardNumberList[j]
    return result


if __name__ == "__main__":
    _ = II()
    AI = LI()
    print("{}".format(solver(AI)))
