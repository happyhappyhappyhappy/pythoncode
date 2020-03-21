# Problem: https://atcoder.jp/contests/abc087/tasks/abc087_b
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
int1 = lambda x: int(x) - 1
intp1 = lambda x: int(x) + 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(yen500, yen100, yen050, objectSum):
    result = "Yes"
    # algorithm
    for j in range(0, intp1(yen500), +1):
        for k in range(0, intp1(yen100), +1):
            pass
        pass
    return result


if __name__ == "__main__":
    A = II()
    B = II()
    C = II()
    X = II()
    print("".format(solver(A, B, C, X)))
