# Problem: https://atcoder.jp/contests/abc042/tasks/abc042_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(allNumber, eachStrings):
    result = ''
    # algorithm
    eachStrings.sort()
    result = "".join(eachStrings)
    return result


if __name__ == "__main__":
    N, L = MI()
    SI = []
    for j in range(0, N):
        tmpStrList = list(map(str, sys.stdin.readline().split()))
        SI.append(tmpStrList[0])
    print("{}".format(solver(N, SI)))
