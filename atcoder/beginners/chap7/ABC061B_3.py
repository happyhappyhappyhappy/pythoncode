# Problem: https://atcoder.jp/contests/abc061/tasks/abc061_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(cityCount, roadCount, fromCity, toCity):
    result = [0]*(cityCount+1)
    roadRange = range(0, roadCount, +1)
    for j in roadRange:
        city = fromCity[j]
        result[city] = result[city] + 1
        city = toCity[j]
        result[city] = result[city] + 1
    # algorithm
    # print("RESULT {}".format(result[1:cityCount+1]))
    return result[1:cityCount+1]


if __name__ == "__main__":
    N, M = MI()
    fromCity = []
    toCity = []
    roadRange = range(0, M, +1)
    for _ in roadRange:
        tmp_i, tmp_j = MI()
        fromCity.append(tmp_i)
        toCity.append(tmp_j)
    solveList = solver(N, M, fromCity, toCity)
    # print("{}".format(solver()))
    for j in range(0, N, +1):
        print(solveList[j])
