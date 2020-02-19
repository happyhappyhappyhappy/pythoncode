# Problem https://atcoder.jp/contests/abc113/tasks/abc113_b
# Python 3rd Try


class Problem:
    def __init__(self, allnumber, maxthermo, avepoint, highs):
        self.allnumber = allnumber
        self.maxthermo = maxthermo
        self.avepoint = avepoint
        self.highs = highs

    def problemprint(self):
        print(self.allnumber)
        print(self.maxthermo)
        print(self.avepoint)
        print(self.highs)


if __name__ == "__main__":
    N = 10
    T = 20
    A = 30
    HI = [1, 2, 3, 4]
#    print(Problem(N, T, A, HI).solve())
    Problem(N, T, A, HI).problemprint()
