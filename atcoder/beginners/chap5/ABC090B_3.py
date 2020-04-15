# Problem: https://atcoder.jp/contests/abc090/tasks/abc090_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def checkParin(checkNum):
    result = False
    checkNumStr = str(checkNum)
    checkNumStrBase = checkNumStr[::-1]
    charEq = 0
    for j in range(0, len(checkNumStrBase)):
        if checkNumStr[j] == checkNumStrBase[j]:
            charEq = charEq + 1
    if charEq == len(checkNumStr):
        result = True
    return result


def solver(fromNum, toNum):
    result = 0
    # algorithm
    j = fromNum
    while ((j <= fromNum) and (j <= toNum)):
        if checkParin(j):
            result = result + 1
        j = j + 1
    return result


if __name__ == "__main__":
    print("{}".format(solver()))
