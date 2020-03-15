# Problem https://atcoder.jp/contests/abc095/tasks/abc095_b
# Python 3rd Try


def solver(donuskind, maxpowder, eachpowder):
    result = donuskind  # mindonuts
    sumpowder = 0
    minpowder = 10**5
    # print(eachpowder)
    for j in eachpowder:
        sumpowder = sumpowder + j
        if j <= minpowder:
            minpowder = j
    # print(minpowder, sumpowder)
    result = result + (maxpowder - sumpowder) // minpowder
    return result


if __name__ == "__main__":
    m = []
    N, X = map(int, input().split(' '))
    for j in range(0, N):
        m.append(int(input()))
    print("{}".format(solver(N, X, m)))
