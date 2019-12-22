# Problem
# Python 1st Try


def solver(inputStr):
    result = inputStr[0]+str(len(inputStr)-2)+inputStr[-1]
    return result


if __name__ == "__main__":
    result = ''
    result = solver(input())
    print(result)
