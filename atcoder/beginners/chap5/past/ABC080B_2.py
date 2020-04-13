# Problem: https://atcoder.jp/contests/abc080/tasks/abc080_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())
#   def MI1(): return map(int1, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


yes = "Yes"


no = "No"


def solver(checkNum):
    result = no
    checkNumStr = str(checkNum)
    harshedNum = 0
    for j in range(0, len(checkNumStr)):
        harshedNum = harshedNum + int(checkNumStr[j])
    if checkNum % harshedNum == 0:
        result = yes
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
