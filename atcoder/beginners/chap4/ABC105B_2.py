# Problem: https://atcoder.jp/contests/abc105/tasks/abc105_b
# Python 2nd Try

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


def solver(TOTALSUM):
    result = "No"
    totalsum4max = TOTALSUM // 4 + 1
    totalsum7max = TOTALSUM // 7 + 1
    for j in range(0,totalsum4max):
        for k in range(0,totalsum7max):
            nowtotal = j * 4 + k * 7
            if nowtotal == TOTALSUM :
                result = "Yes"
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
