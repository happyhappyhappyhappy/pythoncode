# Problem https://atcoder.jp/contests/abc053/tasks/abc053_b
# Python 2nd Try


def solver(string):
    result = 200000
    aposi = 0
    zposi = len(string)
    for j in range(0, len(string), 1):
        if string[j] == 'A':
            aposi = j
            break
    for j in range(len(string)-1, -1, -1):
        if string[j] == 'Z':
            zposi = j
            break
    result = zposi - aposi + 1
    return result


if __name__ == "__main__":
    s = input()
    print('{}'.format(solver(s)))
