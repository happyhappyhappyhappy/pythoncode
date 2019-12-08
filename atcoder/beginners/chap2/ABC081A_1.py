# Problem https://atcoder.jp/contests/abc081/tasks/abc081_a
# Python 1st Try


def onecounter(input_square):
    strList = list(map(int, input_square.split('')))
    print(strList)
    result = 0
    if strList[0] == 1:
        result = result + 1
    if strList[1] == 1:
        result = result + 1
    if strList[2] == 1:
        result = result + 1
    return result


if __name__ == "__main__":
    answer = onecounter(input())
    print(answer)
exit
