# Problem:
# Python  Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def initSet():
    result = set()
    for j in range(ord('a'),ord('z')+1):
        result.add(chr(j))
    return result

def solver(inputString,allCharSet):
    result = ''
    inputSet = set(inputString)
    # print("INPUT={}".format(inputSet))
    # print("ALL={}".format(allCharSet))
    diffset = allCharSet - inputSet
    # print("DIFF={}".format(diffset))
    difflist = list(diffset)
    difflist.sort()
    # print("{}".format(difflist))
    if len(difflist) == 0:
        result = "None"
    else:
        result = difflist[0]
    return result

if __name__ == "__main__":
    S = sys.stdin.readline().split('\n')
    allset = initSet()
    print("{}".format(solver(S[0],allset)))
