# Problem: https://atcoder.jp/contests/abc047/tasks/abc047_b
# Python 3rd Try

import sys
# import pprint
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(WIDTH, HEIGHT, OPERATION):
    result = 0
    all_ope = len(OPERATION)
    up_max = HEIGHT
    left_min = 0
    right_max = WIDTH
    down_min = 0
    for j in range(0, all_ope, +1):
        each_ope = OPERATION[j]
        ope = each_ope[2]
        if ope == 1:
            if left_min < each_ope[0]:
                left_min = each_ope[0]
        if ope == 2:
            if each_ope[0] < right_max:
                right_max = each_ope[0]
        if ope == 3:
            if down_min < each_ope[1]:
                down_min = each_ope[1]
        if ope == 4:
            if each_ope[1] < up_max:
                up_max = each_ope[1]
    if ((left_min < right_max) and (down_min < up_max)):
        result = (right_max-left_min) * (up_max - down_min)
    return result


if __name__ == "__main__":

    W, H, N = MI()
    OPE = list()
    for _ in range(0, N, +1):
        OPE.append(LI())
    print("{}".format(solver(W, H, OPE)))
