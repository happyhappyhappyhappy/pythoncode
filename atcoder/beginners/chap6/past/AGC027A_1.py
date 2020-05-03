# Problem: https://atcoder.jp/contests/agc027/tasks/agc027_a
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(allChild, haveCandy, eachHappy):
    result = 0
    allHappyCount = 0
    eachHappy.sort()
    for j in range(len(eachHappy)):
        allHappyCount = allHappyCount + eachHappy[j]
    # algorithm
    # print("{}".format(allHappyCount))
    # if allHappyCount < haveCandy:
    #    result = allChild - 1
    #     return result
    for j in range(0, allChild, +1):
        haveCandy = haveCandy - eachHappy[j]
        if haveCandy < 0:
            return result
        else:
            result = result + 1
    if 0 < haveCandy:
        result = result - 1
    return result


if __name__ == "__main__":
    N, X = MI()
    childHappyCount = LI()
    print("{}".format(solver(N, X, childHappyCount)))
