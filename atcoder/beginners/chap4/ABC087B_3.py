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
    result = 0
    # algorithm
    for yen500v in range(0, intp1(yen500)):
        for yen100v in range(0, intp1(yen100)):
            for yen050v in range(0, intp1(yen050)):
                nowtotal = yen500v*500+yen100v*100+yen050v*50
                if nowtotal == objectSum:
                    result = intp1(result)
    return result


if __name__ == "__main__":
    A = II()
    B = II()
    C = II()
    X = II()
    print("{}".format(solver(A, B, C, X)))
