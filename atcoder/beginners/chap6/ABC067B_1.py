# Problem: https://atcoder.jp/contests/abc067/tasks/abc067_b
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(selectNum, barLongth):
    result = 0
    barLongth.sort(reverse=True)
    #   print("{}".format(barLongth))
    # algorithm
    j = 0
    while j < selectNum:
        result = result + barLongth[j]
        j = j + 1
    return result


if __name__ == "__main__":
    _, K = MI()  # Nは要らない
    LII = LI()
    print("{}".format(solver(K, LII)))
