# Problem: https://atcoder.jp/contests/agc012/tasks/agc012_a
# Python 1st Try

import sys
# from collections import defaultdict
# import heapq,copy
# from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solver(eachPoints):
    result = 0
    menbers = len(eachPoints)
    group = menbers // 3
    eachPoints.sort(reverse=False)
#    print(eachPoints)
    useSkillList = []
    #  最初のグループ個だけカットしたリストを新規作成[0,1,2,3,4,5]->[2,3,4,5]
    for ui in range(group, menbers, +1):
        useSkillList.append(eachPoints[ui])
#    print("UseListOnly {}".format(useSkillList))
    # for pi in range(0, menbers):
    #    if pi // group == 1:
    #        print("Get Position -> {}={}".format(pi, eachPoints[pi]))
    #        result = result + eachPoints[pi]
    # algorithm
    for sum2pos in range(0, len(useSkillList), +2):
        result = useSkillList[sum2pos] + result
    return result


if __name__ == "__main__":
    _ = II()
    AI = LI()
    print("{}".format(solver(AI)))
