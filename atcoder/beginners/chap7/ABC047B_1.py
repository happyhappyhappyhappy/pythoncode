# Problem: https://atcoder.jp/contests/abc047/tasks/abc047_b
# Python 1st Try

import sys
import pprint
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(Width, Height, Point, x_position, y_position, control_id):
    result = 0
    surface = [[0] * (Width+1) for _ in range(0, Height+1, +1)]
    # algorithm
    # pprint.pprint(surface)
    for j in range(0, Point, +1):
        if control_id[j] == 1:
            for x in range(0, Width+1):
                for y in range(0, Height+1):
                    if x <= x_position[j]:
                        #  print("x={},y={} Point".format(x, y))
                        surface[y][x] = 1
        elif control_id[j] == 2:
            for x in range(0, Width+1):
                for y in range(0, Height+1):
                    if x_position[j] <= x:
                        surface[y][x] = 1
        elif control_id[j] == 3:
            for x in range(0, Width+1):
                for y in range(0, Height+1):
                    if y <= y_position[j]:
                        surface[y][x] = 1
        else:  # control_id[X] == 4
            for x in range(0, Width+1):
                for y in range(0, Height+1):
                    if y_position[j] <= y:
                        surface[y][x] = 1
    pprint.pprint(surface)
    return result


if __name__ == "__main__":
    W, H, N = MI()
    x_position = list()
    y_position = list()
    control_id = list()
    for j in range(0, N, +1):
        x_tmp, y_tmp, a_tmp = MI()
        x_position.append(x_tmp)
        y_position.append(y_tmp)
        control_id.append(a_tmp)
    print("{}".format(solver(W, H, N, x_position, y_position, control_id)))
