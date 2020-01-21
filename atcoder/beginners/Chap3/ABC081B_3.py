# Problem https://atcoder.jp/contests/abc081/tasks/abc081_b
# Python 3rd Try
import math


def solve(N, Ai):
    answer = int(math.log2(10**9)) + 1
    eachCounter = [0] * N
    for j in range(0, N):
        counter = 0
        while True:
            if Ai[j] % 2 == 0:
                counter = counter + 1
                Ai[j] = Ai[j] / 2
            else:
                break
        eachCounter[j] = counter
    for j in range(0, N):
        if eachCounter[j] < answer:
            answer = eachCounter[j]

    return answer


if __name__ == "__main__":
    N = int(input())
    Ai = list(map(int, input().split(' ')))
    print(solve(N, Ai))
