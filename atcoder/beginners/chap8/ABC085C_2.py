# Problem: https://atcoder.jp/contests/abc085/tasks/abc085_c
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(papers, totalSum):
    result = [0, 0, 0] # 10000円札,5000円札,1000円札
    # algorithm
    return result


if __name__ == "__main__":
    n, y = MI()
    print("{}".format(solver(n, y)))
