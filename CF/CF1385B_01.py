# Problem: https://codeforces.com/problemset/problem/1385/B
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(number, allList):
    result = ""
    resultList = []
    # algorithm
    # set_list = set(allList)
    # print(set_list)
    # test_ans = list(set(allList))
    # print(test_ans)
    box = [0] * ( number + 1 )
    # print(box)
    # box[1] = 1
    # print(box)
    for j in range(0,len(allList)):
        num = allList[j]
        if box[num] == 0:
            # print("box[{}] = {}".format(num, box[num]))
            resultList.append(str(num))
            box[num] = 1
    # print(resultList)
    result = " ".join(resultList)
    return result


if __name__ == "__main__":
    t = II()
    for _ in range(t):
        n = II()
        an = LI()
        print("{}".format(solver(n, an)))
