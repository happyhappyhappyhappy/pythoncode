# Problem https://atcoder.jp/contests/abc113/tasks/abc113_b
# Python 1st Try
import sys


def solver(allNum, MaxTemp, TargetTemp, heightPlace):
    answer = 0
    minDiff = MaxTemp
    for j in range(0, allNum):
        diffTemp = abs(TargetTemp - (MaxTemp-heightPlace[j]*0.006))

    return answer+1


if __name__ == "__main__":
    N = list(map(int, sys.stdin.readline().rsplit()))
    print(type(N))
    sLine = list(map(float, sys.stdin.readline().split()))
    Hi = list(map(float, sys.stdin.readline().split()))
    print(solver(N[0], sLine[0], sLine[1], Hi))
