# Problem: https://atcoder.jp/contests/abc080/tasks/abc080_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


yes = "Yes"
no = "No"


def solver(inputNum):
    result = no
    # algorithm
    inputNumStr = str(inputNum)
    fx = 0
    for j in range(0, len(inputNumStr)):
        fx = fx + int(inputNumStr[j])
    if inputNum % fx == 0:
        result = yes
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
