# Problem https://atcoder.jp/contests/abc095/tasks/abc095_a
# Python 1st Try


def addCost(infoTicket):
    result = 0
    if infoTicket[0] == 'o':
        result = result + 100
    if infoTicket[1] == 'o':
        result = result + 100
    if infoTicket[2] == 'o':
        result = result + 100
    return result


def solver(inputstr):
    result = 0
    result = 700 + addCost(inputstr)
    return result


if __name__ == "__main__":
    answer = 0
    answer = solver(input())
    print(answer)
