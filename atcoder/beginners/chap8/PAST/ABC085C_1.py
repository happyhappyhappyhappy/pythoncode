# Problem: https://atcoder.jp/contests/abc085/tasks/abc085_c
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(givenPieces, total_sum):
    #   result = 0
    # algorithm
    for x in range(0, givenPieces+1, +1):
        for y in range(0, givenPieces+1-x, +1):
            remained_money = total_sum - (x * 10000 + y * 5000)
#            remained_pieces = givenPieces - x - y
#            if remained_pieces < 0:
            z = givenPieces - (x + y)
            total = x * 10000 + y * 5000 + z * 1000
            if total_sum == total:
                return [x, y, (remained_money // 1000)]
    return [-1, -1, -1]


if __name__ == "__main__":
    N, Y = MI()
    result = solver(N, Y)
    print("{} {} {}".format(result[0], result[1], result[2]))
