BASE = 3


def accumu(base, j):
    result = 1
    # a = 1
    while (0 < j):
        if (j & 1):
            result = base * result
        base = base * base
        # print("{}".format(j))
        j = j >> 1
        # print("{}".format(j))
    return result


if __name__ == "__main__":
    N = int(input())
    for j in range(1, N, +1):
        res = accumu(BASE, j)
        print("{} の {} 乗は {}".format(BASE, j, res))
