# Problem: https://atcoder.jp/contests/abc081/tasks/arc086_a
# Python 3rd Try

import sys
from collections import Counter
# import heapq,copy
# import pprint
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(ball_count, limit_num, ball_write_nums):
    result = 0
    total_count = Counter(ball_write_nums)
    count_list = list(total_count.values())
    count_list.sort()
    change_num = len(count_list) - limit_num
    for j in range(0, change_num, +1):
        result += count_list[j]
    return result


if __name__ == "__main__":
    K, N = MI()
    SI = LI()
    print("{}".format(solver(K, N, SI)))
