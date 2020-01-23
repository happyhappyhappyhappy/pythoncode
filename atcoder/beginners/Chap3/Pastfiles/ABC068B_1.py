# Problem https://atcoder.jp/contests/abc068/tasks/abc068_b
# Python 1st Try


def solver(givenNum):

    answer = 1
    counter = 0
    rangeNum = range(0, givenNum)
    eachCount = [0] * givenNum
    for j in rangeNum:
        oneCount = 0
        nowNumber = j + 1
        while True:
            if nowNumber % 2 == 0:
                oneCount = oneCount + 1
                nowNumber = nowNumber / 2
            else:
                break
        eachCount[j] = oneCount
#    print(eachCount)
    for j in rangeNum:
        if counter <= eachCount[j]:
            counter = eachCount[j]
            answer = j + 1
    return answer


if __name__ == "__main__":
    print(solver(int(input())))
