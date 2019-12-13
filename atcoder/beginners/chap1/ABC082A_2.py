# Problem https://atcoder.jp/contests/abc081/tasks/abc081_a
# Python 2nd Try


def solver(a, b):
    answer = 0
    answer = (a + b + 1) // 2
    return answer


if __name__ == "__main__":
    a, b = map(int, input().split(' '))
    answer = 0
    answer = solver(a, b)
    print(answer)
