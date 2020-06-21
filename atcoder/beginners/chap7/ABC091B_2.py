# Problem: https://atcoder.jp/contests/abc091/tasks/abc091_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(blueCard, redCard):
    result = 0
    # algorithm
    return result


if __name__ == "__main__":
    N = II()
    blueCard = list()
    for _ in range(0, N, +1):
        strings = sys.stdin.readline().strip('\n')
        blueCard.append(strings)
    M = II()
    redCard = list()
    for _ in range(0, M, +1):
        strings = sys.stdin.readline().strip('\n')
        redCard.append(strings)
    print("Blue:{}".format(blueCard))
    print("Red {}".format(redCard))
    print("{}".format(solver(blueCard, redCard)))
