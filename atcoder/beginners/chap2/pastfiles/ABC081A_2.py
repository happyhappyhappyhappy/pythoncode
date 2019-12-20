# Problem https://atcoder.jp/contests/abc081/tasks/abc081_a
# Python 2nd Try


def solver(marble):
    result = 0
    n = marble
    while 0 < n:
        scaleNo = n % 10
        result = result + scaleNo
        n = n // 10
    return result


if __name__ == "__main__":
    answer = 0
    answer = solver(int(input()))
    print(answer)
