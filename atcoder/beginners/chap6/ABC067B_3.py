# Problem: https://atcoder.jp/contests/abc067/tasks/abc067_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(allNumber, selectNum, eachLength):
    result = 0
    # algorithm
    sortedStickLength = sorted(eachLength, reverse=True)
    #    print("{}:{}".format(sortedStickLength, eachLength))
    for j in range(0, selectNum, +1):
        result = result + sortedStickLength[j]
    return result


if __name__ == "__main__":
    N, K = MI()
    StickList = LI()
    print("{}".format(solver(N, K, StickList)))
