# Problem https://atcoder.jp/contests/abc072/tasks/abc072_b
# Python 1st Try
import sys


def solver(inputStr):
    answer = ''
    answerList = []
    for j in range(0, len(inputStr), 2):
        answerList.append(inputStr[j])
    answer = ''.join(answerList)
    return answer


if __name__ == "__main__":
    s = sys.stdin.readline().split()
    print(solver(s[0]))
