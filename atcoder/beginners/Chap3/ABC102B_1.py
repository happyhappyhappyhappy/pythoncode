# Problem https://atcoder.jp/contests/abc102/tasks/abc102_b
# Python 1st Try
import sys


def solve(N, givenList):
    answer = 0
    sortedList = sorted(givenList, reverse=True)
    answer = sortedList[0]-sortedList[-1]
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    Ai = list(map(int, sys.stdin.readline().split(' ')))
    print(solve(N, Ai))
