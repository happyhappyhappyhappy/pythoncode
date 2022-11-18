import sys

# TODO: ここの挙動の確認
def testing(luckynum,testpin):
    firstChar = testpin[0]
    secondChar = testpin[1]
    thirdChar = testpin[2]
    # 一文字目検索
    resultind1 = luchynum.find(firstChar)
    if resultind1 == -1:
        return False
    resultind2 = luchynum.find(secondChar,resultind1+1)
    if resultind2 == -1:
        return False
    resultind3 = luckynum.find(thirdChar,resultind2+1)
    if resultind3 == -1:
        return False
    return True

def int2strprt(num):
    realstr = "{}".format(num)
    if num < 10:
        strs = "00"+realstr
    else:
        if num < 100:
            strs = "0"+realstr
        else:
            strs = realstr
    return strs

def solver(Lucky):
    result = 0
    for luckynumber in range(0,1000):
        checkStrs=int2strprt(luckynumber)
        # print(checkStrs)
        # print("{}-{}-{}".format(checkStrs[0],checkStrs[1],checkStrs[2]))
        if testing(Lucky,checkStrs):
            result = result + 1
    return result


if __name__ == "__main__":
    tmp=input()
    L = sys.stdin.readline()
    print("{}".format(solver(L)))
