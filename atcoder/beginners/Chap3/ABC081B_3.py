# Problem https://atcoder.jp/contests/abc081/tasks/abc081_b
# Python 3rd Try
import sys


def solve(N, Ai):
    answer = sys.max
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
    return answer

if __name__ == "__main__":
    print(solve(N, Ai))