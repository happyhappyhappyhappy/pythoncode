# Problem https://atcoder.jp/contests/abc085/tasks/abc085_a
# Python 2nd Try
# import pprint


def solver(errorStr):
    result = '2018'
#    pprint.pprint(errorStr)
    monthDay = errorStr[4:]
#    pprint.pprint(monthDay)
    result = result + monthDay
    return result


if __name__ == "__main__":
    result = ''
    result = solver(input())
    print(result)
