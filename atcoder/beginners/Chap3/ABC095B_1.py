# Problem https://atcoder.jp/contests/abc095/tasks/abc095_b
# Python 1st Try


def solver(kinddonus, eachsource, havesource):
    result = 0
    allsource = 0
    minsource = 1000
    for j in range(0, kinddonus, +1):
        allsource = eachsource[j] + allsource
        if eachsource[j] <= minsource:
            minsource = eachsource[j]
    result = kinddonus + (havesource - allsource) // minsource
    return result


if __name__ == "__main__":
    N, X = list(map(int, input().split(' ')))
    M = []
    for j in range(0, N, +1):
        M.append(int(input()))
    print(solver(N, M, X))
