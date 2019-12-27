# Problem https://atcoder.jp/contests/abc082/tasks/abc082_b
# Python 1st Try


yes = "Yes"
no = "No"


def solver(wordStrS, wordStrT):
    result = ""
    wordSStr = ''.join(list(sorted(wordStrS)))
    strTSort = ''.join(list(reversed(list(sorted(wordStrT)))))
    if wordSStr < strTSort:
        result = yes
    else:
        result = no
    return result


if __name__ == "__main__":
    result = ''
    s = input()
    t = input()
    result = solver(s, t)
    print(result)
