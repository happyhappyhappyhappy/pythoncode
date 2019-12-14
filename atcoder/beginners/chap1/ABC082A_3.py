# Problem https://atcoder.jp/contests/abc082/tasks/abc082_a
# Python 3rd Try
from math import ceil


def ceil2number(a, b):
    result = 0
    c = (a + b) / 2
    result = ceil(c)
    return result


if __name__ == "__main__":
    answer = 0
    a, b = map(int, input().split(' '))
    answer = ceil2number(a, b)
    print(answer)
