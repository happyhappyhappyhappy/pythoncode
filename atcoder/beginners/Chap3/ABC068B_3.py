# Problem https://atcoder.jp/contests/abc068/tasks/abc068_b
# python 3rd Try


import sys


def twoDividedCounter(N):
    answer = 0
    copyNumber = N
    while True:
        print(N+"check")
        if copyNumber % 2 == 0:
            answer = answer + 1
            copyNumber = copyNumber / 2
        else:
            break
    return answer


def solver(N):
    answer = twoDividedCounter(N)
    return answer


if __name__ == "__main__":
    N = list(map(int, sys.stdin))
    print(solver(N[0]))
