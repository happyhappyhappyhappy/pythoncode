# Problem https://atcoder.jp/contests/abc095/tasks/abc095_a
# Python 2nd Try


def solver(memo):
    result = 700
    for j in range(len(memo)):
        if memo[j] == 'o':
            result = result + 100
    return result


if __name__ == "__main__":
    result = 0
    result = solver(input())
    print(result)
