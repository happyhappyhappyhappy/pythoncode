# Problem: https://atcoder.jp/contests/abc080/tasks/abc080_b
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(inputNum):
    result = "No"
    # algorithm
    strNum = str(inputNum)
    divisorNum = 0
    for j in range(0, len(strNum), +1):
        divisorNum = divisorNum + int(strNum[j])
    if inputNum % divisorNum == 0:
        result = "Yes"
    return result


if __name__ == "__main__":
    print("{}".format(solver(II())))
