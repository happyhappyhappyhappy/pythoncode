# Problem https://atcoder.jp/contests/abc068/tasks/abc068_b
# Python 2nd Try


def solver(givenNumber):
    answer = 0
    counter = 0
    for j in range(0, givenNumber):
        counter = 0
        modCounter = 0
        baseNumber = j + 1
        while True:
            if baseNumber % 2 == 0:
                modCounter = modCounter + 1
                baseNumber = baseNumber / 2
            else:
                break
        if answer <= counter:
            answer = counter
    return answer


if __name__ == "__main__":
    N = int(input())
    print(solver(N))
