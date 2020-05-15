# Problem: https://atcoder.jp/contests/agc012/tasks/agc012_a
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def solver(groups, eachScore):
    result = 0
    # print("Group : {}".format(groups))
    # print("Score : {}".format(eachScore))
    sortEachScore= sorted(eachScore)
    # print("Sort : {}".format(sortEachScore))
    for userNo in range(groups, groups*3, +2):
        result = result + sortEachScore[userNo]
    return result
if __name__ == "__main__":
    N = II()
    AI = LI()
    print("{}".format(solver(N, AI)))
