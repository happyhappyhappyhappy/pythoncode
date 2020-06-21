# Problem: https://atcoder.jp/contests/abc091/tasks/abc091_b
# Python 1st Try

import sys
from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(plusCardNum, plusCards, minusCardNum, minusCards):
    result = 0
    selectString = defaultdict(int)
    for j in range(plusCardNum):
        selectString[plusCards[j]] = selectString[plusCards[j]] + 1
    for j in range(minusCardNum):
        selectString[minusCards[j]] = selectString[minusCards[j]] - 1
    keyList = list(selectString.keys())
    for j in range(0, len(keyList)):
        if result < selectString.get(keyList[j]):
            result = selectString.get(keyList[j])
    return result


if __name__ == "__main__":
    N = II()
    NList = []
    for _ in range(0, N, +1):
        NList.append(input())
    M = II()
    MList = []
    for _ in range(0, M, +1):
        MList.append(input())
    print("{}".format(solver(N, NList, M, MList)))
