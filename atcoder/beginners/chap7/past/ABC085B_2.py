# Problem: https://atcoder.jp/contests/abc085/tasks/abc085_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def solver(riceCakesList):
    result = 0
    # print("LIST={}".format(riceCakesList))
    # algorithm
    result = len(set(riceCakesList))
    return result
if __name__ == "__main__":
    N = II()
    DI = list()
    for _ in range(N):
        DI.append(II())
    print("{}".format(solver(DI)))
