# Problem: https://atcoder.jp/contests/abc083/tasks/abc083_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


# int1 = lambda x: int(x) - 1
# p2D = lambda x: print(*x, sep="\n")


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


# def MI1(): return map(int1, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def sumDigit(inputNum):
    result = 0
    numString = str(inputNum)
    for j in range(0, len(numString), +1):
        result = result + int(numString[j])
    return result


def solver(maxNumber, fromNum, toNum):
    result = 0
    for j in range(1, maxNumber+1, +1):
        nowDigitSum = sumDigit(j)
        if fromNum <= nowDigitSum:
            if nowDigitSum <= toNum:
    #                 print("{} is OK!".format(j))
                result = result + j
    return result


if __name__ == "__main__":
    N, A, B, = MI()
    print("{}".format(solver(N, A, B)))
