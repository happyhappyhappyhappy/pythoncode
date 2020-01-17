# Problem https://atcoder.jp/contests/abc081/tasks/abc081_b
# Python 1st Try
import sys

def solve(allNumber,eachNum):
    answer = 0
    counter = [0]*allNumber
    for j in range(len(eachNum)):
        cnt = 0
        while eachNum[j] % 2 == 0:
            counter[j] = counter[j] + 1
            eachNum[j] = eachNum[j] / 2
#    print(counter)


#   TODO: ここに最大値を設定してcounter配列を回す
#   NOTE: 最小値はどこか→Python3で整数型の最大値はsys.maxsizeとして定義

    answer = 1000
##    for j in range(0,len(eachNum)):
        ## if counter[j] <= answer :
        ##    {
        ##        answer = counter[j]
        ##    }
    return answer

if __name__ == "__main__":
    input=sys.stdin.readline
    N = list(map(int,input().split()))
    Ai = list(map(int,input().split()))
    print(solve(N[0],Ai))