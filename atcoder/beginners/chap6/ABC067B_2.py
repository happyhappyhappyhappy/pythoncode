# Problem:
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(selectNum, snakeLongList):
    result = 0
    sortedSnakeLongList = sorted(snakeLongList, reverse=True)
    for j in range(0, selectNum, +1):
        result = result + sortedSnakeLongList[j]
    # algorithm
    return result


if __name__ == "__main__":
    _, K = MI()
    LongI = LI()
    print("{}".format(solver(K, LongI)))
