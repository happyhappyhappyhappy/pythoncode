# Problem https://atcoder.jp/contests/abc081/tasks/abc081_a
# Python 3rd Try


def solver(str):
    result = 0
    if str[0] == '1':
        result = result + 1
    if str[1] == '1':
        result = result + 1
    if str[2] == '1':
        result = result + 1

    return result


if __name__ == "__main__":
    result = 0
    result = solver(input())
    print(result)
