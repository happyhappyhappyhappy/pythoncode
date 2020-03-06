# Problem https://atcoder.jp/contests/abc072/tasks/abc072_b
# Python 3rd Try
import copy


class Problem:
    def __init__(self, inputstring):
        self.inputstring = inputstring

    def __str__(self):
        return self.inputstring

    def solver(self):
        result = ''
        string = copy.copy(self.inputstring)
        result = string[0:len(string):2]
        return result


if __name__ == "__main__":
    s = input()
    x = Problem(s)
    print(x.solver())
