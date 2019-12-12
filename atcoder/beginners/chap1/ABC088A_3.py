# Problem https://atcoder.jp/contests/abc088/tasks/abc088_a
# Python 3rd Try
yes = "Yes"
no = "No"


def solver(total, haveOneYen):

    result = False
    oneYenNeed = total % 500
    if oneYenNeed <= haveOneYen:
        result = True
    return result


if __name__ == "__main__":

    answer = ""
    N = int(input())
    A = int(input())
    answer = solver(N, A)
    if answer:
        print(yes)
    else:
        print(no)
