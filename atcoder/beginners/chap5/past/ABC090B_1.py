# Problem:
# Python  Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def palindromic(Num):
    result = False
    strNum = str(Num)
    strRevNum = strNum[::-1]
    checkDigit = 0
    for j in range(0, len(strNum)):
        if strNum[j] == strRevNum[j]:
            checkDigit = checkDigit + 1
    if checkDigit == len(strNum):
        result = True
    return result


def solver(fromNum, ToNum):

    result = 0
    for j in range(fromNum, ToNum+1, +1):
        if palindromic(j):
            result = result + 1
    return result


if __name__ == "__main__":
    A, B = MI()
    print("{}".format(solver(A, B)))
