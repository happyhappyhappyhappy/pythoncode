# Problem https://atcoder.jp/contests/abc095/tasks/abc095_b
# Python 2nd Try


def solver(donuskind, eachgram, givenpow):
    result = 0
    eachonesum = sum(eachgram)
    mingram = min(eachgram)
    result = donuskind + ((givenpow - eachonesum) // mingram)
    return result


if __name__ == "__main__":
    N, X = map(int, input().split())
    gram = []
#    print("N={} X={}".format(N, X))
    for j in range(0, N, +1):
        gram.append(int(input()))
    print("{}".format(solver(N, gram, X)))
#    print("gram = {}".format(gram))
