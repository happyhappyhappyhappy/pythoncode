# Problem: https://atcoder.jp/contests/abc083/tasks/abc083_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
intm1 = lambda x: int(x) - 1
intp1 = lambda x: int(x) + 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def digitSum(target):
    result = 0
    strTarget = str(target)
    for j in range(0, len(strTarget)):
        result = result + int(strTarget[j])
    return result


def checker(target, fromNumber, toNumber):
    result = False
    x = digitSum(target)
    if fromNumber <= x :
        if  x <= toNumber :
            result = True
    return result


def solver(maxNumber, fromNumber, toNumber):
    result = 0
    for j in range(1, maxNumber + 1):
        if checker(j, fromNumber, toNumber):
#            print("{} is check!".format(j))
            result = result + j
    # algorithm
    return result


if __name__ == "__main__":
    N, A, B = MI()
    print("{}".format(solver(N, A, B)))
