# Problem https://atcoder.jp/contests/abc086/tasks/abc086_a
# Python 2nd try
yes = "Odd"
no = "Even"
if __name__ == "__main__":
    a,b =  map(int,input().split(' '))
    answer = ""
    check = (a*b)%2
    if check == 1:
        answer = yes
    else:
        answer = no
    print(answer)