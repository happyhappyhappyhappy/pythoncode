# Problem: https://atcoder.jp/contests/agc025/tasks/agc025_a
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(inputNum):
    result = 0
    # algorithm
    totalDigit = 0
    inputStr = str(inputNum)
    for j in range(0, len(inputStr)):
        totalDigit = totalDigit + int(inputStr[j])
    if totalDigit == 1:
        result = 10
    else:
        result = totalDigit
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
