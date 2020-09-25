# Problem: https://atcoder.jp/contests/arc096/tasks/arc096_a
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1


def solver(a_price, b_price, half_price, need_a, need_b):
    result = MAXSIZE
    for half_get in range(0, 2*(10**5)+1, +2):
        pass
    # algorithm
    return result


if __name__ == "__main__":
    A, B, C, X, Y = MI()
    print("{}".format(solver(A, B, C, X, Y)))
