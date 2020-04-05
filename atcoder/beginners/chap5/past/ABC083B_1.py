# Problem: https://atcoder.jp/contests/abc083/tasks/abc083_b
# Python  1st Try

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

def int2ketanowa(No):
    result = 0
    noStr = str(No)
    nolen = len(noStr)
    for j in range(0,nolen):
        result = result + int(noStr[j])
    return result

def solver(maxNum, upperNum, lowerNum):
    result = 0
    for j in range(1,maxNum+1,+1):
        sumKeta = int2ketanowa(j)
        if upperNum <= sumKeta and sumKeta <= lowerNum:
            result = result + j
    return result


if __name__ == "__main__":
    N, A, B = MI()
    print("{}".format(solver(N, A, B)))
