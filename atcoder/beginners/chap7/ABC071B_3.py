# Problem:
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(inputString):
    full_set = set()
    input_set = set()
    for j in range(ord('a'), ord('z')+1, +1):
        full_set.add(chr(j))
    for j in range(0, len(inputString), +1):
        input_set.add(inputString[j])
    print("FULLSET:{}".format(full_set))
    print("INPUT:{}".format(input_set))
    # set -= other
    result = 0
    # algorithm
    return result


if __name__ == "__main__":
    S = sys.stdin.readline().split()
    print("{}".format(solver(S[0])))
