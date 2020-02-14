# Problem https://atcoder.jp/contests/abc113/tasks/abc113_b
# Python 2nd Try
import sys


def solver(allplace, maxtemp, targettemp, eachheight):
    answer = 0
    difftemp = maxtemp
    for j in range(0, allplace):
        heretemp = abs(targettemp - (maxtemp - eachheight[j]*0.006))
        print(difftemp, heretemp)
        if heretemp < difftemp:
            answer = j
            difftemp = heretemp
    return answer+1


if __name__ == "__main__":
    N = list(map(int, sys.stdin.readline().split()))
    T, A = map(float, sys.stdin.readline().split(' '))
    HI = list(map(float, sys.stdin.readline().split(' ')))
    print(solver(N[0], T, A, HI))
