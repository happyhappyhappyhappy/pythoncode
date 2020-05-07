# Problem: https://atcoder.jp/contests/agc027/tasks/agc027_a
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(childs, candies, happyNumber):
    result = 0
    happyNumber.sort()
    for ch_i in range(0, childs, +1):
        tmpCaI = candies - happyNumber[ch_i]
        if 0 <= tmpCaI:  # まだまだお菓子には余裕があります
            result = result + 1
            candies = tmpCaI
        else:  # これ以上菓子が配れない
            break
    # 全部終わってキッカリで無ければ最後の一人が不満
    if 0 < candies:
        result = result - 1
    return result


if __name__ == "__main__":
    N, x = MI()
    AI = LI()
    print("{}".format(solver(N, x, AI)))
