# Problem: https://atcoder.jp/contests/arc096/tasks/arc096_a
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


def solver(a_price, b_price, c_price, target_x, target_y):
    result = 10000000
    for mix_i in range(0, 2 * 10^5+1, +1):
        a_i = target_x - mix_i//2
        b_i = target_y - mix_i//2
        totalPrice = max(a_i, 0) * a_price + max(b_i,0) * b_price + mix_i * c_price
        if totalPrice < result:
            # print("A={},B={},C={} -> total = {}".format(a_i, b_i, mix_i, totalPrice))
            result = totalPrice
    return result


if __name__ == "__main__":
    A, B, C, X, Y = MI()
    print("{}".format(solver(A, B, C, X, Y)))
