# Problem: https://atcoder.jp/contests/abc051/tasks/abc051_b
# Python  3rd Try

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


def solver(maxNum, totalNum):
    result = 0
    for x in range(0,maxNum+1):
        for y in range(0,maxNum+1):
            z = totalNum - x - y
            if 0 <= z and z <= maxNum:
                result = result + 1
    return result


if __name__ == "__main__":
    K, S = MI()
    print("{}".format(solver(K, S)))
