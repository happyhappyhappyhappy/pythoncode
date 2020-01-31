# Problem https://atcoder.jp/contests/abc068/tasks/abc068_b
# python 3rd Try


import sys


def twoDividedCounter(N):
    answer = 0
    copyNumber = N
    while True:
        if copyNumber % 2 == 0:
            answer = answer + 1
            copyNumber = copyNumber / 2
        else:
            break
    return answer


def solver(N):
    answer = 1
    counter = 0
    for j in range(1, N+1):
        jcount = twoDividedCounter(j)
        if counter < jcount:
            answer = j
            counter = jcount

    return answer


if __name__ == "__main__":
    N = sys.stdin.readline().rsplit()
    print(solver(int(N[0])))
