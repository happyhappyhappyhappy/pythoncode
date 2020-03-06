# Problem https://atcoder.jp/contests/abc072/tasks/abc072_b
# Python 2nd Try


class Problem:
    def __init__(self, problemstring):
        self.problemstring = problemstring
        self.length = len(self.problemstring)

    def solve(self):
        result = ''
        resultlist = []
        for j in range(0, self.length):
            if j % 2 == 0:
                resultlist.append(self.problemstring[j])
        result = ''.join(resultlist)
        return result


if __name__ == "__main__":
    #    S = "atcoder"
    #    print("{} => {}".format(S, Problem(S).solve()))
    #    S = "aaaa"
    #    print("{} => {}".format(S, Problem(S).solve()))
    #    S = "z"
    #    print("{} => {}".format(S, Problem(S).solve()))
    S = input()
    print(Problem(S).solve())
