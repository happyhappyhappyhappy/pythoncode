# Problem: https://atcoder.jp/contests/abc088/tasks/abc088_b
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(cardCount, cardNumberList):
    result = 0
    cardNumberList.sort(reverse=True)
    #   print("整列済み {}".format(cardNumberList))
    # Aliceのターン
    AlicesCard = 0
    for j in range(0, cardCount, +2):
        #        print("Alice got {}".format(cardNumberList[j]))
        AlicesCard = AlicesCard + cardNumberList[j]
    BobsCard = 0
    for j in range(1, cardCount, +2):
        #           print("Bob got {}".format(cardNumberList[j]))
        BobsCard = BobsCard + cardNumberList[j]
    result = abs(AlicesCard-BobsCard)
    return result


if __name__ == "__main__":
    N = II()
    AI = LI()
    print("{}".format(solver(N, AI)))
