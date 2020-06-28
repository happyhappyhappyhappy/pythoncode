# Problem: atcoder.jp/contests/abc081/tasks/arc086_a
# Python 1st Try

import sys
# from collections import defaultdict
from collections import Counter as counter
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(ALLNUM, KIND, ball_numbers):
    result = 0
    counter_result = counter(ball_numbers)
    print("{}".format(counter_result))
    # algorithm
    return result


if __name__ == "__main__":
    N, K = MI()
    Ai = list(map(int, sys.stdin.readline().split()))
    print(Ai)
    print("{}".format(solver(N, K, Ai)))
