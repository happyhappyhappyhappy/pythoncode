if __name__ == "__main__":
    grams = [100, 200, 300, 250]
    maxgrams = 0
    sumgrams = 0
    for j in grams:
        if maxgrams <= j:
            maxgrams = j
        sumgrams = sumgrams + j
    print("maxgrams = {}".format(maxgrams))
    print("sum = {}".format(sumgrams))
