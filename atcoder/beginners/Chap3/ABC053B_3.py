# Problem https://atcoder.jp/contests/abc053/tasks/abc053_b
# Python 3rd Try
import copy


def solver(givenstring):
    result = 0
    usestrA = copy.copy(givenstring)
    usestrZ = copy.copy(givenstring)
# a position
    apos = usestrA.index('A')+1
    usestrrevZ = usestrZ[::-1]
    zpos = len(givenstring) - usestrrevZ.index('Z')
    result = zpos - apos + 1
    return result


if __name__ == "__main__":
    s = input()
    print("{}".format(solver(s)))
