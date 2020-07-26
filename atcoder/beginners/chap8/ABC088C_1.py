# Problem: https://atcoder.jp/contests/abc088/tasks/abc088_c
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
yes = "Yes"
no = "No"


def solver(c_grid):
    result = no
    a_list=[0, c_grid[1][0] - c_grid[0][0], c_grid[2][0] - c_grid[0][0]]
    b_list=[c_grid[0][0], c_grid[0][1], c_grid[0][2]]
    if (c_grid[1][1] == a_list[1] + b_list[1]) and \
        (c_grid[1][2] == a_list[1] + b_list[2]) and \
            ( c_grid[2][1] == a_list[2] + b_list[1]) and \
                ( c_grid[2][2] == a_list[2] + b_list[2]):
                    result = yes
    return result


if __name__ == "__main__":
    c_grid = list()
    for _ in range(3):
        c_grid.append(LI())
    # print("{}".format(c_grid))
    print("{}".format(solver(c_grid)))
