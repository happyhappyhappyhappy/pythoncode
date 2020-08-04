# Problem: https://atcoder.jp/contests/abc085/tasks/abc085_c
# Python 2nd Try

import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(papers, totalSum):
    result = " ".join(map(str,[ -1 , -1 , -1])) # 10000円札,5000円札,1000円札
    for x in range(0, papers+1 , +1):
        for y in range(papers - x, papers+1 , +1):
            part_hundred_yen = totalSum - x*10000 - y*5000
            print("1000Yen={}".format(part_hundred_yen))
            if_hundred_yen_papers = part_hundred_yen // 1000
            if 0 <=if_hundred_yen_papers and 0 <= (papers - x - y - if_hundred_yen_papers):
                result = " ".join(map(str,[x, y, if_hundred_yen_papers]))
                return result
    return result


if __name__ == "__main__":
    n, y = MI()
    print("{}".format(solver(n, y)))
