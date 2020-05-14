# Problem:https://atcoder.jp/contests/agc012/tasks/agc012_a
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(groupNumber, scoreList):
    allMenbar = 3 * groupNumber
    scoreList.sort()
#    print(scoreList)
    secondPositioner = scoreList[groupNumber:allMenbar:+2]
#    print(secondPositioner)
    result = sum(secondPositioner)
    # algorithm
    return result


if __name__ == "__main__":
    N = II()
    AI = LI()
    print("{}".format(solver(N, AI)))
