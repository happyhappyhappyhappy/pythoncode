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

    def solve(self):
        maxdiff = 100000.0
        result = 1
        for j in range(0, self.allnumber):
            difftemp = abs(self.avepoint-(self.maxthermo-self.highs[j]*0.006))
#            print('{}->{}'.format(maxdiff,difftemp))
            if difftemp < maxdiff:
                maxdiff = difftemp
                result = j+1
        return result


if __name__ == "__main__":
    N = int(input())
    T, A = map(float, input().split(' '))
    HI = list(map(float, input().split(' ')))
    print(Problem(N, T, A, HI).solve())
#    print(Problem(2, 12.5, 5.0, [1000.0, 2000.0]).solve())
#    print(Problem(3, 21.0, 11.0, [81234.0, 94124.0, 52141.0]).solve())
