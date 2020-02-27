# Problem https://atcoder.jp/contests/abc072/tasks/abc072_b
# Python 2nd Try


class Problem:
    def __init__(self, problemstring):
        self.problemstring = problemstring
        self.length = len(self.problemstring)

    def solve(self):
        result = ''
        analyzestr = self.problemstring
        for j in range(0, self.length, +2):
            result = result.join(analyzestr[j])
        return result


if __name__ == "__main__":
    S = input()
    print(Problem(S).solve())
