# Problem: https://atcoder.jp/contests/abc088/tasks/abc088_c
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


YES = "Yes"
NO  = "No"


def solver(grid):
    result = NO
    # algorithm
    a0 = 0
    b0 = grid[0][0]
    b1 = grid[0][1]
    b2 = grid[0][2]
    a1 = grid[1][0] - b0
    a2 = grid[2][0] - b0
    if a1+b1 == grid[1][1] and a1+b2 == grid[1][2] \
        and a2 + b1 == grid[2][1] and a2+b2 == grid[2][2]:
        result = YES
    return result


if __name__ == "__main__":
    grid_c = [ [0] * 3 for j in range(0, 3)]
    # pp.pprint(grid_c)
    for j in range(0, 3):
        grid_c[j][0], grid_c[j][1], grid_c[j][2] = MI()
    # pp.pprint(grid_c)
    print("{}".format(solver(grid_c)))
