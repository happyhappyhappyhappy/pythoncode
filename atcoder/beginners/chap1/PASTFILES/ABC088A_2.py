# Problem https://atcoder.jp/contests/abc088/tasks/abc088_a
# Python 2nd Try
yes = "Yes"
no = "No"


def canpay(needMoney, oneYen):
    zangaku = needMoney % 500
    if zangaku <= oneYen:
        return True
    else:
        return False


if __name__ == "__main__":

    N = int(input())
    A = int(input())
    result = True
    if canpay(N, A):
        print(yes)
    else:
        print(no)
exit
