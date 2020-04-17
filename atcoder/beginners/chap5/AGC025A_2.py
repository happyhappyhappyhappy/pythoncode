# Problem: https://atcoder.jp/contests/agc025/tasks/agc025_a
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(inputNo):
    result = 36
    for a in range(1, inputNo, +1):
        strA = str(a)
        strB = str(inputNo-a)
        checkDigitAdd = 0
        for j in range(0, len(strA)):
            checkDigitAdd = checkDigitAdd + int(strA[j])
        for j in range(0, len(strB)):
            checkDigitAdd = checkDigitAdd + int(strB[j])
        if checkDigitAdd < result:
            result = checkDigitAdd
#            print("Then {} {} , changed".format(strA, strB))
    # algorithm
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
