# Problem https://atcoder.jp/contests/abc087/tasks/abc087_b
# Python 1st Try


def solver(dataset):
    result = 0
    for yen500 in range(0, dataset[0]+1):
        for yen100 in range(0, dataset[1]+1):
            for yen050 in range(0, dataset[2]+1):
                sum = yen500*500+yen100*100+yen050*50
                if sum == dataset[3]:
                    result = result + 1
    return result


if __name__ == "__main__":
    datas = []
    for j in range(0, 4):
        datas.append(int(input()))
    print("{}".format(solver(datas)))
