# Problem https://atcoder.jp/contests/abc081/tasks/abc081_a
# Python 1st Try


def onecounter(input_square):
    result = 0
    if input_square[0] == '1':
        result = result + 1
    if input_square[1] == '1':
        result = result + 1
    if input_square[2] == '1':
        result = result + 1
    return result


if __name__ == "__main__":
    answer = onecounter(input())
    print(answer)
exit
