# Problem https://atcoder.jp/contests/abc095/tasks/abc095_a
# Python 3rd Try


def solver(memoStr):
    result = 700
    if memoStr[0] == 'o':
        result = result + 100
    if memoStr[1] == 'o':
        result = result + 100
    if memoStr[2] == 'o':
        result = result + 100
    return result


if __name__ == "__main__":
    result = 0
    result = solver(input())
    print(result)
