# Problem: https://atcoder.jp/contests/abc081/tasks/arc086_a
# Python 2nd Try

import sys
from collections import Counter
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(givenBall, selectKind, ball_num):
    result = 0
    summary_Ball = Counter(ball_num)
    # print("{}".format(list(summary_Ball.values())))
    sortedCount = sorted(list(summary_Ball.values()))
    # print(sortedCount)
    ballAllKind = len(sortedCount)
    changeNumberKind = ballAllKind - selectKind
    if changeNumberKind <= 0:
        result = 0
    else:
        for j in range(0, changeNumberKind, +1):
            result += sortedCount[j]
    return result


if __name__ == "__main__":
    N, K = MI()
    Ai = LI()
    print("{}".format(solver(N, K, Ai)))
