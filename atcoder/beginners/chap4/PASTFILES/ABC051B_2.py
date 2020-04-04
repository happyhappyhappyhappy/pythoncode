# Problem:
# Python  Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
intm1 = lambda x: int(x) - 1
intp1 = lambda x: int(x) + 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(intm1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(limitno, giventotal):
    result = 0
    for x in range(0, limitno+1):
        for y in range(0, limitno+1):
            z = giventotal - x - y
            if ( 0 <= z ) and (z <= limitno):
#                print("{} + {} + {} = {}".format(x,y,z,giventotal))
                result = intp1(result)
    return result


if __name__ == "__main__":
    K, S = MI()
    print("{}".format(solver(K, S)))
