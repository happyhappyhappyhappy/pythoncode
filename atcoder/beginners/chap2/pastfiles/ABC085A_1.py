# Problem https://atcoder.jp/contests/abc085/tasks/abc085_a
# Python 1st Try


def solver(errorDay):
    result = "2018/01/"
    day = errorDay[8:]
    #   print(day)
    result = result+day
    return result


if __name__ == "__main__":
    result = ""
    result = solver(input())
    print(result)
