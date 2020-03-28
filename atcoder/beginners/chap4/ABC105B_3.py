# Problem: https://atcoder.jp/contests/abc105/tasks/abc105_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(givenMoney):
    result = "No"
    for j in range(0,101):
        for k in range(0,101):
            nowtotal = j * 4 + k * 7
            if nowtotal == givenMoney:
                result = "Yes"
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
