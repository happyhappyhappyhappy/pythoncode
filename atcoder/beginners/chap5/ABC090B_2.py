# Problem: https://atcoder.jp/contests/abc090/tasks/abc090_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(fromNum, toNum):
    result = 0
    # algorithm
    for number in range(fromNum, toNum+1):
        strNum = str(number)
        if strNum[0] == strNum[4]:
            if strNum[1] == strNum[3]:
                result = result + 1
    return result


if __name__ == "__main__":
    A, B = MI()
    print("{}".format(solver(A, B)))
