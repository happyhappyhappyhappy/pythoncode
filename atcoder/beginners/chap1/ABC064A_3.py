# Problem
# Python 3rd Try
yes = "YES"
no = "NO"
if __name__ == "__main__":
    r, g, b = map(int, input().split(' '))
    answer = ""
    checkNo = (g*10+b) % 4
    if checkNo == 0:
        answer = yes
    else:
        answer = no
    print(answer)
exit
