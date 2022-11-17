import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1


def solver(Lucky):
    result = 0
    # algorithm
    print("LuckyNumber is {}".format(Lucky))
    return result


if __name__ == "__main__":
    II()
    L = sys.stdin.readline()
    print("{}".format(solver(L)))
