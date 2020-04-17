# Problem: https://atcoder.jp/contests/agc025/tasks/agc025_a
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def digitSum(inputNum):
    result = 0
    inputNumStr = str(inputNum)
    for j in range(0, len(inputNumStr)):
        result = result + int(inputNumStr[j])
    return result


def solver(inputNum):
    result = 10**5
    # algorithm
    for j in range(1, inputNum):
        total = digitSum(j)+digitSum(inputNum-j)
        if total <= result:
            result = total
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
