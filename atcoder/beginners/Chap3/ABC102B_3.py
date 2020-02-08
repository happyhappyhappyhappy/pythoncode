# Problem https://atcoder.jp/contests/abc102/tasks/abc102_b
# Python 3rd Try
import sys


def solve(cells):
    answer = 0
    cells.sort(reverse=True)
    answer = cells[0] - cells[-1]
    return answer


if __name__ == "__main__":
    X = list(map(int, sys.stdin.readline().split()))
    AI = list(map(int, sys.stdin.readline().split()))
    print(solve(AI))
