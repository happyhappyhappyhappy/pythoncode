# Problem https://atcoder.jp/contests/abc102/tasks/abc102_b
# Python 2nd Try
import sys


def solver(allN, numberList):
    answer = 0
    for j in range(0, allN):
        for k in range(0, allN):
            nowAbs = (numberList[j] - numberList[k]).__abs__()
            if answer < nowAbs:
                answer = nowAbs
    return answer


if __name__ == "__main__":
    N = sys.stdin.readline().rsplit()
    Ai = list(map(int, sys.stdin.readline().split()))
    answer = solver(int(N[0]), Ai)
    print(answer)
