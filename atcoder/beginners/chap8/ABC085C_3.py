# Problem: https://atcoder.jp/contests/abc085/tasks/abc085_c
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
YES = "YES"
NO = "NO"

def solver(totalSheet, sum):
    result = [-1, -1, -1]
    # algorithm
    for sheet_10000 in range(0, totalSheet+1, +1):
        for sheet_5000 in range(0, totalSheet + 1 - sheet_10000, +1):
            sheet_1000 = totalSheet - sheet_10000 - sheet_5000
            nowSum = sheet_10000 * 10000 + sheet_5000 * 5000 + sheet_1000 * 1000
            if nowSum == sum:
                result = [sheet_10000 ,sheet_5000, sheet_1000]
    return result


if __name__ == "__main__":
    N, Y = MI()
    answer = solver(N, Y)
    print("{} {} {}".format(answer[0], answer[1], answer[2]))
