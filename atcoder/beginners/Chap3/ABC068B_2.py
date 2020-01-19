# Problem
# Python 2nd Try
import sys


def solver(allNumber, eachNum, useRange):
    answer = sys.maxsize
    counter = [0]*allNumber
    for j in useRange:
        while True:
            if eachNum[j] % 2 == 0:
                counter[j] = counter[j] + 1
                eachNum[j] = eachNum[j] / 2
            else:
                break
#       print(counter[j])

    for j in useRange:
        if counter[j] <= answer:
            answer = counter[j]
    return answer


if __name__ == "__main__":
    N = int(input())
    Ai = list(map(int, input().split(' ')))
#    print(Ai)
    print(solver(N, Ai, range(0, N)))
