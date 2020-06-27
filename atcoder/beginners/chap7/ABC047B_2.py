# Problem: https://atcoder.jp/contests/abc047/tasks/abc047_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(Width, Height, op_count, x_list, y_list, op_list):
    result = 0
    x_label_max = Width
    x_label_min = 0
    y_label_max = Height
    y_label_min = 0
    for j in range(0, op_count):
        real_ope = op_list[j]
        if real_ope == 1:
            x_label_min = max(x_list[j], x_label_min)
        if real_ope == 2:
            x_label_max = min(x_list[j], x_label_max)
        if real_ope == 3:
            y_label_min = max(y_list[j], y_label_min)
        if real_ope == 4:
            y_label_max = min(y_list[j], y_label_max)
    resultWidth = x_label_max - x_label_min
    resultHeight = y_label_max - y_label_min
    if resultWidth < 0:
        resultWidth = 0
    if resultHeight < 0:
        resultHeight = 0
    result = resultWidth * resultHeight
    return result


if __name__ == "__main__":
    W, H, N = MI()
    x_list = list()
    y_list = list()
    op_list = list()
    for _ in range(0, N, +1):
        tmp_x, tmp_y, tmp_op = MI()
        x_list.append(tmp_x)
        y_list.append(tmp_y)
        op_list.append(tmp_op)
    print("{}".format(solver(W, H, N, x_list, y_list, op_list)))
