# Problem: https://atcoder.jp/contests/abc042/tasks/abc042_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(str, sys.stdin.readline().split()))


def LS(): return list(map(str, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(allNumber, eachStringList):
    result = ""
    # algorithm
    eachStringList.sort(reverse=False)
    #    print("{}".format(eachStringList))
    result = result.join(eachStringList)
    return result


if __name__ == "__main__":
    N, _ = MI()
    SI = []
    for j in range(N):
        tmpList = LS()
        SI.append(tmpList[0])
    print("{}".format(solver(N, SI)))
