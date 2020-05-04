# Problem: https://codeforces.com/problemset/problem/1342/A
# Python 1st  Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(firstA, firstB, oneChangeCost, twoChangeCost):
    if firstA < firstB:
        tmp = firstB
        firstB = firstA
        firstA = tmp
    allOne = (firstA+firstB) * oneChangeCost
    diffAandB = firstA - firstB
    partCost = firstB * twoChangeCost + diffAandB * oneChangeCost
    if allOne < partCost:
        return allOne
    else:
        return partCost


if __name__ == "__main__":
    T = II()
    for _ in range(T):
        A, B = MI()
        X, Y = MI()
        print("{}".format(solver(A, B, X, Y)))
