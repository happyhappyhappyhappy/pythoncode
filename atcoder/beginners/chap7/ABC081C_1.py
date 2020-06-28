# Problem: atcoder.jp/contests/abc081/tasks/arc086_a
# Python 1st Try

import sys
# from collections import defaultdict
import collections as col
# import pprint
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(ALLNUM, KIND, ball_numbers):
    result = 0
    # prp = pprint.pprint
    counter_result = col.Counter(ball_numbers)
    ball_num_len = len(counter_result)
    counter_result_sorted = sorted(counter_result.items(), key=lambda x: x[1])
    # prp(counter_result_sorted)
    if ball_num_len <= KIND:
        return 0
    reduce_kind = ball_num_len - KIND
    # prp(reduce_kind)
    for _, ballCount in counter_result_sorted:
        result += ballCount
        reduce_kind = reduce_kind - 1
        # prp(reduce_kind)
        if reduce_kind <= 0:
            break
    return result


if __name__ == "__main__":
    N, K = MI()
    Ai = list(map(int, sys.stdin.readline().split()))
    # print(Ai)
    print("{}".format(solver(N, K, Ai)))
