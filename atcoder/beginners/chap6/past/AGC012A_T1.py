# _*_ coding:utf-8 _*_
#  Atcoder_Beginners_Contest-
#  Atcoder_Grand_Contest012-A
#  https://atcoder.jp/contests/agc012/tasks/agc012_a


def maxLevel(memberNumber, orgMemberLevelList):

    maxLevelSortedList = sorted(orgMemberLevelList, reverse=True)
    print(maxLevelSortedList)
    maxLevelScore = 0
    checkMemberCountRange = range(0, memberNumber, +1)
    for i in checkMemberCountRange:
        print("Use Position[{}] = {}".format(2*i+1, maxLevelSortedList[2*i+1]))
        maxLevelScore = maxLevelScore+maxLevelSortedList[2*i+1]
    answer = maxLevelScore
    return answer


if __name__ == '__main__':
    N = int(input().strip())
    levelNoSortList = list(map(int, input().strip().split(' ')))
    solution = maxLevel(N, levelNoSortList)
    print("{}".format(solution))
