# Problem https://atcoder.jp/contests/abc085/tasks/abc085_a
# Python 3rd Try
import copy


def solver(errorStr):
    strList = list(errorStr)
    trueList = copy.deepcopy(strList)
    trueList[3] = '8'
    result = ''.join(trueList)
    return result


if __name__ == "__main__":
    result = ""
    result = solver(input())
    print(result)
