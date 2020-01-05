# Problem  https://atcoder.jp/contests/abc069/tasks/abc069_b
# Python 3rd Try


def solver(inputStr) :
    top =  inputStr[0]
    middle = len(inputStr)-2
    endChar = inputStr[-1]
    return top,middle,endChar


if __name__=="__main__" :
    answer1=''
    answer2=0
    answer3=''
    S = input()
    answer1,answer2,answer3= solver(S)
    print(answer1,answer2,answer3,sep='')



