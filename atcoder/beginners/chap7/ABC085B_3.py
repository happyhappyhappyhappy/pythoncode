# Problem: https://atcoder.jp/contests/abc085/tasks/abc085_b
# Python 3rd Try

import sys
from collections import Counter,deque
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def solver(riseSetQue):
    result = 0
    print("RICELEN={}".format(len(riseSetQue)))

    # algorithm
    return result
if __name__ == "__main__":
    N = II()
    riceSet = deque()
    for j in range(0, N, +1):
        riceSet.append(II())
    print("{}".format(solver(riceSet)))
