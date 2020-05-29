# Problem: https://atcoder.jp/contests/abc071/tasks/abc071_b
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def solver(inputStr):
    # print("STR={}".format(inputStr))
    # バケツを用意する
    bucket = [0] * 26
    result = "None"
    # print("Bucket:{}".format(bucket))
    for j in range(0, len(inputStr), +1):
        charNo = ord(inputStr[j]) - ord('a')
        bucket[charNo] = bucket[charNo] + 1
    for j in range(0, 26, +1):
        if bucket[j] == 0:
            result = chr(ord('a')+j)
            break
    # algorithm
    return result
if __name__ == "__main__":
    S = sys.stdin.readline().split()
    print("{}".format(solver(S[0])))
