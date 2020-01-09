# Proglem https://atcoder.jp/contests/abc082/tasks/abc082_b
# Python 2nd Try


yes = "Yes"
no = "No"


def solver(sstr, tstr):
    result = True
    sfirst_str = ''.join(sorted(list(sstr)))
    tend_str = ''.join(reversed(sorted(list(tstr))))
#    print(tend_str)
    if sfirst_str < tend_str:
        result = True
    else:
        result = False
    return result


if __name__ == "__main__":
    s = input()
    t = input()
    if solver(s, t):
        print(yes)
    else:
        print(no)
