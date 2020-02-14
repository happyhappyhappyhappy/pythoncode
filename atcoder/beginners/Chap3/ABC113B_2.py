# Problem https://atcoder.jp/contests/abc113/tasks/abc113_b
# Python 2nd Try
import sys


def solver(allplace, maxtemp, targettemp, eachheight):
    answer = 0
    # difftemp = maxtemp # これNG。対策はしょうが無いが素直にfloat変数としての最大値を使う必要あり
    # sample2にて最大21,0の設定が何時までも続いてしまうため
    difftemp = 10.0**5
    for j in range(0, allplace):
        heretemp = abs(targettemp - (maxtemp - eachheight[j]*0.006))
        if heretemp <= difftemp:
            answer = j
            difftemp = heretemp
    return answer+1


if __name__ == "__main__":
    N = list(map(int, sys.stdin.readline().split()))
    T, A = map(float, sys.stdin.readline().split(' '))
    HI = list(map(float, sys.stdin.readline().split(' ')))
    print(solver(N[0], T, A, HI))
