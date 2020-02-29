# Problem https://atcoder.jp/contests/abc053/tasks/abc053_b
# Python 1st Try


class Problem:
    def __init__(self, stringdata):
        self.stringdata = stringdata

    def solver(self):
        result = 0
        return result


if __name__ == "__main__":
    s = "QWERTYASDFZXCV"
    print('{} => {} =? 5'.format(s, Problem(s).solver()))
    s = "ZABCZ"
    print('{} => {} =? 4'.format(s, Problem(s).solver()))
    s = "HASFJGHOGAKZZFEGA"
    print('{} => {} =? 12'.format(s, Problem(s).solver()))
