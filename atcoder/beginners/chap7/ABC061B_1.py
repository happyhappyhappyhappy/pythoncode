# Problem: https://atcoder.jp/contests/abc061/tasks/abc061_b
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def solver(cityNumber, roadNumber):
    result = [0] * cityNumber
    fromList = []
    toList = []
    for _ in range(0, roadNumber, +1):
        tmp_f, tmp_t = MI()
        fromList.append(tmp_f -1)
        toList.append(tmp_t - 1)
    # print("from_LIST:{}".format(fromList))
    # print("to_LIST{}".format(toList))
    city_Count_List = [0] * cityNumber
    for j in range(0,roadNumber,+1):
        city_Count_List[fromList[j]] = city_Count_List[fromList[j]] + 1
        city_Count_List[toList[j]] = city_Count_List[toList[j]] + 1
    result = city_Count_List
    return result
if __name__ == "__main__":
    N, M = MI()
    answerList = solver(N, M)
    for j in range(0, N, +1):
        print("{}".format(answerList[j]))
