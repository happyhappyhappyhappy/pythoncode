# Problem: https://atcoder.jp/contests/abc091/tasks/abc091_b
# Python 3rd Try

import sys
from collections import defaultdict
# import pprint
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(blue_count, blue_list, red_count, red_list):
    result = 0
    allDict = defaultdict(int)
    for j in range(0, blue_count, +1):
        allDict[blue_list[j]] += 1
    for j in range(0, red_count, +1):
        allDict[red_list[j]] -= 1
    # algorithm
    # print("{}".format(allDict))
    dictList = list(allDict.values()) + [0]
    dictList.sort(reverse=True)
    # pprint.pprint("{}".format(dictList))
    result = dictList[0]
    return result


if __name__ == "__main__":
    N = II()
    si = []
    for _ in range(0, N, +1):
        si.append(input())
    M = II()
    ti = []
    for _ in range(0, M, 1):
        ti.append(input())
    print("{}".format(solver(N, si, M, ti)))
