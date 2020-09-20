# Problem: https://atcoder.jp/contests/arc096/tasks/arc096_a
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


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1
MAXSHEET = 10**5

def solver(a_price, b_price, ab_price, x_sheet , y_sheet):
    result = MAXSHEET*a_price+MAXSHEET*b_price
    for j in range(0, 2*MAXSHEET, 2):
        total = ((x_sheet-j//2)*a_price + (y_sheet-j//2)*b_price +
                                         j*ab_price)
        print("total={}".format(total))
        check = ( total < result )
        if check:
            print("値は{}に".format(total))
            result = total
    return result


if __name__ == "__main__":
    a_price, b_price, ab_price, x_sheet , y_sheet = MI()
    print("{}".format(solver(a_price, b_price,
                             ab_price, x_sheet, y_sheet)))
