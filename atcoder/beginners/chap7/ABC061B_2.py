# Problem: https://atcoder.jp/contests/abc061/tasks/abc061_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(CITY_NUM, CITY_LIST):
    # result = ""
    resultList = [0] * CITY_NUM
    for j in range(0, len(CITY_LIST), +1):
        now_city = CITY_LIST[j]
        resultList[now_city-1] = resultList[now_city-1]+1
    # for j in range(0, CITY_NUM, +1):
        # print("CITY:{} ROAD:{}".format(j, resultList[j]))
    resultListStr = [str(j) for j in resultList]
    return '\n'.join(resultListStr)
    # print("{}".format(strReturn))
    # return result


if __name__ == "__main__":
    N, M = MI()
    ROAD_ENUMERATION_LIST = []
    for j in range(0, M, +1):
        from_tmp, to_tmp = MI()
        ROAD_ENUMERATION_LIST.append(from_tmp)
        ROAD_ENUMERATION_LIST.append(to_tmp)
    print("{}".format(solver(N, ROAD_ENUMERATION_LIST)))
