# Problem https://atcoder.jp/contests/abc088/tasks/abc088_a
# Python 1st Try
if __name__ == "__main__":
    yes = "Yes"
    no = "No"
    answer = ""
    N = int(input().strip())
    A = int(input().strip())
    chargeCoin = N % 500
    if chargeCoin <= A:
        answer = yes
    else:
        answer = no
    print(answer)
exit
