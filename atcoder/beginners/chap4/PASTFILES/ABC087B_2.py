# Problem
# Python 2nd Try
import sys


def solver(yen500, yen100, yen050, sumX):
    result = 0
    for j in range(0, yen500+1, +1):
        for k in range(0, yen100+1, +1):
            for m in range(0, yen050+1, +1):
                totalsum = j*500+k*100+m*50
                if sumX == totalsum:
                    result = result + 1
    return result


if __name__ == "__main__":
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    C = int(sys.stdin.readline())
    X = int(sys.stdin.readline())
    # print(A, B, C, X, sep="\n")
    print("{}".format(solver(A, B, C, X)))
