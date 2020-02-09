# Problem https://atcoder.jp/contests/abc113/tasks/abc113_b
# Python 1st Try
import sys


def solver(allnum, maxtemp, targettemp, heightplace):

    answer = 0
    mindiff = 100000000
    for j in range(0, allnum):
        difftemp = abs(targettemp - (maxtemp-heightplace[j]*0.006))
        if difftemp < mindiff:
            mindiff = difftemp
            answer = j
    return answer+1


if __name__ == "__main__":
    N = list(map(int, sys.stdin.readline().rsplit()))
    SLINE = list(map(float, sys.stdin.readline().split()))
    HI = list(map(float, sys.stdin.readline().split()))
    print(solver(N[0], SLINE[0], SLINE[1], HI))
