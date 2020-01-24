# Problem https://atcoder.jp/contests/abc068/tasks/abc068_b
# Python 2nd Try


def solver(givenNumber):
    answer = 1
    counter = 0
    modCounter = [0] * givenNumber
    for j in range(0, givenNumber):
        eachCounter = 0
        baseNumber = j + 1
        while True:
            if baseNumber % 2 == 0:
                eachCounter = eachCounter + 1
                baseNumber = baseNumber / 2
            else:
                break
        modCounter[j] = eachCounter
    for j in range(0, givenNumber):
        if counter <= modCounter[j]:
            counter = modCounter[j]
            answer = j+1
    return answer


if __name__ == "__main__":
    N = int(input())
    print(solver(N))
