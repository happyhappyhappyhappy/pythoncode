# Problem https://atcoder.jp/contests/abc082/tasks/abc082_a
# Python 1st Try


def orginalCeil(a, b):
    c = (a + b + 1) // 2
    return c


if __name__ == "__main__":
    a, b = map(int, input().split(' '))
    answer = orginalCeil(a, b)
    print(answer)
exit
