import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
# 入り口→各買い物場所へ行く合計→真ん中の位置にあるものが最短である
# の検証

# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

if __name__ == "__main__":

    person_num=int(input())
    ent_list=[]
    exit_list=[]
    for j in range(person_num):
        ent,exi = MI()
        ent_list.append(ent)
        exit_list.append(exi)
    # print("===== 入り口位置 =====")
    # for j in range(len(ent_list)):
    #     print("{} -> {}".format(j,ent_list[j]))
    # print("===== 出口位置 =====")
    # for j in range(len(exit_list)):
    #     print("{} -> {}".format(j,exit_list[j]))
    # print("-----ソートしました-----")
    ent_list.sort()
    exit_list.sort()
    # print("===== 入り口位置 =====")
    # for j in range(len(ent_list)):
    #     print("{} -> {}".format(j,ent_list[j]))
    # print("===== 出口位置 =====")
    # for j in range(len(exit_list)):
    #     print("{} -> {}".format(j,exit_list[j]))
    eachmin = []
    for j in range(100):
        nowjsdist=0
        for k in range(len(ent_list)):
            nowjsdist=nowjsdist+abs(ent_list[k]-j)
        print("{} -> {}".format(j,nowjsdist))
        eachmin.append([j,nowjsdist])
    mindist = MAXSIZE
    minpos=0
    for j in range(100):
        [x,y]=eachmin[j]
        print("入り口 {} → 総距離 {}".format(x,y))
        if y < mindist:
            mindist = y
            minpos = j
    print("最短総距離 {} この時の位置 {}".format(mindist,minpos))
    flag = minpos in ent_list
    if flag == True:
        midpos = ent_list.index(minpos)
        print("{} は ent_list の {}/{} に見つかりました".format(minpos,midpos,person_num))
    else:
        print("{} は 入り口位置にはありません".format(minpos))