# Problem
# Python 3rdTry 
yes = "Odd"
no = "Even"
if __name__ == "__main__":    
    answer = ""
    a, b = map(int, input().split(' '))
    if (a*b) % 2 == 1:
        print(yes)
    else:
        print(no)
    print(answer)
