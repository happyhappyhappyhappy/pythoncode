BASE = 2


def accumu(base, j):
    result = 1
    a = 1
    while 0 < j:
        if j & 1:
            result = result  * a
        a = base * base
        j = j >> 1
    return result


if __name__ == "__main__":
    N = int(input())
    for j in range(0, N, +1):
        res = accumu(BASE, j)
        print("{} no {} jou {}".format(BASE, j, res))
