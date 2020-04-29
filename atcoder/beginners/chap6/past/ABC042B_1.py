# Problem: https://atcoder.jp/contests/abc042/tasks/abc042_b
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(allNum, longLeng, eachString):
    result = ''
    eachString.sort()
    result = "".join(eachString)
    return result


if __name__ == "__main__":
    N, L = MI()
    SI = []
    for _ in range(0, N, +1):
        getStrList = sys.stdin.readline().split()
        SI.append(getStrList[0])
    print("{}".format(solver(N, L, SI)))
