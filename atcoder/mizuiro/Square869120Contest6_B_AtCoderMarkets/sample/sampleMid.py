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
    pos_list=LI()
    for j in range(pos_list.count()):
        print(pos_list[j])
#    for j in range(person_num):
#        apint = int(input())
#        print(apint)
#        pos_list.append(int(input()))
#    for j in range(pos_list.count()):
#        print("{} -> {}".format(j,pos_list[j]))
